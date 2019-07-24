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

iron_man_02=media.Movie("IRON MAN 2",
                        "With the world now aware of his identity as Iron Man, Tony Stark must contend with both his declining health and a vengeful mad man with ties to his father's legacy.",
                        "https://upload.wikimedia.org/wikipedia/en/e/ed/Iron_Man_2_poster.jpg",
                        "https://www.youtube.com/watch?v=BoohRoVA9WQ")

thor=media.Movie("THOR ",
                 "The powerful but arrogant god Thor is cast out of Asgard to live amongst humans in Midgard (Earth), where he soon becomes one of their finest defenders.",
                 "https://upload.wikimedia.org/wikipedia/en/f/fc/Thor_poster.jpg",
                 "https://www.youtube.com/watch?v=JOddp-nlNvQ")

the_first_avenger=media.Movie("THE FIRST AVENGER",
                              "Steve Rogers, a rejected military soldier transforms into Captain America after taking a dose of a Super-Soldier serum",
                              "https://upload.wikimedia.org/wikipedia/en/3/37/Captain_America_The_First_Avenger_poster.jpg",
                              "https://www.youtube.com/watch?v=JerVrbLldXw")

the_avenger=media.Movie("The Avenger",
                        "Earth's mightiest heroes must come together and learn to fight as a team if they are going to stop the mischievous Loki and his alien army from enslaving humanity.",
                        "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                        "https://www.youtube.com/watch?v=eOrNdBpGMv8")


movies=[iron_man_01,incredible_hulk,iron_man_02,thor,the_first_avenger,the_avenger]
fresh_tomatoes.open_movies_page(movies)
