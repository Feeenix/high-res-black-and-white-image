def install_package(*libs):
        import os,sys
        _cwd = str(os.getcwd())
        if not os.path.isdir("libraries"):
            os.mkdir("libraries")
        allmodules = os.listdir("libraries")
        for name in libs:
            fileexists=False
            for s in allmodules:
                if s.find(name) == -1: fileexists = False
                else:
                    fileexists = True
                    print(name,s)
                    break
            if not fileexists:
                command = "pip install "+name+f" --target \"{os.path.join(_cwd,'libraries')}\" --no-user --upgrade"
                print(command)
                os.system(command)
