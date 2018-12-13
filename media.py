import webbrowser


class Movie():
    """ This class describes movies. It contains attributes of movies and
        methods that can be used to act upon the movies.
        Attributes: Title, Storyline, Poster URL and Trailer URL"""
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """Initiates movie with a title, storyline, poster URL and
           trailer URL"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Shows movie trailer when user clicks on a movie poster"""
        webbrowser.open(self.trailer_youtube_url)
