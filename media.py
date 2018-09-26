import webbrowser


class Movie():
    '''Storing movie data.

       Stores the title and summary of the movie
       and also stores the links to the movie's poster
       image and its trailer.
       It can also open the URl for the movie's trailer.
    '''

    def __init__(self, title, summary, poster, trailer):
        # Store the title of the movie
        self.title = title
        # Store the summary of the movie
        self.summary = summary
        # Store the URL of the poster image
        self.poster = poster
        # Store the URL for the movie's trailer
        self.trailer = trailer

    def play_trailer(self):
        # Open the trailer URL and play it
        webbrowser.open(self.trailer)
