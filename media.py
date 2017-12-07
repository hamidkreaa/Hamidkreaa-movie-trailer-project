import webbrowser


class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """ the Class Movie is Model for the Movie objects """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
    """ this method opens
        trailer for the movie using trailer_youtube_url """
    webbrowser.open(self.trailer_youtube_url)
