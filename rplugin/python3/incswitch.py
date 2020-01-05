import pynvim 
import os

@pynvim.plugin
class IncSwitch:

    # Feel free to add more stuff here:
    headers = {'.h', '.hpp', '.H', '.hh', '.hxx', '.cuh'}
    sources = {'.c', '.cpp', '.cxx', '.C', '.cu'}

    def __init__(self, nvim):
        self.nvim = nvim

        # Avoid searching for files if they've already been found once.
        self.cachedLocs = {} 

    def traverse(self, cwd, thisfile):
        # get file extension
        justfile = os.path.split(thisfile)[-1]
        base, extension = os.path.splitext(justfile)

        # see if headers, or sources being searched for
        if extension in IncSwitch.headers:
            searchFor = IncSwitch.sources
        elif extension in IncSwitch.sources:
            searchFor = IncSwitch.headers
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
        filepath = os.path.join(root, name)

        # Save location so there's no need to search again.
        self.cachedLocs[thisfile] = filepath

        if found:
            return filepath
        else:
            return ""

    @pynvim.command('IncSwitch')
    def incswitch(self):

        # Get current file name
        thisfile = self.nvim.command_output('echo @%').strip()
        cwd = self.nvim.command_output('pwd').strip()

        # if file has been found before, use cached location.
        if thisfile in self.cachedLocs.keys():
            filepath = self.cachedLocs[thisfile]

        # Search for header/source file
        else:
            # Attempt search in current directory
            filepath = self.traverse(cwd, thisfile)

            if not filepath:

                # Attempt the search two directories up
                cwd = os.path.join(cwd, '..')
                cwd = os.path.join(cwd, '..')
                filepath = self.traverse(cwd, thisfile)

                if not filepath:
                    raise Exception('Unable to find corresponding source/header file.')

        comm = 'edit ' + filepath
        self.nvim.command(comm)
