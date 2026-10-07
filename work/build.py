#!/usr/bin/env python3
"""组装夜航图演示文稿:shell + fragments -> 最终单文件 index.html"""
import os, re, sys, json

ROOT = '/Users/dongliang/Documents/projects/agent_book'
FRAG = os.path.join(ROOT, 'work', 'fragments')
SHELL = os.path.join(ROOT, 'work', 'shell.html')
OUT = os.path.join(ROOT, 'index.html')

ORDER = """
cover toc
part-1 c06a c06b c06c c07 c08
part-2 c09 c10 c11a c11b c11code c12a c12b c12code c13 c14 c15 c15code c16a c16b c17a c17b
part-3 c18a c18b
part-4 c19a c19b
part-5 c21a c21b c21code c22a c22b c22code c23a c23b c23code c24 c24code c25 c26 c26code c27a c27b c27codea c27codeb c28 c29a c29b c29code c30a c30b c31a c31b c31code c32a c32b c32code
part-6 c33 c34 c35
end
""".split()

def main():
    shell = open(SHELL, encoding='utf-8').read()
    frags, ids, missing, problems = [], [], [], []
    for name in ORDER:
        path = os.path.join(FRAG, name + '.html')
        if not os.path.exists(path):
            missing.append(name); continue
        html = open(path, encoding='utf-8').read().strip()
        # 校验 section 标签
        secs = re.findall(r'<section\b[^>]*>', html)
        if not secs:
            problems.append(f'{name}: 无 <section>')
        for s in secs:
            m = re.search(r'id="([^"]+)"', s)
            sid = m.group(1) if m else '(no-id)'
            if sid in ids:
                problems.append(f'{name}: 重复 id {sid}')
            ids.append(sid)
            for attr in ('data-part', 'data-crumb', 'data-title'):
                if attr + '="' not in s:
                    problems.append(f'{name}/{sid}: 缺 {attr}')
        if re.search(r'https?://', html):
            problems.append(f'{name}: 含外部 URL')
        if '<script' in html.lower() or '<style' in html.lower():
            problems.append(f'{name}: 含 script/style')
        frags.append(f'<!-- ▸ {name} -->\n{html}')
    shell = shell.replace('<!--FRAGMENTS-->', '\n\n'.join(frags))
    shell = shell.replace('01 / 54', f'01 / {len(ORDER)}') if False else shell
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(shell)
    print(f'✓ 写出 {OUT}  ({os.path.getsize(OUT)/1024:.0f} KB)')
    print(f'  片段 {len(frags)}/{len(ORDER)} · 幻灯片节 {len(ids)} 个')
    if missing: print('  ✗ 缺失:', ', '.join(missing))
    if problems:
        print('  ⚠ 问题:')
        for p in problems: print('   -', p)
    sys.exit(0 if not missing else 1)

if __name__ == '__main__':
    main()
