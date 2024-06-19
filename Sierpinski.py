# Author: Martin Ringman
# 4/10/2022

from graphics import *
import random, math

# returns tuple of x-y coordinates of a randomly chosen corner of triangle
def pickRandomCorner():
    cornerChoice = random.randrange(1,4)
    if cornerChoice == 1:
        cornerCoordinates = corner1
    elif cornerChoice == 2:
        cornerCoordinates = corner2
    else:
        cornerCoordinates = corner3
    return cornerCoordinates

# passed coordinates of two points
# returns finds distance between two points
def findEuclideanDistance(p1, p2): # (2-tuple), (2-tuple) -> float
    distance = math.sqrt((p1[0] - p2[0])*(p1[0] - p2[0]) + (p1[1] - p2[1])*(p1[1] - p2[1]))
    return distance

# passed tuple of x-y coordinates of current point
# returns 3 integers for red, green, blue values (0 - 255)
def getColor(point):
    redLocal = int((1 - findEuclideanDistance(point, corner1)/ maxDistance) * 256)
    greenLocal = int((1 - findEuclideanDistance(point, corner2) / maxDistance) * 256)
    blueLocal = int((1 - findEuclideanDistance(point, corner3) / maxDistance) * 256)
    return redLocal, greenLocal, blueLocal
    
# MAIN
width = int(input("How wide do you want your window? "))
height = int(input("How tall do you want your window? "))

corner1 = (width // 2, 0)  #red corner (top middle)
corner2 = (0, height)      #green corner (lower left)
corner3 = (width, height)  #blue corner (lower right)

distance1 = findEuclideanDistance(corner1, corner2)
distance2 = findEuclideanDistance(corner2, corner3)
if distance1 > distance2:
    maxDistance = distance1
else:
    maxDistance = distance2

win = GraphWin("window title", width, height) #open window of desired size

currentPoint = (random.randrange(width), random.randrange(height)) #finding a first random point

i = 1
while i <= 50000:
    currentCorner = pickRandomCorner()
    currentPoint = (currentPoint[0] + currentCorner[0]) / 2, (currentPoint[1] + currentCorner[1]) / 2 
    if i > 10:
        red, green, blue = getColor(currentPoint) 
        win.plot(currentPoint[0], currentPoint[1], color_rgb(red, green, blue))
    i += 1

input("Hit Enter to quit") 
win.close()
