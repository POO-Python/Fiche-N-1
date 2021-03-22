class Song(object):
    
    def __init__(self, title, singers, duration):
        self.title = title
        self.singers = singers
        self.duration = duration

    def hassinger(self, name):
        return name in self.singers

    def __str__(self):
        result =  self.title + ' par ' + self.singers[0]
        for i in range(1, len(self.singers)):
            result += ', ' + self.singers[i]
        return result

