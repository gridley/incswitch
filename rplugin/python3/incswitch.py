import pynvim 
import os

@pynvim.plugin
class IncSwitch:

    def __init__(self, nvim):
        self.nvim = nvim

        # Avoid searching for files if they've already been found once.
        self.cachedLocs = {} 

    @pynvim.command('IncSwitch')
    def incswitch(self):

        # Feel free to add more stuff here:
        headers = {'.h', '.hpp', '.H', '.hh', '.hxx'}
        sources = {'.c', '.cpp', '.cxx', '.C', '.cu'}

        # Get current file name
        thisfile = self.nvim.command_output('echo @%').strip()
        cwd = self.nvim.command_output('pwd').strip()

        # if file has been found before, use cached location.
        if thisfile in self.cachedLocs.keys():
            filepath = self.cachedLocs[thisfile]

        # Search for header/source file
        else:
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

            # start search two directories up from current location. This is
            # roughly applicable to most code projects where an include directory
            # is unlikely to be more than two levels away from a src directory.
            cwd = os.path.join(cwd, '..')
            cwd = os.path.join(cwd, '..')

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

            filepath = os.path.join(root, name)

            # Save location so there's no need to search again.
            self.cachedLocs[thisfile] = filepath


        comm = 'edit ' + filepath
        self.nvim.command(comm)
