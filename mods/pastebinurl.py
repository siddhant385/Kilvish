class IPORT:
    content = ''
    def __init__(self,searchurl):
        self.searchurl = searchurl
        self.getip()

    def getip(self):
        response = urllib.request.urlopen(self.searchurl).read()
        self.content = response.decode('utf-8')
        return self.content

    def ip(self):
        ip = self.content.split(":")
        return ip[0]
    
    def port(self):
        strport = self.content.split(":")
        port = int(strport[1])
        return port
