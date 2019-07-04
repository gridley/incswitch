# incswitch
This is great for C++ projects where headers and source files are in different directories.

Switch between header and source files quickly in neovim. Directories are searched recursively.
For example, if a file called calcmeaningoflife.C and calcmeaningoflife.h are the in same directory, a keybinding
is provided to automatically switch between files. Also, if one of the files were nested a few directories below
the current working directory, this extension would switch to that file as well since it searches directories
recursively. After finding the location of the corresponding header/source pair once, the location is cached
to slightly improve the speed of switching files after the first switch.

Currently, the program treats source files as anything with one of the following extensions
`sources = {'.c', '.cpp', '.cxx', '.C'} `

And headers with these:
`headers = {'.h', '.hpp', '.H', '.hh', '.hxx'}`

Notably, it's trivial to add more recognized source/header file extensions, like .f90 if you're a troglodyte.

# Recommended setup:
`pip3 install --user pynvim`
add this to your init.vim, after ensuring
[vim-plug](https://www.linode.com/docs/tools-reference/tools/how-to-install-neovim-and-plugins-with-vim-plug/#install-the-vim-plug-plugin-manager) works:

`Plug gridley/incswitch`

Lastly, set up a keyboard shortcut for switching between source and header files. Ctrl-h is a good one:

`echo 'map <C-h> :IncSwitch <CR>' >> ~/.config/nvim/init.vim`
