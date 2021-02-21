# Classic Brick Breaker Game 

## Requirements :
    - python packages :
        sys
        termios
        tty
        signal
        numpy
    
    Run on Ubuntu :
        sudo apt update
        sudo apt-get python3
        pip install numpy
        cd ./{ Folder containing Game files }
        python3 main.py

    For Mac and Windows : 
        - Shift to Linux 


## Controls :
    - a : move left
    - d : move right
    - k : release ball
    - g : start game
    - q : quit game
 
## Files :
 ### art :
    - Just some Ascii Arts
 
 ### ball :
    - Handles functionality of Ball like collision etc. Uses Inheritence.

 ### bricks : 
    - Used to render Bricks on Screen and also delete them

 ### gametop : 
    - update top values like Score,Time etc. etc.

 ### headerfile :
    - It contains some important attributes or definations used in the Game

 ### inherit_bricks :
    - It just defines different types pf bricks used to render on the screen

 ### items :
    - Contains some important items like instructions etc.

 ### keypressed : 
    - Used to take input from the User

 ### main :
    - Calls the game

 ###  mainrunning :
    - Contains the main game flow

 ### paddle :
    - Handles paddle functionality

 ### powerup :
    - Contains classes and function for Powerup using function overiding method

 ### screen :
    - Screen is created here

## Some concepts Concepts :
 ### Inheritance :
    - Inheritance allows us to define a class that inherits all the methods and properties from another class. Child class is the class that inherits from another class, also called derived class.
    - Implemeted in ball.py

 ### Polymorphism :
    - In Python, Polymorphism lets us define methods in the child class that have the same name as the methods in the parent class. In inheritance, the child class inherits the methods from the parent class.
    - Implemented in powerup.py

 ### Encapsulation :
    - Encapsulation in Python is the process of wrapping up variables and methods into a single entity.In programming, a class is an example that wraps all the variables and methods defined inside it.
    - Whole code is based on it

 ### Abstraction :
    - Abstraction in Python is the process of hiding the real implementation of an application from the user and emphasizing only on usage of it.
    - Done!
