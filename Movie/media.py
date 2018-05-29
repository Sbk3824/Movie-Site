import webbrowser
class Movie():
    
    def __init__(self, title, storyline, img_url, youtube_url):
        self.title = title
        self.storyline = storyline
        self.img_url = img_url
        self.youtube_url = youtube_url
        
    def show_trailer(self):
        webbrowser.open(self.youtube_url)