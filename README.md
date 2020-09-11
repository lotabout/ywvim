This is a fork of [ywvim](http://www.vim.org/scripts/script.php?script_id=2662).

Table "wubi" and "pinyin" are included.

## Install

Use vimplug

```
Plug 'lotabout/ywvim'
```

Put these in your `.vimrc`:

```
let g:ywvim_ims=[
            \['wb', '五笔', 'wubi.ywvim'],
            \['py', '拼音', 'pinyin.ywvim'],
            \['xh', '小鹤', 'xiaohe.ywvim'],
            \]

let g:ywvim_py = { 'helpim':'wb', 'gb':0 }

let g:ywvim_zhpunc = 1
let g:ywvim_listmax = 10
let g:ywvim_esc_autoff = 0
let g:ywvim_autoinput = 0
let g:ywvim_circlecandidates = 1
let g:ywvim_helpim_on = 1
let g:ywvim_matchexact = 0
let g:ywvim_chinesecode = 1
let g:ywvim_gb = 0
let g:ywvim_preconv = 'g2b'
let g:ywvim_conv = ''
let g:ywvim_lockb = 1
let g:ywvim_theme = 'dark'
let g:ywvim_intelligent_punc = 1
```
