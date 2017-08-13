import webbrowser
import os
import re

# HTML head element information for the movie trailer page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>

    
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link rel="stylesheet" type="text/css" href="http://fonts.googleapis.com/css?family=Open+Sans:400,800">
    <link rel="stylesheet" type="text/css" href="http://fonts.googleapis.com/css?family=Raleway:400">
    <link rel="stylesheet" type="text/css" href="css/main.css">

    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <script type="text/javascript" src="js/main.js"></script>
   
</head>
'''

# Page layout, title bar, and video trailer modal
main_page_content = '''
<body>
<!-- Trailer Video Modal -->
<div class="modal" id="trailer">
    <div class="modal-dialog">
        <div class="modal-content">
            <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24">
            </a>
            <div class="scale-media" id="trailer-video-container"></div>
        </div>
    </div>
</div>


<!-- Main Page Content -->
<div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">My Movie List</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>

<!-- Footer and social -->
<footer>
   <div class="container">
    <div class="row">
        <div class="col-md-6">
                      <ul class="social-icons">
                        <li><a href="#" class="social-icon facebook"></a></li>
                        <li><a href="#" class="social-icon twitter"></a></li>
                        <li><a href="#" class="social-icon dribble"></a></li>
                        <li><a href="#" class="social-icon rss"></a></li>
                        <li><a href="#" class="social-icon forrst"></a></li>
                    </ul>
                     </div>
                <div class="col-md-6 text-right">
                <p>&copy;Copyright 2017 . All rights reserved.</p>
             </div>
            </div>	
	</div>
	</footer>
</body>
</html>
'''

# HTML of individual movies (e.g title, year of release)
movie_tile_content = '''
<div class="col-md-4 col-lg-3 movie-tile text-center">
    <div class="movie-img" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
        <img src="{poster_image_url}">
    </div>
    <h2>{movie_title}</h2>
    <div class="year">{year}</div>
    
    
</div>
'''

def open_movies_page(movies, sort_option="none"):

    print("open_movies_page called!")

    # sort_option for movies array 
    movies = sort_movie_data(movies, sort_option) 

    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Swap placeholder for tiles with the actual dynamically generated content
    rendered_content = main_page_content.format(movie_tiles=
        create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # Open the output file in the browser
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2) # open in a new tab, if possible


def create_movie_tiles_content(movies):

    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_url)
        youtube_id_match = (youtube_id_match or 
            re.search(r'(?<=be/)[^&#]+', movie.trailer_url))
        trailer_youtube_id = (youtube_id_match.group(0) 
            if youtube_id_match else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            year=movie.year,
            poster_image_url=movie.poster_url,
            trailer_youtube_id=trailer_youtube_id)
    return content

# Movies list are sorted in orders
def sort_movie_data(movies, sort_option):
    if sort_option == "none": 
        # list will display without sorting
        return movies
    elif sort_option == "alpha":
        # other wise list of movies will be sorted by alphabetically of title
        movies.sort(key=lambda m: m.title, reverse=False)
        return movies
    elif sort_option == "alpha-reverse":
        # Other option it will sort in reverse alphabetically by title
        movies.sort(key=lambda m: m.title, reverse=True)
        return movies
    elif sort_option == "cron":
        # This option will sort base on cronologically by year
        movies.sort(key=lambda m: m.year, reverse=False)
        return movies
    elif sort_option == "cron-reverse":
        # Sort reverse cronologically by year
        movies.sort(key=lambda m: m.year, reverse=True)
        return movies
    else:
        # Just display with sorted order
        return movies

