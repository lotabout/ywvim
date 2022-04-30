#!/usr/bin/env python3

# usage:
# ./rime-to-ywvim.py wubi86_jidian.dict.yaml wubi86_jidian_extra.dict.yaml wubi86_jidian.ywvim

mb_header = '''# vim:fileencoding=utf-8:list:listchars=trail\:]:
[Description]
Name=极点五笔86
MaxCodes=4
MaxElement=0
UsedCodes=abcdefghijklmnopqrstuvwxyz
WildChar=*
NumRules=0
PyChar=;

[CharDefinition]

[Punctuation]
~ ～
! ！
( （
) ）
+ ＋
, ，
. 。
\ 、
: ：
; ；
< 《
> 》
? ？
^ ……
_ ──
" “ ”
' ‘ ’
0 0
1 1
2 2
3 3
4 4
5 5
6 6
7 7
8 8
9 9

[Main]
'''

import sys

def loadmb(mb, fp):
    start = False
    for line in fp:
        line = line.strip()
        if start and not line.startswith('#') and len(line) > 0:
            components = line.split('\t')
            char = components[0]
            key = components[1]
            if key in mb:
                mb[key].append(char)
            else:
                mb[key] = [char]
        elif line.startswith('...'):
            start = True

def save_mb_to(mb, fp):
    fp.write(mb_header)
    for key, chars in mb.items():
        fp.write(f'{key} {" ".join(chars)}')
        fp.write('\n')

import sys
if len(sys.argv) < 3:
    print('args: <mb_to_load> <file_to_write>')
    sys.exit(1)

mb = {}
for file in sys.argv[1:-1]:
    print(f'loading from {file}')
    with open(file) as fp:
        loadmb(mb, fp)
with open(sys.argv[-1], 'w') as fp:
    print(f'saving mb to {sys.argv[-1]}')
    save_mb_to(mb, fp)
