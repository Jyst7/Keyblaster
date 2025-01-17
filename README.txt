Introduction

This Python code implements a typing game using the Turtle graphics library. The game presents the user with sentences to type and includes a score system, level progression, a boss mode, and win/lose conditions. There are two game modes, "Basic Mode" and "Infinite Mode".

How to Run

- If you have Pycharm
    1.  Make sure you have Python installed on your system.
    2.  Make sure to have the main file "KeyBlaster.py"
    3.  Make sure text files named "0.txt", "1.txt", "2.txt", "3.txt", and "4.txt" are in the same directory as your Python script. These files should contain the sentences for the game.
    4.  Make Sure the "Final Boss GIF.gif" file is in the same folder
    5.  Run the code(KeyBlaster.py)

Game Mechanics

-   Game Modes: The game starts with three buttons:
    -   "Basic Mode" - The game ends when level 3 is reached.
    -   "Infinite Mode" - The game continues until the user runs out of lives (3).
    -   "Instructions" - Provides instructions on how to play the game
-   Typing: Users type the displayed words and sentences. Correctly typed characters will advance the cursor and incorrect letters will show what letter was inputted, and what was expected.
-   Scoring: A score is based on time taken to complete a sentence. Faster times get higher scores. There is also a words per minute (WPM) counter.
-   Leveling: As the score increases, the game level will increase. With each level increase the meteors will fall faster. Once a score goal has been reached the player will enter boss mode.
-   Boss Mode: When a player reaches a level milestone, boss mode will start. During boss mode a timer starts that is equal to the length of the sentence to be typed divided by the current level, and decreases each second. The player must complete the sentence before the timer reaches zero or they will lose one life and exit boss mode. Once the boss sentence is complete the player is moved back to the normal mode.
-   Meteors: Sentences are displayed on the meteors which will move down the screen. Failing to complete a sentence will result in the player losing a life.
-   Cannon: A cannon appears at the bottom of the screen and moves to fire a lazer to destroy the meteors when the sentence is correctly typed.
-   Win Condition:
    -   In "Basic Mode," reaching level 3 will win the game.
    -   In "Infinite Mode," the game continues until the user runs out of lives.
-   Lose Condition:
    -   Running out of lives will trigger a lose screen.
    -   Reaching level 3 in Infinite Mode will trigger a win screen.

Classes

-   Sentence: Handles the loading and selection of sentences from text files. It determines the correct text file based on the level and boss mode.
-   Typing: finds the sentence to be typed on the screen.
-   MyTurtle: Creates turtles with pre-defined properties for basic graphics.
-   MyScreen: Creates the screen for the game.
-   Button: Creates buttons that are clickable.
-   Meteor: Creates and manages the meteors that hold the sentences and moves down the screen.

Functions

-   on_motion(event): Tracks the mouse cursor position.
-   on_click(x, y): Handles button click events and starts the game.
-   letters(letter): Processes user input when typing.
-   keypress(): Registers key presses to the letters function.
-   background(): Draws the background of the game.
-   winscreen(): Displays the win screen.
-   losescreen(): Displays the lose screen.
-   update_scorelevel(): Updates score, level, WPM, and other on-screen information.
-   cannon_exit(): Handles the end-game sequence for the cannon.
-   Boss(): Creates and moves the boss in boss mode.
-   boss_hide(): Hides the boss once boss mode has been exited.
-   start_bosstime(): Starts the boss mode timer.
-   update_timer(): Updates the boss mode timer.
-   stop_bosstime(): Stops the boss mode timer.
-   shootcannon(meteor, fire=True): Moves the cannon to fire at the meteor.
-   lazer(meteor_x, meteor_y): Draws a lazer from the cannon to the meteor

Additional Notes

-   The game uses a GIF image for the final boss; make sure "Final Boss GIF.gif" is in the correct location, or the game will fail during boss mode.
-   The text files ("0.txt", "1.txt", "2.txt", "3.txt", and "4.txt") are necessary for the game to load the sentences correctly.
-   The levels in boss mode depend on the game level, which increases with your score.
-   Make sure you have turtle and time libraries installed.
-   The game speed is set using the delay variable, which is currently set to 0.1.
-   The text file names are determined by the level and boss mode to determine the difficulty of the sentences

Author

Jayson Sone and Dhillan Aggarwal