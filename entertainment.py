import fresh_tomatoes
import media

iron_man_01=media.Movie("IRON MAN",
                        "After being held captive in an Afghan cave, billionaire engineer Tony Stark creates a unique weaponized suit of armor to fight evil.",
                        "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",
                        "https://www.youtube.com/watch?v=8ugaeA-nMTc")

#print(iron_man_01.storyline)

incredible_hulk=media.Movie("THE INCREDIBLE HULK",
                            "Bruce Banner, a scientist on the run from the U.S. Government, must find a cure for the monster he turns into, whenever he loses his temper.",
                            "https://upload.wikimedia.org/wikipedia/en/8/88/The_Incredible_Hulk_poster.jpg",
                            "https://www.youtube.com/watch?v=xbqNb2PFKKA")
#print(incredible_hulk.storyline)
#incredible_hulk.show_trailer()

movies=[iron_man_01,incredible_hulk]
fresh_tomatoes.open_movies_page(movies)
