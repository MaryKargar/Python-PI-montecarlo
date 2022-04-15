import turtle
import tkinter as tk
# import random
import matplotlib.pyplot as plt
import math
from rng4 import *
import datetime
randoms=[]

root = tk.Tk()
canvas = tk.Canvas(root)
canvas.config(width=400, height=200)
canvas.pack(side=tk.LEFT)
screen = turtle.TurtleScreen(canvas)
pen= turtle.RawTurtle(screen)
pen.hideturtle()
pen.speed(0)
# screen.bgcolor("cyan")
inCircle = 0
outCircle = 0
piValues = []
errors=0
stop=False
xpoints=[]
ypoints=[]
def accuracy(num,n):
    temp = str(num)
    for x in range(len(temp)):
        if temp[x] == '.':
            try:
                return float(temp[:x+n+1])
            except:
                return float(temp)      
    return float(temp)
    
def calculateP():
    # screen.clear()
    # drawSquare()  
    global inCircle
    global outCircle
    global piValues
    global stop
    global randoms
    global xpoints,ypoints
    randoms=customRandom(int(randomValue.get()))
    c=0
    for i in range(3):
        for j in randoms:
            x=j
            xpoints.append(x)           
            if c<len(randoms)-1:
                y=randoms[c+1]
                ypoints.append(y)
                c=c+1

            if (x**2+y**2>100**2):
                pen.color("blue")
                pen.up()
                pen.goto(x,y)
                pen.down()
                pen.dot()
                outCircle = outCircle+1

            else:
                pen.color("red")
                pen.up()
                pen.goto(x,y)
                pen.down()
                pen.dot()
                inCircle = inCircle+1

            pi = 4.0 * inCircle / (inCircle + outCircle)

            piValues.append(pi)
            
            errors = [abs(math.pi - pi) for pi in piValues]
        
        print (piValues[-1])
        pEntryValue.set(accuracy(piValues[-1], int(accuracyValue.get())))
    savePlot()
        

  
def showPlot():
    global piValues
    global errors
    global xpoints,ypoints
    
    plt.hist(xpoints,color='red')
    plt.ylabel("Iterations")
    plt.xlabel("X points")
    plt.show()

    plt.clf()

    plt.hist(ypoints,color='red')
    plt.ylabel("Iterations")
    plt.xlabel("Y points")
    plt.show()
    plt.clf()

    plt.axvline(x=0.0, color='yellow', linestyle='-')
    plt.hist(errors,color='red')
    plt.ylabel("Iterations")
    plt.xlabel("Error")
    plt.show()
    plt.clf()

    plt.axvline(x=math.pi, color='yellow', linestyle='-')
    plt.hist(piValues,range=[0, 11],color="red",)
    plt.ylabel("Iterations")
    plt.xlabel("Value of PI")
    plt.show()
    plt.clf()

def savePlot():
    global piValues
    global errors
    global xpoints,ypoints
    time = datetime.datetime.now()
    timeStamp= f"{time.year}-{time.month}-{time.day}-{time.hour}-{time.minute}-{time.second}"
 

    plt.hist(xpoints,color='red')
    plt.ylabel("Iterations")
    plt.xlabel("X points")
    plt.savefig(f"Histogram_x_{timeStamp}.png")

    plt.clf()

    plt.hist(ypoints,color='red')
    plt.ylabel("Iterations")
    plt.xlabel("Y points")
    plt.savefig(f"y_Zeitstempel_{timeStamp}.png")

    plt.clf()

    plt.hist(piValues,range=[0, 11],color="red",)
    plt.ylabel("Iterations")
    plt.xlabel("Value of PI")   
    plt.savefig(f"pi_Zeitstempel_{timeStamp}.png")

    plt.clf()

    plt.axvline(x=0.0, color='yellow', linestyle='-')
    plt.hist(errors,color='red')
    plt.ylabel("Iterations")
    plt.xlabel("Error")
    plt.savefig(f"pi_Zeitstempel_errors_{timeStamp}.png")

    plt.clf()

    
def finish():
    global root
    root.withdraw()
def drawSquare():
    global pen
    pen.color("black")
    pen.up()
    pen.setposition(-100,-100)
    pen.down()
    pen.fd(200)
    pen.left(90)
    pen.fd(200)
    pen.left(90)
    pen.fd(200)
    pen.left(90)
    pen.fd(200)
    pen.left(90)
    pen.up()
    pen.setposition(0,-100)
    pen.down()
    pen.circle(100)



frame = tk.Frame(root)
frame.pack(side = tk.TOP)

emptyLable = tk.Label(frame, text="")
emptyLable.grid(row= 0, column=0)

randomLable = tk.Label(frame, text= "number of random")
randomValue= tk.StringVar()
randomEntry = tk.Entry(frame, text =randomValue)
randomLable.grid(row= 1, column=0)
randomEntry.grid(row= 1, column=1)
emptyLable = tk.Label(frame, text="")
emptyLable.grid(row= 2, column=0)

accuracyLable = tk.Label(frame, text= "Accuracy",pady=20)
accuracyValue=tk.StringVar()
accuracyEntry = tk.Entry(frame, text=accuracyValue)
accuracyLable.grid(row= 3, column=0)
accuracyEntry.grid(row= 3, column=1)

emptyLable.grid(row= 4, column=0)

buttonStart = tk.Button(frame, text="Start", command=calculateP)
buttonStart.grid(row= 5, column=0)
buttonCancel = tk.Button(frame, text="Cancel", command=finish)
buttonCancel.grid(row= 5, column=2)

buttonPlot = tk.Button(frame, text="Show Plot", command=showPlot)
buttonPlot.grid(row= 5, column=1)

emptyLable.grid(row= 6, column=0)
pLable = tk.Label(frame, text= "π")
pEntryValue = tk.StringVar()
pEntry = tk.Entry(frame, text=pEntryValue)
pLable.grid(row= 7, column=0)
pEntry.grid(row= 7, column=1)

drawSquare()



root.mainloop()
    