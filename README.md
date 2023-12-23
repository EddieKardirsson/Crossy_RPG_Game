# Crossy_RPG_Game

this project is based on the following online course on Zenva by Nimish Narang:
https://academy.zenva.com/course/learn-python-and-pygame-by-making-a-game/

I did follow along and also improved the code in many ways so that the game can have multiple resolutions.
I myself use a desktop resolution of 4K (2160p) and prefer to run the game in the 2K (1440p) resolution (which is windowed)
Since most people (especially on laptops) uses 1080p in many cases, I put the default resolution at 720p.

If you want to use a different resolution when running the code, go to main.py and line 11:
  
  game = Game(resolution_720p)

change the parameter value to the corresponding resolution tuple variables.

For example: if you use 1080p desktop resolution and set the game resolution to "resolution_1080p" the game will be like windowed-fullscreen.
