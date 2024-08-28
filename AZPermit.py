# Import Libraries
from tkinter import *
from random import randint

# Global Variable
qCount = 0  # Int
usedQuestions = []  # List
actualAnswer = 0  # Integer
usersAnswer = 0  # Integer
points = 0  # Integer

def readFile():
    #  Read Text File With Questions

    data = [] # 2D Array
    file = open("q.txt",mode="r")

    # Loop each line in the file and appends the list
    for line in file:
        data.append(line.strip().split(','))

    return data

def displayQuestion():
    # Display Random Question
    data = readFile()  # Calls Read File & Stores Questions

    # Imports Variable and Adds to It
    global qCount, usedQuestions, actualAnswer, btnRestart, gameOver

    randomQ = randint(0,len(data)-1) # Generate Random Question Number As Int
    currentQuestion = str(data[randomQ][0])  # Current Question Number As String

    while currentQuestion in usedQuestions and len(usedQuestions) < len(data):
        randomQ = randint(0, len(data) - 1)
        currentQuestion = str(data[randomQ][0])

    if qCount < len(data):
        # Displays Question and Answers
        resetBtns()  # Calls Procedures to Reset Buttons
        qNum.config(text="Question: {0}".format(qCount+1))
        question.config(text=data[randomQ][1])
        btnA.config(text=data[randomQ][2],font=("Verdana",15))
        btnB.config(text=data[randomQ][3],font=("Verdana",15))
        btnC.config(text=data[randomQ][4],font=("Verdana",15))
        btnD.config(text=data[randomQ][5],font=("Verdana",15))

        qCount += 1  # Increments Question Count
        usedQuestions.append(currentQuestion)
        actualAnswer = data[randomQ][6]
    else:
        gameOver.config(text="Quiz completed!\n\nYour Score Is: %s/30" %points)
        gameOver.place(relwidth = 1,relheight = 1)
        btnRestart.place(relx=0.45,
                         rely=0.8,
                         relwidth = 0.1,
                         relheight = 0.1)

def checkAnswer():
    # Will Check the Answer and Increment Points of Score
    global points
    if int(actualAnswer) == usersAnswer:
        points +=1  # Increments Points By 1
        score.config(text="Score: %s" %points)
    resetBtns()
    displayQuestion()

def resetGame():
    # Resets The Game Variables and Removes Game Over Widgets Temporarily
    global qCount, usedQuestions, actualAnswer, usersAnswer, points, gameOver
    qCount = 0  # Int
    usedQuestions = []  # List
    actualAnswer = 0  # Integer
    usersAnswer = 0  # Integer
    points = 0  # Integer
    score.config(text="Score: %s" % points)
    gameOver.place_forget()
    btnRestart.place_forget()
    resetBtns()
    displayQuestion()

def btnPressed(answer):
    # Checks Which Button Has Been Pressed
    # And Changes The Color of Text

    resetBtns()  # Calls Procedures to Reset Buttons

    if answer == 1:
        btnA.config(fg = "#FFFFFF")
    elif answer == 2:
        btnB.config(fg = "#FFFFFF")
    elif answer == 3:
        btnC.config(fg="#FFFFFF")
    elif answer == 4:
        btnD.config(fg="#FFFFFF")
    global usersAnswer
    usersAnswer = answer

def resetBtns():
    #  Resets the Text of the Buttons and Answer
    global usersAnswer
    btnA.config(fg="#000000")
    btnB.config(fg="#000000")
    btnC.config(fg="#000000")
    btnD.config(fg="#000000")
    usersAnswer = 0

# Graphics
def gui():

    global qNum, question, btnA, btnB, btnC, btnD, score, gameOver, btnRestart

    #  Window Configuration
    win = Tk()  # GUI Window
    win.title("AZ Permit Study Guide")  # Window Title
    fgColor = "#FFFFFF"  # Font Color
    bgColor = "#000000"  # Background Color
    text = ("Verdana",18) #  Tuple With String and Int
    win.geometry("1920x1080")  # Window Size
    win.iconbitmap(r"Driver.ico")  # Windows Icon

    #  Background Image for App
    bgImage = PhotoImage(file = r"background.png")
    Label(win,image = bgImage).place(relwidth=1,relheight =1)

    # Main Title and Frame of Program
    titleFrame = Frame(win,bg=bgColor)
    titleFrame.place(relwidth = 1, relheight =0.08)

    # Main Title Label Widgets
    Label(titleFrame,
          text="AZ Permit Study Guide",
          font = text,
          anchor = CENTER,
          fg = fgColor,
          bg = bgColor).place(relx = 0,relheight = 1)

    # Score Label Widget
    score = Label(titleFrame,
                  text="Score: 0",
                  font = text,
                  anchor = E,
                  fg = fgColor,
                  bg = bgColor)

    score.place(relx = 0.82,
                relwidth=0.18,
                relheight = 1)

    #  Label Widgets for Question Number
    qNum = Label(win,
                 fg = fgColor,
                 bg = bgColor,
                 font = text)

    qNum.place(relx=0.1,
               rely=0.15,
               relwidth = 0.8,
               relheight = 0.1)

    #  Label Widget For Question
    question = Label(win,
                     text="Press Start to Begin",
                     fg = fgColor,
                     bg = "#303030",
                     font = text)
    question.place(relx = 0.1,
                   rely = 0.25,
                   relwidth = 0.8,
                   relheight = 0.3)

    # Image for Buttons
    btnImg = PhotoImage(file = r"button.png")
    nextBtn = Button(win,
                     text = "Next",
                     bd = 0,
                     image = btnImg,
                     compound = CENTER,
                     command = checkAnswer,
                     font=("Verdana",15))

    # Next Button Which Will Trigger a Change of Questions

    # First Multiple Choice Answers
    btnA = Button(win,
                  text = "Test",
                  image = btnImg,
                  compound = CENTER,
                  command = lambda:btnPressed(1))

    btnA.place(relx= 0.1,
               rely=0.6,
               relwidth = 0.35,
               relheight =0.1)

    # Second Multiple Choice Answer
    btnB = Button(win,
                  text="Test",
                  image=btnImg,
                  compound=CENTER,
                  command = lambda:btnPressed(2))

    btnB.place(relx=0.55,
               rely=0.6,
               relwidth=0.35,
               relheight=0.1)

    # Third Multiple Choice Answer
    btnC = Button(win,
                  text="Test",
                  image=btnImg,
                  compound=CENTER,
                  command = lambda:btnPressed(3))

    btnC.place(relx=0.1,
               rely=0.8,
               relwidth=0.35,
               relheight=0.1)

    # Fourth Multiple Choice Answer
    btnD = Button(win,
                  text="Test",
                  image=btnImg,
                  compound=CENTER,
                  command = lambda:btnPressed(4))

    btnD.place(relx=0.55,
               rely=0.8,
               relwidth=0.35,
               relheight=0.1)

    def hideStart():
        # Hides Start Button & Runs 1st Question
        btnStart.destroy()  # Removes Start Button
        displayQuestion()  # Runs 1st Question

        # Displays Next Button on the Screen
        nextBtn.place(relx=0.91,
                      rely=0.35,
                      relwidth=0.08,
                      relheight=0.1)

    # Start Button Which Appears at the Beginning
    btnStart = Button(win,
                      text="Start",
                      image = btnImg,
                      compound = CENTER,
                      command = hideStart,
                      font=("Arial",50))

    btnStart.place(relx = 0.1,
                   rely=0.6,
                   relwidth =0.8,
                   relheight = 0.3)

    # Game Over Label Which Appears at the End
    gameOver = Label(win,
                     fg="#FFFFFF",
                     bg ="#000000",
                     font=("Verdana",50))

    # Restart Button Which Appears at the End
    btnRestart = Button(win,
                        text="Restart Game",
                        command = resetGame)

    win.mainloop()
# Call Procedure
gui()