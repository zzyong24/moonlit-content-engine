#!/usr/bin/env python3
"""naming_helper.py — 月明内容引擎的文件命名助手（v0.5.1 规范）

内容文件命名：MMDDHHMM-[纯中文主题]-平台.md
图片文件命名：[序号]-[含义].png

用法：
    python3 naming_helper.py content "AI工具三个坑" "公众号"
        → 输出：2608261140-AI工具三个坑-公众号.md

    python3 naming_helper.py image 1 "3件事钩子"
        → 输出：1-3件事钩子.png

    python3 naming_helper.py image "对比表"
        → 输出：对比表.png（无序号）
"""
import sys
from datetime import datetime


def now():
    """返回 MMDDHHMM（6 位数字无连字符）"""
    return datetime.now().strftime('%y%m%d%H%M')


def content_name(topic, platform):
    """生成内容文件名：MMDDHHMM-[主题]-平台.md"""
    now_str = now()
    # 主题保留中文+空格（不需要转换）
    return f'{now_str}-{topic}-{platform}.md'


def image_name(num, meaning):
    """生成图片文件名：[序号]-[含义].png"""
    if num is None:
        return f'{meaning}.png'
    return f'{num}-{meaning}.png'


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == 'content':
        if len(sys.argv) != 4:
            print('用法: python3 naming_helper.py content "[主题]" "[平台]"')
            sys.exit(1)
        print(content_name(sys.argv[2], sys.argv[3]))
    elif cmd == 'image':
        if len(sys.argv) == 3:
            print(image_name(None, sys.argv[2]))
        elif len(sys.argv) == 4:
            try:
                num = int(sys.argv[2])
                print(image_name(num, sys.argv[3]))
            except ValueError:
                print('用法: python3 naming_helper.py image [序号] "[含义]"')
                sys.exit(1)
        else:
            print('用法: python3 naming_helper.py image [序号] "[含义]"')
            sys.exit(1)
    else:
        print(f'未知命令: {cmd}')
        sys.exit(1)


if __name__ == '__main__':
    main()