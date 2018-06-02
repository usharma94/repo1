#Programmer: Upma Sharma

##Program: A2: Even function
##Date: March 1st, 2018

"""Purpose: Use the math and turtle module to map out a fundamental sin wave
and corresponding harmonicfrequencies. Add the frequencies to map out a
Triangle wave."""

import math 
import turtle



#set up the screen.

def makeScreen(amp):
    wn = turtle.Screen()
    wn.bgcolor("lightyellow")
    wn.setworldcoordinates(-100, (-amp-50), 500, (amp+50)) 
    return (wn)

#set up turtles and their attributes including: name, shape, color, pensize. 


def makeTurtle(color):
    a_turtle = turtle.Turtle()
    a_turtle.shape("turtle")
    a_turtle.pensize(3)
    a_turtle.speed("fastest")
    a_turtle.color(color)
   
    
    return( a_turtle)

#draw and label the x-axis for reference

def makeGraph():
    a_turtle = makeTurtle("black")
    a_turtle.shape("classic")
    a_turtle.forward(400)
    a_turtle.penup()
    a_turtle.forward(20)
    a_turtle.pendown()
    a_turtle.write("x-axis")
    a_turtle.penup()
    a_turtle.forward(-20)
    a_turtle.goto(0,0)
    a_turtle.pendown()
    a_turtle.hideturtle()
    
    
"""set up function that calculates the fundamental frequency and
moves the turtle."""

def sinWave(a_turtle, amp, freq):
    for x in range(361):
        sin_wave =amp* (math.sin(math.radians(x)*freq))
        a_turtle.goto(x,sin_wave)

# set up function that calculates the sum of the waves to form a spectrum

def sumofWaves(a_turtle):
    for x in range(361):
        sum_calc  = (100*(math.sin(math.radians(x)*1))) + (100/2* (math.sin(math.radians(x)*2))) +(100/4* (math.sin(math.radians(x)*4))) + (100/6* (math.sin(math.radians(x)*6))) + (100/8* (math.sin(math.radians(x)*8)))

        a_turtle.goto(x,sum_calc)

"""set up function that calls up the sinWave, sumofWave function and defines
the parameters that need to be supplied to the respective functions to form the
fundamental wave, even harmonic waves 1-4, and spectrum wave."""

def drawWaves(tur1,tur2,tur3, tur4, tur5, tur6, amp, freq):
    for x in range (1):
        sinWave(tur1,amp,freq)
        sinWave(tur2,amp/2,freq*2)
        sinWave(tur3,amp/4, freq*4)
        sinWave(tur4, amp/6, freq*6)
        sinWave(tur5, amp/8, freq*8)
        sumofWaves(tur6)
    
"""the main function calls the above functions and supplies the parameters
such that the program can be excecuted. Asks the user for input on
the reference amplitude and frequency.""" 

def main():

    amp = int(input("Please enter the amplitude of the sinwave as a number: "))
    freq = int(input("Please enter the frequency of the sinwave as a number: "))

    wn = makeScreen(amp)

    makeGraph()

    fo = makeTurtle("red"); fi = makeTurtle("purple"); fie = makeTurtle("green")
    fum = makeTurtle("pink"); fai = makeTurtle("blue"); fil = makeTurtle("black")

    drawWaves(fo, fi, fie, fum, fai, fil, amp, freq)

    wn.exitonclick()

main()


