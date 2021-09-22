#Program to Calculate Depth or Distance (D)  from the earth’s surface to a cave bottom (location of radio transmitter) 
#Last Date Modified: 19 September 2018 
#Authors: Biral Pruthviraj Chaudhari (specifications, programming), Maria Deligero (specifications, programming), Roni Furst (test values table), Vicki Sahanatien (specifications, programming, error checking), Urvash Prajapait algorithm, programming) 
#import data 
import math 
#user input and Initialization 
L=float(input("please enter the surface length:")) 
x=float(input("please enter the angle measured at surface:")) 
#implementation ( logic) 
#splitting the formulae into small parts 
y=(math.radians(x)) 
a=2*L  
print (a )
b=float(9*(math.tan(y)**2)+8) 
print (b )
c=3*(math.tan(y)) 
print (c )
#final result calculation 
D=a/(math. sqrt(b)- c)  #green highlight shows where the code correction was made  
print (D) 
#end of the program 

 
