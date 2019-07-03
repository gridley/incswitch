# incswitch
Switch between header and source files quickly in neovim. Directories are searched recursively.

# Recommended setup:
`pip3 install --user pynvim`

add this to your init.vim, after ensuring [vim-plug](https://www.linode.com/docs/tools-reference/tools/how-to-install-neovim-and-plugins-with-vim-plug/) works:

`Plug gridley/incswitch`

Lastly, set up a keyboard shortcut for switching between source and header files. Ctrl-h is a good one:

`echo 'map <C-h> :IncSwitch <CR>' >> ~/.config/nvim/init.vim`

# TODO
Cache location of source/header pair to avoid need to search each time.
Come back to same line number when switching.
