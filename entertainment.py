import fresh_tomatoes
import media

iron_man_01=media.Movie("Iron Man",
                        "After being held captive in an Afghan cave, billionaire engineer Tony Stark creates a unique weaponized suit of armor to fight evil.",
                        "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",
                        "https://www.youtube.com/watch?v=8ugaeA-nMTc")

#print(iron_man_01.storyline)

incredible_hulk=media.Movie("The Incredible Hulk",
                            "Bruce Banner, a scientist on the run from the U.S. Government, must find a cure for the monster he turns into, whenever he loses his temper.",
                            "https://upload.wikimedia.org/wikipedia/en/8/88/The_Incredible_Hulk_poster.jpg",
                            "https://www.youtube.com/watch?v=xbqNb2PFKKA")
#print(incredible_hulk.storyline)
#incredible_hulk.show_trailer()

iron_man_02=media.Movie("Iron Man 2",
                        "With the world now aware of his identity as Iron Man, Tony Stark must contend with both his declining health and a vengeful mad man with ties to his father's legacy.",
                        "https://upload.wikimedia.org/wikipedia/en/e/ed/Iron_Man_2_poster.jpg",
                        "https://www.youtube.com/watch?v=BoohRoVA9WQ")

thor=media.Movie("Thor",
                 "The powerful but arrogant god Thor is cast out of Asgard to live amongst humans in Midgard (Earth), where he soon becomes one of their finest defenders.",
                 "https://upload.wikimedia.org/wikipedia/en/f/fc/Thor_poster.jpg",
                 "https://www.youtube.com/watch?v=JOddp-nlNvQ")

the_first_avenger=media.Movie("The First Avenger",
                              "Steve Rogers, a rejected military soldier transforms into Captain America after taking a dose of a Super-Soldier serum",
                              "https://upload.wikimedia.org/wikipedia/en/3/37/Captain_America_The_First_Avenger_poster.jpg",
                              "https://www.youtube.com/watch?v=JerVrbLldXw")

the_avenger=media.Movie("The Avenger",
                        "Earth's mightiest heroes must come together and learn to fight as a team if they are going to stop the mischievous Loki and his alien army from enslaving humanity.",
                        "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                        "https://www.youtube.com/watch?v=eOrNdBpGMv8")

iron_man_03=media.Movie("Iron Man 3",
                        "When Tony Stark's world is torn apart by a formidable terrorist called the Mandarin, he starts an odyssey of rebuilding and retribution.",
                        "https://upload.wikimedia.org/wikipedia/en/d/d5/Iron_Man_3_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=YLorLVa95Xo")

thor_dark_world=media.Movie("Thor The Dark World",
                            "When Dr. Jane Foster (Natalie Portman) gets cursed with a powerful entity known as the Aether, Thor is heralded of the cosmic event known as the Convergence and the genocidal Dark Elves.",
                            "https://upload.wikimedia.org/wikipedia/en/7/7e/Thor_-_The_Dark_World_poster.jpg",
                            "https://www.youtube.com/watch?v=npvJ9FTgZbM")

winter_soldier=media.Movie("The Winter Soldier",
                           "As Steve Rogers struggles to embrace his role in the modern world, he teams up with a fellow Avenger and S.H.I.E.L.D agent, Black Widow, to battle a new threat from history: an assassin known as the Winter Soldier.",
                           "https://upload.wikimedia.org/wikipedia/en/e/e8/Captain_America_The_Winter_Soldier.jpg",
                           "https://www.youtube.com/watch?v=7SlILk2WMTI")

end_game=media.Movie("Avengers: Endgame",
                           "After Thanos, an intergalactic warlord, disintegrates half of the universe, the Avengers must reunite and assemble again to reinvigorate their trounced allies and restore balance.",
                           "https://thumbor.forbes.com/thumbor/960x0/https%3A%2F%2Fblogs-images.forbes.com%2Fscottmendelson%2Ffiles%2F2019%2F03%2FPayoff_1-Sht_Online_v6_Domestic_Lg-1200x675.jpg",
                           "https://www.youtube.com/watch?v=TcMBFSGVi1c")

movies=[iron_man_01,incredible_hulk,iron_man_02,thor,the_first_avenger,the_avenger,iron_man_03,thor_dark_world,winter_soldier,end_game]
fresh_tomatoes.open_movies_page(movies)
