import random

print "Light puzzle"

desk = []
loop = 0
for i in range(3):
    desk.append(["X"] * 3)

def print_desk(desk):
    for row in desk:
        print " ".join(row)

def  turnInitialLightsOn(desk):
    desk[1][1]='Y'
 
"""Method to get the random position"""   
def random_position():
    return random.randint(0, 2)
    
"""Actual logic starts here"""
def startPlaying():
    pos = raw_input('Enter the position')
    print "Moves : %s" % loop
    row = -1
    col = -1
    x = pos.split(' ')
    row = x[0]
    col = x[1]
    print "row is %s, col is %s" % (row, col)

turnInitialLightsOn(desk)
print 'Initially center light turned on'
print_desk(desk)

while loop < 10:
    startPlaying()
    loop+=1
    
    
    
print "Game Over!!!"
