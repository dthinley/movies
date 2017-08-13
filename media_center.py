import media
import fresh_tomatoes

# Create instances of the Movie class to hold information of my favourite movies
point_break = media.Movie("Point Break",
                        "1991 [R]",
                        "Point Break is a 1991 American action crime thriller film directed by Kathryn Bigelow, starring Patrick Swayze, Keanu Reeves, Lori Petty and Gary Busey.",
                        "http://t2.gstatic.com/images?q=tbn:ANd9GcSg5eJ7B6CSA31lD7Fu9RSCbFtyqBm4JezITWtb61sVpbzkwcKq",
                        "https://www.youtube.com/watch?v=-oawCc2iNLI")

bad_boys_II = media.Movie("Bad Boys II",
                        "2003 [R]",
                        "Two loose-cannon narcotics cops investigate the flow of Ecstasy into Florida from a Cuban drug cartel.",
                        "http://www.gstatic.com/tv/thumb/movieposters/31357/p31357_p_v8_ab.jpg",
                        "https://www.youtube.com/watch?v=g6vcdR30W1A")

alien_vs_predator = media.Movie("Alien VS Predator",
                        "2004  [PG-13]",
                        "Alien vs. Predator (also abbreviated as AVP) is a 2004 science fiction action horror film",
                        "http://www.gstatic.com/tv/thumb/movieposters/34715/p34715_p_v8_aa.jpg",
                        "https://www.youtube.com/watch?v=ukKN1KnOLIQ")

the_experiment = media.Movie("The Experiment",
                        "2010   [R]",
                        "26 men are chosen to participate in the roles of guards and prisoners in a psychological camp.",
                        "http://movieboozer.com/wp-content/uploads/2011/05/The_Experiment_2010_1.jpg",
                        "https://www.youtube.com/watch?v=oi22xiNAfD0")

virus = media.Movie("Virus",
                        "1999   [R]",
                        "Virus is a 1999 American science fiction horror film ",
                        "http://www.gstatic.com/tv/thumb/movieposters/22392/p22392_p_v8_ab.jpg",
                        "https://www.youtube.com/watch?v=yyqlHGc1WzA")


random_hearts = media.Movie("Random Hearts",
                        "1999   [R]",
                        "Random Hearts is a compelling love story about two people who never would have met... in a perfect world.  ",
                        "http://www.gstatic.com/tv/thumb/movieposters/23873/p23873_p_v8_aa.jpg",
                        "https://www.youtube.com/watch?v=I7O_VVmGABU")

The_6th_Day = media.Movie("The 6th Day",
                        "2000 [R]",
                        "Futuristic action about a man who meets a clone of himself and stumbles into a grand conspiracy about clones taking over the world.  ",
                        "http://www.gstatic.com/tv/thumb/movieposters/26574/p26574_p_v8_ap.jpg",
                        "https://www.youtube.com/watch?v=f4uDW79vMsg")

groundhog_day = media.Movie("Groundhog Day",
                        "1993 [PG]",
                        "Weatherman finds himself inexplicably living the same day over and over again. ",
                        "http://www.gstatic.com/tv/thumb/movieposters/14569/p14569_p_v8_ah.jpg",
                        "https://www.youtube.com/watch?v=2vmmTnDJnH0")

hollow_man = media.Movie("Hollow Man",
                        "2000  [R]",
                        "Hollow Man is a 2000 American-German science fiction horror film ",
                        "http://www.gstatic.com/tv/thumb/movieposters/25993/p25993_p_v8_aj.jpg",
                        "https://www.youtube.com/watch?v=2mc_eK3iu88")




# Add the instances to a list
movies = [
    point_break,
    bad_boys_II,
    alien_vs_predator,
    the_experiment,
    virus,
    random_hearts,
    The_6th_Day,
    groundhog_day,
    hollow_man,
    
]

# Generate a web page that displays the movies in the list by sorted option chronological order
fresh_tomatoes.open_movies_page(movies,"cron")
