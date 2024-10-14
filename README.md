Spaceship Battle Game

A simple 2D spaceship battle game built using Pygame, where two players control spaceships on opposite sides of the screen, shoot bullets at each other, and try to deplete the other player's health.

Features

Two-player Local Gameplay: Players control red and yellow spaceships.
Shooting Mechanism: Players can fire bullets, and each hit reduces the opponent’s health.
Health System: Each player starts with 10 health points, and the game ends when a player’s health reaches zero.
Victory Screen: Displays the winner and ends the game after a short delay.
Real-time Movement: Players can move up, down, left, and right within their play areas.
Controls

Red Spaceship (Right side):
Move: Arrow Keys (Up, Down, Left, Right)
Shoot: Slash (/)
Yellow Spaceship (Left side):
Move: WASD Keys (W, A, S, D)
Shoot: Q
Prerequisites

Python 3.x
Pygame: Install the Pygame library using pip:
bash
Copy code
pip install pygame
Installation

Clone this repository or download the project files.
Ensure you have Python 3.x and Pygame installed.
Place the required assets (spaceships, background images, sound effects) in the Assets folder.
Run the game:
bash
Copy code
python spaceship_battle.py
Assets

Ensure the following assets are placed in an Assets folder:

spaceship_yellow.png: Image of the yellow spaceship.
spaceship_red.png: Image of the red spaceship.
space.png: Background space image.
(Optional) Grenade+1.mp3: Sound effect for a bullet hit.
(Optional) Gun+Silencer+1.mp3: Sound effect for firing bullets.
How to Play

The game starts with two spaceships, one yellow and one red, positioned on opposite sides of the screen.
Players use their assigned controls to move their spaceship and shoot bullets at their opponent.
Each player starts with 10 health points, and every successful bullet hit reduces the opponent’s health by 1.
The first player to reduce the opponent’s health to 0 wins, and a victory message is displayed.
Game Flow

Movement: Move your spaceship around your half of the screen using the respective keys.
Shooting: Fire bullets to hit the opponent’s spaceship. Watch out for incoming bullets from the other player.
Winning: The game ends when one player’s health reaches zero. The winning player is displayed on the screen.
Customization

Spaceship Speed: Modify the variable VEL to adjust the speed of the spaceships.
Bullet Speed: Adjust the BULLET_VEL variable for faster or slower bullets.
Health: Change the red_health and yellow_health starting values for a longer or shorter game.
Max Bullets: Modify MAX_BULLETS to change the number of bullets a player can shoot at once.
File Structure

python
Copy code
├── Assets/
│   ├── spaceship_yellow.png   # Yellow spaceship image
│   ├── spaceship_red.png      # Red spaceship image
│   ├── space.png              # Background image
│   └── (Optional sound files for bullet hit and firing)
├── spaceship_battle.py        # Main game script
└── README.md                  # Project documentation
