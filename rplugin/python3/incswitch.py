import pynvim 
import os

@pynvim.plugin
class IncSwitch:

    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.command('IncSwitch')
    def incswitch(self):

        # Feel free to add more stuff here:
        headers = {'.h', '.hpp', '.H', '.hh', '.hxx'}
        sources = {'.c', '.cpp', '.cxx', '.C'}

        # Get current file name
        thisfile = self.nvim.command_output('echo @%').strip()
        cwd = self.nvim.command_output('pwd').strip()

        # get file extension
        justfile = os.path.split(thisfile)[-1]
        base, extension = os.path.splitext(justfile)

        # see if headers, or sources being searched for
        if extension in headers:
            searchFor = sources
        elif extension in sources:
            searchFor = headers
        else:
            raise Exception('No recognized header/source correspondence on this file.')

        # traverse current directory and below to find header or source file
        found = False
        for root, dirs, files in os.walk(cwd):
            for name in files:
                checkFile, checkExt = os.path.splitext(name)
                if checkExt in searchFor and checkFile == base:
                    found = True
                    break
            else:
                continue
            break
        if not found:
            raise Exception('Unable to find corresponding source/header file.')

        comm = 'edit ' + os.path.join(root, name)
        self.nvim.command(comm)
