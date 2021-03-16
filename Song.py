class Song(object):
    
    def __init__(self, title, singers, duration):
        self.title = title
        self.singers = singers
        self.duration = duration

    def hassinger(self, name):
        return name in self.singers



