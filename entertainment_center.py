import fresh_tomatoes
import media

# Create instance for movie Toy_story
toy_story = media.Movie("Toy Story"," A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)
#print '-' * 30

# Create instance for movie Avatar
avatar = media.Movie("Avatar"," A marine on an alien planet",
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=uZNHIU3uHT4")

#print(avatar.storyline)
#avatar.show_trailer()
#print '-' * 30

# Create instance for movie Fury
fury = media.Movie("Fury"," A story of American platon in 2ed world war",
                        "https://upload.wikimedia.org/wikipedia/en/1/17/Fury_2014_poster.jpg",
                        "https://www.youtube.com/watch?v=-OGvZoIrXpg")

#print(fury.storyline)
#fury.show_trailer()
#print '-' * 30

# Create instance for movie Hunger Games
hunger_games = media.Movie("Hunger Games"," A really real hunger game show",
                        "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                        "https://www.youtube.com/watch?v=4S9a5V9ODuY")

#print(hunger_games.storyline)
#hunger_games.show_trailer()
#print '-' * 30

# Create instance for movie Pretty Woman
pretty_women = media.Movie("Pretty Woman", " A Love story btween rich man and poor woman",
                        "https://upload.wikimedia.org/wikipedia/en/b/b6/Pretty_woman_movie.jpg",
                        "https://www.youtube.com/watch?v=Wzii8IuL8lk")

#print(pretty_women.storyline)
#pretty_women.show_trailer()
#print '-' * 30

# Create instance for movie Ghost Busters
ghost_busters = media.Movie("Ghost Busters", " An action movie about Ghosts hunting",
                        "https://upload.wikimedia.org/wikipedia/en/3/32/Ghostbusters_2016_film_poster.png",
                        "https://www.youtube.com/watch?v=w3ugHP-yZXw")

#print(ghost_busters.storyline)
#ghost_busters.show_trailer()

# make a list of movies instences
movies = [toy_story, avatar, fury, hunger_games, pretty_women, ghost_busters]

# call the method open_movies_page to creates an HTML file which will display all in list movies.
fresh_tomatoes.open_movies_page(movies)
