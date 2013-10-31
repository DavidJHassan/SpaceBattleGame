SpaceBattleGame
===============

A simple homework assignment using python and pygame

Homework Criteria:

Part 1:

1. Using Pygame
2. Implementing two Python modules that are game sprites
3. Loading images with exception handling
4. Using an event queue to handle keyboard events
Overview

Instructions
You will implement two sprites for the game as Python / Pygame modules: the battlecruiser (Battlecruiser.py) and the laser (Laser.py).
Download the assets (images) for the game: assets.zip. You will be using this set of assets for the next lab as well.
Specifications and Controls
Both the Battlecruiser and Laser Python classes shall be subclasses of pygame.sprite.Sprite
The Battlecruiser sprite shall use the asset battlecruiser.gif
The Laser sprite shall use the asset laser.gif
Both sprite classes shall load the asset with exception handling
Both sprite classes shall have a class constructor
Both sprite classes shall have and maintain the following member variables:
1. x
2. y
3. dx
4. dy
5. screen (a copy of the drawing surface)
6. image
7. image_w (image width)
8. image_h (image height)
9. rect (a "moving collision box")
10. active (a boolean)
Both sprite classes shall have a method named update
Both sprite classes shall have a method named draw

Both sprite classes shall run using 50 frames-per-second
The controls for the battlecruiser:
LEFT ARROW: Moves the battlecruiser to the left of the screen (in the x-direction)
RIGHT ARROW: Moves the battlecruiser to the right of the screen (in the x-direction)
UP ARROW: Moves the battlecruiser up the screen (in the y-direction)
DOWN ARROW: Moves the battlecruiser down the screen (in the y-direction)
SPACE BAR: Fires a laser. 
Important: the battlecruiser can fire multiple lasers. That is, more than one laser can be drawn on one frame!
ESC: Quit

Running the laser module via python Laser.py shall launch a 800x600 window with a black background, with a barrage of lasers randomly going from down the screen to up.
Running the battlecruiser module via python Battlecruiser.py shall launch a 800x600 window with a black background, allowing you to control the battlecruiser with the controls as noted above.


Part 2:

Add
1. Sound playing
2. Animation
3. Collision detection

You will implement one additional sprite for the game as a Python / Pygame module: the enemy (Enemy.py). You will also implement a game file: game.pythat will use the battlecruiser and laser sprites from Lab 1. This game file shall contain the game loop, event handling, collision detection, and rendering of score.
Again, you will use the assets (images) for the game: assets.zip. 

The Enemy Python class shall:
1. Be subclasses of pygame.sprite.Sprite
2. Load the asset with exception handling
3. Have a class constructor
4. Have and maintain the following member variables:
1. x
2. y
3. dx
4. dy
5. screen (a copy of the drawing surface)
6. image
7. image_w (image width)
8. image_h (image height)
9. rect (a "moving collision box")
10. active (a boolean)
11. thePlayer (a copy of the battlecruiser object)
5. Have a method named update
6. Hethod named draw
7. Use the asset mutalisk.gif if it is alive
8. Use the asset (change image to) laser_explosion.gif if it is hit by a laser, and then the sprite shall no longer be displayed, inactivated.
Running the enemy module via python Enemy.py shall launch a 800x600 window with a white background, with ten (10) enemies bouncing off the walls, elastic collision.
If a laser is fired, the sound asset laser.wav shall be played.
If the battlecruiser collides with an enemy, the game is over and the sound asset death_explode.wav is played.
If a laser collides with an enemy on the screen, 100 points is awarded.
The game score shall be rendered near the upper-left corner of the screen with a font color that is not black!
The dimensions of the window in game.py shall be 800x600.
If the game is over, please give feedback to the player that the game is over (e.g., via "Game Over" message or go to a different screen)


To Play the Game
python game.py

