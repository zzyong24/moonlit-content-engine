#!/usr/bin/env python3
"""Verify a guoshen review receipt against the actual release inputs; not a semantic reviewer."""
import argparse
from datetime import datetime, timezone, timedelta
import hashlib
import json
import os
from pathlib import Path
import sys


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def tree_sha(folder):
    digest = hashlib.sha256()
    excluded = {'node_modules', '__pycache__', '.git', '.DS_Store', '.pytest_cache'}
    for base, dirs, files in os.walk(folder, followlinks=True):
        dirs[:] = sorted(d for d in dirs if d not in excluded)
        for name in sorted(files):
            if name in excluded or name.endswith('.pyc'):
                continue
            p = Path(base) / name
            digest.update(str(p.relative_to(folder)).encode() + b'\0' + sha(p).encode())
    return digest.hexdigest()


def check(receipt_path, platforms, files, guoshen_dir, now=None, stage="final"):
    if stage not in {"content", "final"}:
        raise ValueError("审核阶段必须为 content 或 final")
    now = now or datetime.now(timezone.utc)
    receipt_path = Path(receipt_path).resolve()
    receipt = json.loads(receipt_path.read_text())
    if receipt.get('schemaVersion') != 1 or receipt.get('skill') != 'guoshen':
        raise ValueError('必须提供实际执行 guoshen 后的 v1 审核回执')
    reviewed = datetime.fromisoformat(receipt['reviewedAt'].replace('Z', '+00:00'))
    if reviewed.tzinfo is None or not timedelta(minutes=-5) <= now - reviewed <= timedelta(hours=24):
        raise ValueError('审核已过期或时间无效，发布前重新运行 guoshen')
    skill = Path(guoshen_dir).resolve()
    if receipt.get('skillTreeSha256') != tree_sha(skill):
        raise ValueError('guoshen 规则或资源版本已变，重新审核')
    identity = receipt.get('skillFiles', {})
    # Bind to the activated upstream version. The review context below binds selected rules.
    for relative in ('SKILL.md', 'resources/VERSION'):
        if identity.get(relative) != sha(skill / relative):
            raise ValueError('guoshen 版本已变，重新审核')
    listed = {}
    for row in receipt.get('inputs', []):
        p = (receipt_path.parent / row['path']).resolve()
        if not p.is_file() or sha(p) != row['sha256']:
            raise ValueError('已审输入变化或缺失：' + str(p))
        listed[p] = row['sha256']
    if not files:
        raise ValueError('必须传入这次实际发布的文件，不能只校验回执本身')
    for file in files:
        p = Path(file).resolve()
        if p not in listed:
            raise ValueError('实际发布文件未审核：' + str(p))
    for key in ('report', 'ruleContext', 'evidence'):
        records = receipt.get(key)
        if not isinstance(records, list) or not records:
            raise ValueError('缺少真实审核产物：' + key)
        for row in records:
            p = (receipt_path.parent / row['path']).resolve()
            if not p.is_file() or sha(p) != row['sha256']:
                raise ValueError('审核产物变化或缺失：' + str(p))
    results = receipt.get('platforms', {})
    for platform in platforms:
        platform_result = results.get(platform, {})
        stages = platform_result.get('stages')
        result = stages.get(stage, {}) if isinstance(stages, dict) else platform_result
        if isinstance(stages, dict) and stage == 'content':
            deferred = result.get('deferredChecks', [])
            if not isinstance(deferred, list) or any(x not in {'nativeSettings', 'platformCoverCrop'} for x in deferred):
                raise ValueError(platform + ' 内容门禁只允许延期上传后才出现的原生设置和裁切')
        if isinstance(stages, dict) and stage == 'final':
            for key in ('nativeSettingsEvidence', 'platformCoverEvidence'):
                record = result.get(key)
                if not isinstance(record, dict) or not record.get('path') or not record.get('sha256'):
                    raise ValueError(platform + ' 缺少最终页面证据：' + key)
                p = (receipt_path.parent / record['path']).resolve()
                if p not in listed or listed[p] != record['sha256']:
                    raise ValueError(platform + ' 最终页面证据未绑定实际输入：' + key)
        if result.get('decision') != '未发现明显问题' or result.get('blockingFindings') != 0:
            raise ValueError(platform + ' 未通过发布前预检，修复后重新审核')
        if result.get('coverage') != 'complete' or result.get('semanticReview') is not True:
            raise ValueError(platform + ' 审核未完成，候选扫描不能替代语义审核')
        if result.get('officialSourcesReviewed') is not True:
            raise ValueError(platform + ' 缺少本次官方规则复核')
        if platform not in {'xiaohongshu', 'douyin', 'bilibili', 'wechat_channels'}:
            if result.get('supplementalPlatformReview') is not True:
                raise ValueError(platform + ' 不在上游平台注册表，需完成对应平台补充审核')
    return {'success': True, 'status': 'preflight_passed', 'platforms': platforms,
            'receipt': str(receipt_path), 'stage': stage, 'notice': '发布风险预检，不是平台审核通过或发布授权'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--receipt', required=True, type=Path)
    parser.add_argument('--stage', choices=('content', 'final'), default='final')
    parser.add_argument('--platform', action='append', required=True)
    parser.add_argument('--file', action='append', required=True, type=Path)
    parser.add_argument('--guoshen-dir', required=True, type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(check(args.receipt, args.platform, args.file, args.guoshen_dir, stage=args.stage), ensure_ascii=False))
        return 0
    except (ValueError, KeyError, OSError, TypeError) as error:
        print(json.dumps({'success': False, 'error': str(error)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
