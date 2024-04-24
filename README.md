# bpollock_finalgame
Final Game for CS120
https://docs.google.com/document/d/1G3yKUlE9WGFbf7xW-r-iloruyB29-3UagSKseGBTzJg/edit?usp=sharing (<--- Best way to view documentation because of images in the document)
Instructions: Stay in the red box next to the ghost to slay it! Use WASD to move. Certain scores will give you certain responses from the game.

CREDITS:
Background: https://opengameart.org/content/castle-in-the-dark
Knight: https://www.seekpng.com/ima/u2e6e6q8t4w7q8o0/ 
Ghost: https://opengameart.org/content/stendhal-ghost 
Music: https://pixabay.com/users/syouki_takahashi-3820204/ 
Hit sound: 
https://www.fesliyanstudios.com/royalty-free-sound-effects-download/kick-and-punch-74 
External resource used:
http://programarcadegames.com/python_examples/f.php?file=background_music.py







Game States: 
intro -> gamePlay (or shop)  -> pause -> gamePlay or Quit
Intro
Show title
Hide everything else
gamePlay
Title hidden
btnStart hidden
btnQuit hidden
All sprites shown
Points/Stopwatch reset
Pause
Title hidden
Sprites hidden
btnQuit shown
Quit
Game ends
Sprites:
Knight
User-controlled
Can move up down left and right
Game ends when hit by bullet
Can dodge
Wraps screen
Ghost
NPC
Moves left and right (up and down)
Shoots bullets
Wraps screen
Only 1 ghost
UI Components:
Background
Castle
Should be an abstract enough palette to see the bullets
Title 
Starts gameplay when clicked
Instructions screen multilabel
Shop Button
Hides sprites
Labels to click for certain upgrades
btnQuit 
Appears in pause
When clicked, exits entire game
Sound Effects:
Bullet sound
Dodge sound
Hit sound
Ambient music
Milestones
Gather placeholders
Music, hit effect, sprites for ghost and knight
Basic classes
Add knight class
Add ghost class
Check bullet-knight collision
Check ghost-knight collision
Add stopwatch (timer)
Add quit button
Add intro
Add scorekeeping
Add shop interface 
Add powerups
Add dodging
Game tuning parameters:
Speed of knight
Speed of bullet
Speed of dodge
Amount of bullets
Powerup specifics
Stretch Goals:
Bullets that don’t kill but hinder the player. Slower speed, no dodging, input reversal.
Different sprites based on what powerups
Multiple levels

The Learning Process:
I learned a lot about the process of writing code in computer science. I checked a lot, and I mean a LOT of online resources and realized that coding is not a one-size-fits all solution. Different people write their code in different ways, and I realized that a lot of the time the code I saw on stackoverflow, or youtube was just incompatible with my level of understanding. 
I got stuck making a shop interface and getting bullets to separate from the ghost. I used this to my advantage and repurposed my game to be melee-based by standing close to the ghost to increase points. It was specifically difficult for me to get the bullet to fire without the press of a button, while ALSO having multiple bullets exist on screen at any given time. 
The thing I would like to improve is adding everything I originally aimed for. This means a shop, multiple bullets, player upgrades and player hindrances. 
As far as things I’d do differently? I’d attend class more frequently. I burnt out really hard near the end of this semester and it led to me not getting as much help as I needed. Entirely my fault but a lesson to learn from for sure. I would also stretch out how often I work on assignments, instead of doing it all in 1-2 days, do little bits over the course of the week, etc. 
I strayed quite a bit from my game design document. There were small things that I couldn’t figure out how to get to work, like when my pygame would just crash without any error message when I was early in development. I didn’t get the shop done, I didn’t get hindrances, and I didn’t get dodging. Other than that I got most of what I wanted.
I stayed on task by just sitting down and finally committing to my project. I needed to get it done, and so I closed everything that was distracting me, opened stackoverflow, the class canvas page, specifically the simpleGE page, and the pygame website. Took me a lot longer than I’d like to admit but I have a game, even if it isn’t highly engaging. 


Things I succeeded on: I made the timer, I had a boss/enemy that has an object follow it (in the code it’s a bullet).
I had sprites for both the ghost and the player, the dungeon background, I implemented music and hit sounds. 
This is what my documentation was originally. I will underline features I could not get to work. 


Define classes for sprites
Knight class:
Allow user input with self.isKeyPressed
Ghost class:
Define a function for random speed movements
setBoundAction(self.BOUNCE) to have bounce instead of screen wrapping 
Bullet process(self)
	self.bullet.fire()
Implementing Scorekeeping
	Define score label class using simpleGE.Label
Define a process that checks collisions
		If collision: Add +1
Implementing Timers:
	Define Time class (simpleGE.Label):
	Self.text = ‘Time left:”
	Under same process as scorekeeping,
	If timer < 0:
	Stop
Implementing Instructions
	simpleGE.Label
	Set prevscore = prevscore for score keeping label
	Self.response = Quit
	Direction text lines = ((f””put directions here))
Set up button for play & quit using simpleGE.Button
If play button pressed:
	Play
If quit button pressed:
	Quit
Def main()

