# Import required modules
import turtle  # For graphics
import time  # For game timing
import random  # For random sentence and word choice
from turtle import *
from turtle import Screen


#variable setup
sentence = ""
screen = Screen()
key = ""
i = 0
time1 = 0
complete = False
start_time = 0
end_time = 0
x = 0
y = 0
delay = 0.1
down = 10
posy = 10
rand = random.randint(-200, 200)
bp1 = False
bp2 = False
bp3 = False
blank = 0
file = 4
score = 0
levelscore = 1000
level = 1
bossmode = False
boss_active = False  # Added a flag for the boss to prevent repeated calls
textdata = ""
wpm = 0
typed_text = ""
bossy = 500
boss = None  # Declare boss
bosstime = None  # Declare boss timer
timescore = 0
timervis = True
cannon_speed = 5
meteor_list = []
lives = 3
game_over = False

#classes for easy turtle setups, meteors, etc

class Sentence:
    #testing setup
    def __init__(self, difficult, punctuation, file):
        if difficult > 0:
            self.difficult = 1
        else:
            self.difficult = 0
        if punctuation > 0:
            self.punctuation = 2
        else:
            self.punctuation = 0
        self.file = self.difficult + self.punctuation + self.punctuation + file  # file is added here as a shortcut for testing ended up being used for the final code for ease of use
        print(self.file)
    
    #gets the sentence/word from the file was
    def read(self):
        global sentence, file
        if bossmode:
            if level <= 4:
                self.file = 0
            elif level <= 8:
                self.file = 1
            elif level <= 14:
                self.file = 2
            elif level <= 20:
                self.file = 3
        else:
            self.file = 4
        if file == 4:
            line_number = random.randint(1, 128)
        else:
            line_number = random.randint(1, 26)
        with open(f"{self.file}.txt", "r") as file:
            lines = file.readlines()
        if line_number <= len(lines):
            print(f"{line_number}: {lines[line_number]}")
            sentence = lines[line_number]
        else:
            print("the file doesn't have that many lines")

class Typing:
    def __init__(self, name, color):
        self.name = name
        self.name = turtle.Turtle()
        self.name.color(color)
        self.name.write(sentence, align="center", font=("Courier", 12, "normal"))

#basic turtle for simple applications
class MyTurtle:
    def __init__(self, name, size, color, posx, posy):
        self.name = turtle.Turtle()
        self.name.hideturtle()
        self.name.speed(0)
        self.name.pensize(size)
        self.name.color(color)
        self.name.penup()
        self.name.goto(posx, posy)


class MyScreen:
    def __init__(self, name, title, color, width, height):
        self.name = name
        self.name = turtle.Screen()
        self.name.title(f"{title}")
        self.name.bgcolor(f"{color}")
        self.name.setup(width, height)
        self.name.tracer(0, 0)

#simple way to create buttons
class Button:
    global x, y

    def __init__(self, name, color, text, posx, posy, width, height):
        self.name = name
        self.color = color
        self.text = text
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.draw()

    def draw(self):
        t4 = MyTurtle("b", 5, self.color, self.posx, self.posy)
        t4.name.begin_fill()
        for s in range(2):
            t4.name.forward(self.width)
            t4.name.left(90)
            t4.name.forward(self.height)
            t4.name.left(90)
        t4.name.end_fill()
        t4.name.goto(self.posx + 5, self.posy + self.height / 2 + 5)
        t4.name.color("black")
        t4.name.write(self.text, font=("Courier", 15, "normal"))

    def is_clicked(self, x, y):
        return self.posx <= x <= self.posx + self.width and self.posy <= y <= self.posy + self.height

#creates meteors
class Meteor:
    global sentence, i

    def __init__(self, posy, text):
        self.turtle = turtle.Turtle()
        self.size = len(sentence) * 7  # Changed multiplier to 7
        self.turtle.speed(0)
        self.turtle.penup()
        self.turtle.hideturtle()  # Hide the turtle cursor
        self.text = text
        self.posx = random.randint(-200, 200)
        self.posy = posy
        self.turtle.goto(self.posx, self.posy)  # Set initial position
        self.draw()

    def draw(self):
        self.turtle.clear()
        self.turtle.begin_fill()
        self.turtle.circle(self.size)
        self.turtle.color("grey")
        self.turtle.end_fill()
        self.turtle.goto(self.posx - self.size + 5, self.posy + self.size - 5)
        self.turtle.color("white")
        # Write each character, coloring the current one green
        for idx, char in enumerate(self.text):
            self.turtle.color("#64d9ed" if idx == i else "white")
            self.turtle.write(char, font=("Courier", 15, "normal"))
            # Move cursor for next character
            self.turtle.forward(15)  # Adjust spacing as needed

    def move(self, file):
        global sentence, i, down, lives
        if self.posy <= -300:
            lives -= 1
            i = 0
            self.posy = 400
            self.posx = random.randint(-200, 200)
            s1 = Sentence(0, 0, file)
            s1.read()
            self.text = sentence.strip()
        self.posy -= down
        self.turtle.goto(self.posx, self.posy)
        self.size = len(sentence) * 7  # Changed multiplier to 7
        self.draw()

    def reset(self, file):
        global sentence, i
        i = 0
        self.posx = random.randint(-200, 200)
        self.posy = 400
        s1 = Sentence(0, 0, file)
        s1.read()
        self.text = sentence.strip()
        self.turtle.goto(self.posx, self.posy)
        self.size = len(sentence) * 7  # Changed multiplier to 7
        self.draw()

#definitions/functions
def on_motion(event):
    global x, y
    x, y = (event.x, event.y)

#mouse tracking
def on_click(x, y):
    global b1, b2, b3, b4, bp1, bp2, bp3  # Added b3, b4 and bp3 to globals
    if bp1 == False and bp2 == False and bp3 == False:
        if b1.is_clicked(x, y):
            background()
            bp1 = True
        elif b2.is_clicked(x, y):
            background()
            bp2 = True
        elif b3.is_clicked(x, y):
            background()
            bp3 = True  # Set bp3 to True when instructions clicked
            b4 = Button("b4", "grey", "Exit", -50, -50, 150, 50)
            t11 = turtle.Turtle()
            t11.hideturtle()
            t11.penup()
            t11.color("white")
            t11.goto(0, 100)
            t11.write("Press basic mode for a game that goes until level 3 or until you run out of lives", align="center",
                      font=("Courier", 12, "normal"))
            t11.goto(0, 50)
            t11.write("Press infinite mode for a game that goes forever or until you run out of lives", align="center",
                      font=("Courier", 12, "normal"))
            t11.goto(0, 0)
            t11.write("To play the game just type out the words or sentences given", align="center",
                      font=("Courier", 12, "normal"))
    elif bp3 == True:
        if b4.is_clicked(x, y):
            background()
            bp3 = False  # Reset bp3 when exiting instructions
            b1 = Button("b1", "grey", "Basic Mode", -50, 100, 125, 50)
            b2 = Button("b2", "grey", "Infinite Mode", -50, 25, 165, 50)  # Fixed ID from b1 to b2
            b3 = Button("b3", "grey", "Instructions", -50, -50, 150, 50)

#all the logic for the typing and more
def letters(letter):
    global i, start_time, elapsed_time, boss_active, bossy, complete, lives, score, levelscore, level, bossmode, sentence, boss_active, file, down, textdata, wpm, typed_text, timescore, timervis
    if not bossmode:
        if i < len(sentence):  # Ensure I is within bounds of sentence length
            if letter == sentence[i] and i != len(sentence):
                typed_text = f"Correct! Typed: '{letter}'"
                i += 1
                if i == 1:  # Start timing on first correct input
                    start_time = time.time()
                if i + 1 == len(sentence):  # Check for completion
                    complete = True
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    if elapsed_time < 10:
                        score += round((10 - elapsed_time) * 10)
                    words = len(sentence.split())
                    wpm = round((int(words / (elapsed_time / 60)) + wpm) / 2) if elapsed_time > 0 else 0
                    textdata = f"Elapsed time: {round(elapsed_time)} seconds | WPM: {wpm}"
                    print(textdata)
                    update_scorelevel()
                    if score >= levelscore:
                        level += 1
                        down *= 1.2
                        levelscore *= 2
                        bossmode = True
                        start_bosstime()
                    start_time = 0
                    end_time = 0
                    i = 0
                    # Instead of reset move the correct meteor
                    shootcannon(m1)
                    m1.reset(file)
            else:
                typed_text = f"Typed: '{letter}' Correct: '{sentence[i]}'"
                print(f"Incorrect! Expected '{sentence[i]}', got '{letter}'")
    else:  # Boss mode typing
        if timescore == 0:
            lives -= 1
            bossmode = False
            boss_active = False  # Reset for next boss level
            start_time = 0
            end_time = 0
            i = 0
            stop_bosstime()
            timervis = False
            update_scorelevel()
            shootcannon(None, False)  # Move cannon to center, no target, don't fire
            boss_hide()  # Move boss back
            file = 4
            m1.reset(file)
            background()  # Redraw background after boss fight
        elif i < len(sentence):  # Ensure I is within bounds of sentence length
            if letter == sentence[i] and i != len(sentence):
                typed_text = f"Correct! Typed: '{letter}'"
                i += 1
                boss_text.clear()
                boss_text.goto(-len(sentence) * 7.5, 0)  # Start position for text
                # Write each character, coloring the current one green
                for idx, char in enumerate(sentence):
                    boss_text.color("#64d9ed" if idx < i else "white")
                    boss_text.write(char, font=("Courier", 16, "normal"))
                    boss_text.forward(15)  # Move cursor for next character
                if i == 1:  # Start timing on first correct input
                    start_time = time.time()
                if i + 1 == len(sentence):  # Check for completion
                    complete = True
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    if elapsed_time < 10:
                        score += round((10 - elapsed_time) * 10)
                    words = len(sentence.split())
                    wpm = round(words / (elapsed_time / 60)) if elapsed_time > 0 else 0
                    textdata = f"Elapsed time: {round(elapsed_time)} seconds | WPM: {wpm}"
                    print(textdata)
                    update_scorelevel()
                    bossmode = False
                    boss_active = False  # Reset for next boss level
                    start_time = 0
                    end_time = 0
                    i = 0
                    stop_bosstime()
                    timervis = False
                    update_scorelevel()
                    shootcannon(None, False)  # Move cannon to center, no target, don't fire
                    boss_hide()  # Move boss back
                    file = 4
                    m1.reset(file)
                    background()  # Redraw background after boss fight
            else:
                typed_text = f"Typed: '{letter}' Correct: '{sentence[i]}'"
                print(f"Incorrect! Expected '{sentence[i]}', got '{letter}'")

#gets keypresses
def keypress():
    for l in (",.;:\"?! abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456798"):
        screen.onkeypress(lambda char=l: letters(char), l)
        screen.onkeypress(lambda: None, "Shift_L")
        screen.onkeypress(lambda: None, "Shift_R")

#background drawing
def background():
    def grid():
        t3 = MyTurtle("bg", 3, "black", -1000, -1000)
        t3.name.clear()
        t3.name.setheading(0)
        t3.name.pendown()
        t3.name.begin_fill()
        for i in range(4):
            t3.name.forward(2000)
            t3.name.left(90)
        t3.name.end_fill()
        t3.name.color("#000a00")
        t3.name.goto(0, -1000)
        t3.name.left(50)
        for i in range(50):
            t3.name.pendown()
            t3.name.forward(2000)
            t3.name.left(90)
            t3.name.forward(20)
            t3.name.left(90)
            t3.name.forward(2000)
            t3.name.right(90)
            t3.name.forward(20)
            t3.name.right(90)
        t3.name.penup()
        t3.name.goto(0, -1000)
        t3.name.setheading(130)
        for i in range(50):
            t3.name.pendown()
            t3.name.forward(2000)
            t3.name.right(90)
            t3.name.forward(20)
            t3.name.right(90)
            t3.name.forward(2000)
            t3.name.left(90)
            t3.name.forward(20)
            t3.name.left(90)

    def planet():
        t6 = MyTurtle("pl", 3, "#ADD8E6", 0, -1900)
        t6.name.begin_fill()
        t6.name.circle(800)
        t6.name.end_fill()
        t6.name.penup()
        t6.name.color("green")
        t6.name.begin_fill()
        t6.name.circle(775)
        t6.name.end_fill()

    grid()
    planet()

#win background
def winscreen():
    global xpos, posx, h, middle_turtle  # Add middle_turtle
    cannon.hideturtle()
    middle_turtle.hideturtle()
    t3 = MyTurtle("bg", 3, "black", -1000, -1000)
    t3.name.clear()
    t3.name.ht()
    t3.name.setheading(0)
    t3.name.pendown()
    t3.name.begin_fill()
    for i in range(4):
        t3.name.forward(2000)
        t3.name.left(90)
    t3.name.end_fill()
    t3.name.color("white")
    t3.name.penup()
    t3.name.goto(0, 0)
    t3.name.left(50)
    t3.name.write("Congratulations! You won!", align="center", font=("Courier", 24, "normal"))
    t3.name.goto(0, -50)
    t3.name.write(f"Your Score: {round(score)}", align="center", font=("Courier", 20, "normal"))
    t3.name.goto(0, -100)
    t3.name.write(f"Final Level: {level}", align="center", font=("Courier", 20, "normal"))

    # Move the cannon to the top of the screen
    cannon.showturtle()  # Show the cannon
    cannon.setheading(90)  # Set the cannon to face upwards
    while cannon.ycor() < 600:  # Move cannon upwards
        cannon.sety(cannon.ycor() + 5)  # Move up at medium speed
        screen.update()
        time.sleep(0.01)  # Adjust speed as needed

    def sun():
        t3.name.goto(-300, 300)
        t3.name.color("#f6ff68")
        t3.name.begin_fill()
        t3.name.circle(100)
        t3.name.end_fill()
        t3.name.goto(-308, 308)
        t3.name.color("#ffa141")
        t3.name.begin_fill()
        t3.name.circle(90)
        t3.name.end_fill()
        t3.name.goto(-316, 316)
        t3.name.color("#ff5a00")
        t3.name.begin_fill()
        t3.name.circle(80)
        t3.name.end_fill()

    def venus():
        t3.name.goto(-50, 200)
        t3.name.color("#f8e2b0")
        t3.name.begin_fill()
        t3.name.circle(80)
        t3.name.end_fill()
        t3.name.goto(-58, 208)
        t3.name.color("#e3bb76")
        t3.name.begin_fill()
        t3.name.circle(70)
        t3.name.end_fill()
        t3.name.goto(-66, 216)
        t3.name.color("#ad8d54")
        t3.name.begin_fill()
        t3.name.circle(60)
        t3.name.end_fill()

    def planet():
        t6 = MyTurtle("pl", 3, "#ADD8E6", 0, -1900)
        t6.name.ht()
        t6.name.begin_fill()
        t6.name.circle(800)
        t6.name.end_fill()
        t6.name.penup()
        t6.name.color("green")
        t6.name.begin_fill()
        t6.name.circle(775)
        t6.name.end_fill()

    def neptune():
        t3.name.goto(340, -200)
        t3.name.color("#274687")
        t3.name.begin_fill()
        t3.name.circle(80)
        t3.name.end_fill()
        t3.name.goto(332, -192)
        t3.name.color("#5b5ddf")
        t3.name.begin_fill()
        t3.name.circle(70)
        t3.name.end_fill()
        t3.name.goto(326, -184)
        t3.name.color("#85addb")
        t3.name.begin_fill()
        t3.name.circle(60)
        t3.name.end_fill()

    sun()
    venus()
    planet()
    neptune()

#lose background
def losescreen():
    global xpos, posx, h, middle_turtle  # Add middle_turtle
    cannon.hideturtle()
    middle_turtle.hideturtle()
    t3 = MyTurtle("bg", 3, "black", -1000, -1000)
    t3.name.clear()
    t3.name.ht()
    t3.name.setheading(0)
    t3.name.pendown()
    t3.name.begin_fill()
    for i in range(4):
        t3.name.forward(2000)
        t3.name.left(90)
    t3.name.end_fill()
    t3.name.color("red")  # Changed to red for the lose screen
    t3.name.penup()
    t3.name.goto(0, 0)
    t3.name.left(50)
    t3.name.write("Game Over!", align="center", font=("Courier", 24, "normal"))  # Updated message
    t3.name.goto(0, -50)
    t3.name.write(f"Your Score: {round(score)}", align="center", font=("Courier", 20, "normal"))
    t3.name.goto(0, -100)
    t3.name.write(f"Final Level: {level}", align="center", font=("Courier", 20, "normal"))

    def sun():
        t3.name.goto(-300, 300)
        t3.name.color("#8B0000")  # Dark red
        t3.name.begin_fill()
        t3.name.circle(100)
        t3.name.end_fill()
        t3.name.goto(-308, 308)
        t3.name.color("#A52A2A")  # Brownish red
        t3.name.begin_fill()
        t3.name.circle(90)
        t3.name.end_fill()
        t3.name.goto(-316, 316)
        t3.name.color("#CD5C5C")  # Indian Red
        t3.name.begin_fill()
        t3.name.circle(80)
        t3.name.end_fill()

    def venus():
        t3.name.goto(-50, 200)
        t3.name.color("#696969")  # Dim Grey
        t3.name.begin_fill()
        t3.name.circle(80)
        t3.name.end_fill()
        t3.name.goto(-58, 208)
        t3.name.color("#808080")  # Grey
        t3.name.begin_fill()
        t3.name.circle(70)
        t3.name.end_fill()
        t3.name.goto(-66, 216)
        t3.name.color("#A9A9A9")  # Dark Grey
        t3.name.begin_fill()
        t3.name.circle(60)
        t3.name.end_fill()

    def planet():
        t6 = MyTurtle("pl", 3, "#800000", 0, -1900)  # Dark Red
        t6.name.ht()
        t6.name.begin_fill()
        t6.name.circle(800)
        t6.name.end_fill()
        t6.name.penup()
        t6.name.color("brown")
        t6.name.begin_fill()
        t6.name.circle(775)
        t6.name.end_fill()

    def neptune():
        t3.name.goto(340, -200)
        t3.name.color("#464646")  # dark grey
        t3.name.begin_fill()
        t3.name.circle(80)
        t3.name.end_fill()
        t3.name.goto(332, -192)
        t3.name.color("#5A5A5A")  # darker grey
        t3.name.begin_fill()
        t3.name.circle(70)
        t3.name.end_fill()
        t3.name.goto(326, -184)
        t3.name.color("#696969")  # dim grey
        t3.name.begin_fill()
        t3.name.circle(60)
        t3.name.end_fill()

    sun()
    venus()
    planet()
    neptune()

#writing data to the screen
def update_scorelevel():
    global score, wpm, typed_text, timescore, timervis, lives, elapsed_time
    
    # Clear existing turtles
    score_t.clear()
    lives_t.clear() 
    data_t.clear()
    wpm_turtle.clear()
    next_level_t.clear()
    timer_t.clear()

    # Update score display
    score_t.goto(-475, 400)  # Position in top left corner
    score_t.write(f"Score: {round(score)}", align="left", font=("Courier", 16, "normal"))
    score_t.goto(-475, 380)
    score_t.write(f"Level: {level}", align="left", font=("Courier", 16, "normal"))

    # Update lives display
    lives_t.goto(380, -400)
    lives_t.write(f"Lives: {lives}", align="left", font=("Courier", 16, "normal"))

    # Update sentence/typing display
    if not bossmode:
        data_t.goto(-475, 318)
        data_t.write(f"{sentence}", align="left", font=("Courier", 16, "normal"))
    data_t.goto(-475, 320)
    data_t.write(f"{typed_text}", align="left", font=("Courier", 16, "normal"))

    # Update WPM display
    wpm_turtle.goto(-475, 360)
    wpm_turtle.write(f"WPM: {round(wpm)}", align="left", font=("Courier", 16, "normal"))

    # Update boss timer display
    if bossmode and timervis:
        timer_t.goto(0, 125)
        timer_t.write(f"Time remaining: {timescore}", align="center", font=("Courier", 24, "normal"))

#suggestion by ms. chan
    # Calculate and display score needed for next level
    if wpm > 0 and bossmode == False:
        score_needed = levelscore - score  # Calculate remaining score needed
        # Estimate words needed based on average score per word at current level
        avg_score_per_word = 100  # Base score per word
        if elapsed_time and elapsed_time < 10:
            avg_score_per_word = round((10 - elapsed_time) * 10)
        words_needed = max(1, int(score_needed / avg_score_per_word)) 
        next_level_t.goto(-475, 295)
        next_level_t.write(f"Words until next level: ~{words_needed}", align="left", font=("Courier", 16, "normal"))


#extra turtle setups for more important functions
lives_t = turtle.Turtle()
lives_t.hideturtle()
lives_t.penup()
lives_t.color("white")

score_t = turtle.Turtle()
score_t.hideturtle()
score_t.penup()
score_t.color("white")

data_t = turtle.Turtle()
data_t.hideturtle()
data_t.penup()
data_t.color("white")

wpm_turtle = turtle.Turtle()
wpm_turtle.hideturtle()
wpm_turtle.penup()
wpm_turtle.color("white")

next_level_t = turtle.Turtle()
next_level_t.hideturtle()
next_level_t.penup()
next_level_t.color("white")

timer_t = turtle.Turtle()
timer_t.hideturtle()
timer_t.penup()
timer_t.color("white")

update_scorelevel()  # Initialize score display

boss_text = turtle.Turtle()
boss_text.hideturtle()
boss_text.color("white")
boss_text.penup()
boss_text.goto(0, 0)  # Set x-axis to center
boss_text.pendown()


def cannon_exit():
    global cannon, bp1, bp2
    while cannon.ycor() > -600:
        cannon.sety(cannon.ycor() - 800)
        screen.update()
        time.sleep(0.001)

    cannon.hideturtle()  # Hide the cannon after it has exited the screen
    if bp1 and level >= 3:
        winscreen()
    elif lives <= 0:
        losescreen()
    else:
        winscreen()


def exitlevel():
    global bp1, level,lives
    if bp1 and level >= 3:
        lives = 0

#code for the bose shaping and sentence type
def Boss():
    global sentence, boss_active, bossy, boss, timescore, timervis
    if not boss_active:  # Check if boss has already been activated
        bossy = 500
        screen.register_shape("Final Boss GIF.gif")
        boss = turtle.Turtle()
        boss.penup()
        boss.shape("Final Boss GIF.gif")
        boss.goto(0, bossy)
        s1.read()
        boss_text.clear()
        # Write the full sentence centered on the screen
        boss_text.goto(0, 0)  # Center the text
        boss_text.color("white")
        boss_text.write(sentence, align="center", font=("Courier", 18, "normal"))  # Write full sentence
        boss_active = True  # Set the boss flag to indicate it has been created
        timescore = int(len(sentence) * 1 / level)
        timervis = True
    if bossy > 300 and boss_active == True:
        bossy -= 10
        boss.clear()
        boss.sety(bossy)


def boss_hide():
    global bossy, boss, boss_active
    while bossy < 600 and boss_active == False:
        bossy += 10
        boss.clear()
        boss.sety(bossy)
        screen.update()
        time.sleep(0.01)
    background()


def start_bosstime():
    global timescore, bosstime
    timescore = int(len(sentence) * 1 / level)
    bosstime = screen.ontimer(update_timer, 1000)  # Set timer for every second
    print("timer has started")


def update_timer():
    global timescore, bosstime, timervis
    if bossmode and timescore > 0:
        timescore -= 1
        update_scorelevel()
        bosstime = screen.ontimer(update_timer, 1000)
    elif not bossmode or timescore == 0:
        stop_bosstime()
        timervis = False
        update_scorelevel()


def stop_bosstime():
    global bosstime
    if bosstime:
        screen.ontimer(bosstime, 0)  # Clears the timer
        bosstime = None
        print("timer has stopped")


cannon = turtle.Turtle()
cannon.hideturtle()
cannon.shape("circle")
cannon.color("red")
cannon.shapesize(2, 2, 2)
cannon.penup()
cannon.goto(0, -350)
cannon.showturtle()

#code to calculate how to move smoothly to the meteor and shoot
def shootcannon(meteor, fire=True):
    global cannon, bossy
    if meteor:
        target_x = meteor.posx
        start_distance = abs(cannon.xcor() - target_x)
        move_amount = start_distance / len(sentence)
        while abs(cannon.xcor() - target_x) > cannon_speed:
            if cannon.xcor() < target_x:
                cannon.setx(cannon.xcor() + cannon_speed)
            else:
                cannon.setx(cannon.xcor() - cannon_speed)
            screen.update()
            time.sleep(0.005)
        if fire:
            lazer(meteor.posx, meteor.posy)
    else:
        while abs(cannon.xcor() - 0) > cannon_speed:
            if cannon.xcor() < 0:
                cannon.setx(cannon.xcor() + cannon_speed)
            else:
                cannon.setx(cannon.xcor() - cannon_speed)
            screen.update()
            time.sleep(0.005)
        if fire:
            lazer(0, -150)  # Fire at a set height


def lazer(meteor_x, meteor_y):
    global cannon, beam
    beam = turtle.Turtle()  # Create line
    beam.hideturtle()
    beam.color("white")
    beam.pensize(3)
    beam.penup()
    beam.goto(cannon.xcor(), cannon.ycor())
    beam.pendown()
    beam.goto(meteor_x, meteor_y)  # Move line to position of meteor
    screen.update()
    time.sleep(0.1)  # give time for beam to render
    beam.clear()  # clear line


# Added code for the new turtle
middle_turtle = turtle.Turtle()
middle_turtle.hideturtle()  # Initially hide the turtle
middle_turtle.penup()
middle_turtle.goto(0, 0)  # Move to the center of the screen
middle_turtle.speed(0)  # Set to fastest speed so you don't see it move


#removed unnceccesary steps to start game will add the instructions in the game instead of console meaning you dont have to interact with console -suggestion no.5

#game setup
print("Game Runs Successfully")
s1 = Sentence(0, 0, 4)
s1.read()
s2 = MyScreen("screen", "window", "white", 1000, 1000)

#got rid of unneccesary setup that created a turtle in the middle of the screen -suggestion no.1

m1 = Meteor(posy, sentence.strip())
background()
word = "example"
b1 = Button("b1", "grey", "Basic Mode", -50, 100, 125, 50)
b2 = Button("b1", "grey", "Infinite Mode", -50, 25, 165, 50)
b3 = Button("b3", "grey", "Instructions", -50, -50, 150,50)
screen.getcanvas().bind("<Motion>", on_motion)
screen.onscreenclick(on_click)
listen()
keypress()

#main gameloop
while lives > 0:
    update_scorelevel()
    if not bossmode:
        file = 4
        if bp1 == True or bp2 == True:
            m1.move(file)
        time.sleep(delay)
        screen.update()
        exitlevel()
    elif bossmode:
        m1.turtle.clear()  # pause the meteors
        Boss()  # moved to the letters function
        time.sleep(delay)
        screen.update()
cannon_exit()  # Call cannon exit before drawing win screen
screen.update()
turtle.done()
# make approx num of words ~ for next level -suggestion no. 3
