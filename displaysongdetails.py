"""
    Class to describe how songs are displayed in the webapp
"""

class DisplaySong():

    def __init__(self, name, id):
        self.name = name 
        self.id = id 
        self.iframe = self.getIFrameLink()
    
    def setIFrameLink(self):
        return format('<iframe src="https://open.spotify.com/embed/track/{self.id}}" width="300" height="80" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>')

    def getIFrameLink(self):
        return self.iframe

    