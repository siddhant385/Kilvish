# class SCREENSHOT:

#     SC_DATA = b""

#     def __init__(self):
#         self.generate()

#     def generate(self):
#         obj = io.BytesIO()
#         im  = pyscreenshot.grab()
#         im.save(obj, format="PNG")
#         self.SC_DATA = obj.getvalue()

#     def get_data(self):
#         return self.SC_DATA

class SCREENSHOT:

    def __init__(self):
        self.SC_DATA = b""
        self.generate()
        

    def Screenshot(self,File):
        with mss() as sct:
            sct.shot(output=File)

    def generate(self):
        self.Screenshot("screen.jpg")
        f = open("screen.jpg",'rb')
        data = f.read()
        f.close()
        self.SC_DATA = data
        os.remove("screen.jpg")

    def get_data(self):
        return self.SC_DATA