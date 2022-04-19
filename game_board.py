from Marble import Marble
from Point import Point
import turtle
import math

TURN_RIGHT = 90

class MastermindBoard:
    def __init__(self, color="blue", line_thickness=10):
        # creates a new pen
        self.pen = self.new_pen()
        # change the color for the leaderboard outline
        self.color = color
        # change the line thickness to be bolder
        self.line_thickness = line_thickness
        self.window = turtle.Screen()
        # set screen to a default size for every computer it opens on
        self.window.setup(width=1000, height=900)
        # fastest speed
        self.pen.speed(0)
        # hide the turtle to make it go fastest
        self.pen.hideturtle()
        # make each of the different marbles stored inside lists
        self.big_marbles = []
        self.small_marbles = []
        self.colored_marbles = []
        # store all the colored marbles needed for the game
        self.colors = ["red", "blue", "green", "yellow", "purple", "black"]
    
    def get_user(self) -> str:
        
        # title for turtle window
        turtle.title("CS5001 MasterMind Code Game")
        # obtain the users name in order to display them on a leaderboard
        # after they play and if they win
        #user_name = turtle.textinput("CS5001 Mastermind", "Your Name:")
        
        #return user_name
    
    def new_pen(self): 
        """creates a new pen 

        Returns:
            _type_: _description_
        """
        return turtle.Turtle()
    
    def draw_rectangle(self, width: int, height: int):
        
        self.pen.forward(width)
        self.pen.right(TURN_RIGHT)
        self.pen.forward(height)
        self.pen.right(TURN_RIGHT)
        self.pen.forward(width)
        self.pen.right(TURN_RIGHT)
        self.pen.forward(height)
        self.pen.right(TURN_RIGHT)
        
    def make_gameboard(self, width: int, height: int):
        
        # draw the gameboard square
        self.pen.pensize(self.line_thickness)
        self.pen.penup()
        self.pen.goto(-480,430)
        self.pen.pendown()
        self.draw_rectangle(width, height)
            
    def make_leaderboard(self, width: int, height: int):
        
        # draw the leaderboard rectangle
        self.pen.pensize(8)
        self.pen.color(self.color)
        self.pen.penup()
        self.pen.goto(220, 430)
        self.pen.pendown()
        self.draw_rectangle(width, height)
    
    def get_high_scores(self):
        
        self.pen.pensize(8)
        self.pen.color(self.color)
        self.pen.penup()
        self.pen.goto(250, 375)
        self.pen.write("Leaders: ", font=("Calibri", 20, "bold"))
        self.pen.pendown()
        
        #with open('leaderboard', "w", encoding='utf8') as leaderboardfile:
            #leaderboardfile.write()
        
    def make_game_objects(self, width, height):

        # draw the game objects box needed
        self.pen.color("black")
        self.pen.pensize(self.line_thickness)
        self.pen.penup()
        self.pen.goto(-480, -275)
        self.pen.pendown()
        self.draw_rectangle(width, height)
        
    def add_gifs(self, name_of_gif, x, y): 
        
        # showturtle() in order to make it visible to show gifs
        self.pen.showturtle()
        self.window.addshape(name_of_gif)
    
        self.pen.up()
        # go to the coordinates for the gif to be placed
        self.pen.goto(x, y)
        # gets the name of the gif needed to be placed
        self.pen.shape(name_of_gif)
        # leaves the gif at the spot it needs to go
        self.pen.stamp()
        self.pen.down()
        self.pen.shape("blank")
        
    def gifs(self):
        
        self.add_gifs('checkbutton.gif', 50, -340)
        self.add_gifs('quit.gif', 325, -350)
        self.add_gifs('xbutton.gif', 150, -340)
        #self.add_gifs('file_error.gif')
        #self.add_gifs('leaderboard_error.gif')
        #self.add_gifs('Lose.gif')
        #self.add_gifs('quitmsg.gif')
        #self.add_gifs('winner.gif') 
               
    def make_marbles(self):
        """makes the marbles that are intiatlly placed on the gameboard
        and each marble is stored in a list
        """
        current_y = 410
        for y in range(10):
            row = []
            current_x = -450
            current_y  = current_y - 63
            for x in range(4):
                current_x = current_x + 70
                
                marble = Marble(Point(current_x, current_y), "white", size=23)
                marble.draw_empty()
                row.append(marble)
            self.big_marbles.append(row)       
            
        current_y = 390
        for y in range(20):
            row = []
            current_x = -50
            if y != 0 and y % 2 == 0: 
                current_y = current_y - 48
            else:
                current_y = current_y - 15
        
            for x in range(2): 
                current_x = current_x + 20 
                
                marble = Marble(Point(current_x, current_y), "white", size=5) 
                marble.draw_empty()
                row.append(marble)
            self.small_marbles.append(row)
            print(self.small_marbles)
    
    def make_colored_marbles(self):
        """make the colored marbles at the bottom in order for the player 
        to click on in order to start guessing the correct pattern the ai
        has intended
        """
        row = []
        # make the colored marbles in order for the player to start guessing
        color = self.colors
        # current x,y to have the colored marbles placed correctly at the 
        # bottom for the player to click on and guess the pattern
        current_y = -360
        current_x = -480
        # for loop to have each colored filled in the 6 marbles at the bottom
        for colors in color:
            current_x = current_x + 70 
            # puts colored marbles at specific coordinates   
            marble = Marble(Point(current_x, current_y), colors, size=23)
            marble.draw_empty()
            marble.draw() 
            row.append(marble)   
        self.colored_marbles.append(row)
        
#def quit_the_game(x, y):
        
    #if x > 225 and x < 424 and y > -405 and y < -294:
        #exit()

#def confirm_guesses(x, y):
  
    
#def remove_guesses(x, y):
    
     
def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)
     
def main():
    
    # MastermindBoard class to contain everything needed to make the gameboard
    gameboard = MastermindBoard()
    # gets the username/name of the player in order to store in a leaderboard file
    gameboard.get_user()
    # make the mastermind gameboard, the square that gets the marbles inside 
    gameboard.make_gameboard(650, 680)
    # make the leaderboard square that stores highscores
    gameboard.make_leaderboard(230, 680)
    # make the game objects square with the colored marbles to guess with, the
    # check/x button and the quit button
    gameboard.make_game_objects(930, 140)
    # insert the gifs including any picture that is present on the board, the 
    # check/ x button and the quit button
    gameboard.gifs()
    # making the marbles for when the player has the guess the code
    gameboard.make_marbles()
    # making the colored marbles that the player starts with in order to guess
    # the correct code the ai wants
    gameboard.make_colored_marbles()
    # make a file in order to store high scores for furture players to see
    gameboard.get_high_scores()
    # allows the player to use the quit button in order to quit the game
    #turtle.onscreenclick(quit_the_game)
    # allows the player to confirm that a guess should be checked/entered
    #turtle.onscreenclick(confirm_guesses)
    # allows the player to remove a guess that has not yet been checked/entered
    # also resets the clickable, colored guess buttons
    #turtle.onscreenclick(remove_guesses)
    # keeps the game running until the players clicks the quit button
    turtle.mainloop()

if __name__ == "__main__":
    main()
