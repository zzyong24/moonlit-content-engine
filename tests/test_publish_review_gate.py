import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from datetime import datetime, timezone, timedelta

spec = importlib.util.spec_from_file_location('gate', Path(__file__).resolve().parents[1] / 'scripts/publish_review_gate.py')
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


class GateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='publish review with spaces ')
        self.root = Path(self.temp.name)
        self.skill = self.root / 'guoshen'
        (self.skill / 'resources').mkdir(parents=True)
        (self.skill / 'SKILL.md').write_text('review process')
        (self.skill / 'resources/VERSION').write_text('0.2.0')
        self.source = self.root / 'content.md'; self.source.write_text('真实复盘')
        self.now = datetime.now(timezone.utc)
        for name in ('report.md', 'context.json', 'evidence.json'):
            (self.root / name).write_text('actual fixture review data')
        self.data = {'schemaVersion': 1, 'skill': 'guoshen', 'reviewedAt': self.now.isoformat(),
          'skillTreeSha256': gate.tree_sha(self.skill),
          'skillFiles': {name: gate.sha(self.skill / name) for name in ('SKILL.md', 'resources/VERSION')},
          'inputs': [{'path': 'content.md', 'sha256': gate.sha(self.source)}],
          'platforms': {'douyin': {'decision': '未发现明显问题', 'blockingFindings': 0,
             'coverage': 'complete', 'semanticReview': True, 'officialSourcesReviewed': True}}}
        for key, name in [('report','report.md'),('ruleContext','context.json'),('evidence','evidence.json')]:
            self.data[key] = [{'path': name, 'sha256': gate.sha(self.root / name)}]

    def tearDown(self): self.temp.cleanup()
    def run_check(self, platform='douyin', stage='final'):
        p = self.root / 'receipt.json';p.write_text(json.dumps(self.data))
        return gate.check(p, [platform], [self.source], self.skill, self.now, stage=stage)
    def test_current_review_passes_without_granting_authorization(self):
        self.assertEqual(self.run_check()['status'], 'preflight_passed')
    def test_changed_content_fails(self):
        self.source.write_text('修改了发布正文')
        with self.assertRaisesRegex(ValueError, '输入变化'): self.run_check()
    def test_missing_report_and_candidate_only_fail(self):
        self.data['platforms']['douyin']['semanticReview'] = False
        with self.assertRaisesRegex(ValueError, '候选扫描'): self.run_check()
        self.data['platforms']['douyin']['semanticReview'] = True
        self.data['report'] = []
        with self.assertRaisesRegex(ValueError, '真实审核产物'): self.run_check()
    def test_expired_and_wrong_platform_fail(self):
        with self.assertRaisesRegex(ValueError, '未通过'): self.run_check('bilibili')
        self.data['reviewedAt'] = (self.now - timedelta(days=2)).isoformat()
        with self.assertRaisesRegex(ValueError, '过期'): self.run_check()
    def test_rule_version_and_report_edit_fail(self):
        (self.skill / 'resources/VERSION').write_text('0.3.0')
        with self.assertRaisesRegex(ValueError, '版本已变'): self.run_check()
    def test_unsupported_platform_requires_actual_supplemental_review(self):
        self.data['platforms']['wechat_article'] = dict(self.data['platforms']['douyin'])
        with self.assertRaisesRegex(ValueError, '补充审核'): self.run_check('wechat_article')
        self.data['platforms']['wechat_article']['supplementalPlatformReview'] = True
        self.assertTrue(self.run_check('wechat_article')['success'])

    def test_content_only_allows_draft_but_never_final(self):
        final = {'decision': '未检查', 'blockingFindings': 1, 'coverage': 'incomplete'}
        content = dict(self.data['platforms']['douyin'])
        content['deferredChecks'] = ['nativeSettings', 'platformCoverCrop']
        self.data['platforms']['douyin'] = {'stages': {'content': content, 'final': final}}
        self.assertTrue(self.run_check(stage='content')['success'])
        with self.assertRaisesRegex(ValueError, '最终页面证据'):
            self.run_check()
        content['deferredChecks'].append('speech')
        with self.assertRaisesRegex(ValueError, '只允许延期'):
            self.run_check(stage='content')

    def test_final_native_evidence_must_be_hash_bound(self):
        complete = dict(self.data['platforms']['douyin'])
        self.data['platforms']['douyin'] = {'stages': {'content': complete, 'final': dict(complete)}}
        final = self.data['platforms']['douyin']['stages']['final']
        for key in ('nativeSettingsEvidence', 'platformCoverEvidence'):
            f = self.root / (key + '.json'); f.write_text('actual reviewed page evidence')
            final[key] = {'path': f.name, 'sha256': gate.sha(f)}
        with self.assertRaisesRegex(ValueError, '未绑定'):
            self.run_check()
        self.data['inputs'].extend(final[k] for k in ('nativeSettingsEvidence', 'platformCoverEvidence'))
        self.assertTrue(self.run_check()['success'])
        (self.root / 'nativeSettingsEvidence.json').write_text('changed native label')
        with self.assertRaisesRegex(ValueError, '输入变化'):
            self.run_check()


if __name__ == '__main__': unittest.main()
