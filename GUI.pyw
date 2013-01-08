import pygame
import Fractal
import logUtils
from pygame.locals import *
from PGSetup import *
from PGBasic import *
from dat import *
from datetime import *
from Logger import *

BACKGROUND = (236, 233, 216)
CANCEL = -1
running = True
secsA = str(datetime.now())
secsB = [secsA[11:13], secsA[14:16], secsA[17:18]]
mins = (int(secsB[0]) * 60) + int(secsB[1])
secs = (mins * 60) + int(secsB[2])

logFile = "Logs\\%st=%s.log" % (str(datetime.now())[0:10], str(secs))
log = ""

#Small button:
#34 by 27

screen = winInit('Fraction Calculator V2.2.1', "Data\\icon.bmp", 424, 212, 0, 32)
screen.fill(BACKGROUND)

def showButtons(screen):
    screen.blit(box, boxrect)
    screen.blit(seven, sevenrect)
    screen.blit(eight, eightrect)
    screen.blit(nine, ninerect)
    screen.blit(div, divrect)
    screen.blit(fract, fractrect)
    screen.blit(four, fourrect)
    screen.blit(five, fiverect)
    screen.blit(six, sixrect)
    screen.blit(mult, multrect)
    screen.blit(mix, mixrect)
    screen.blit(one, onerect)
    screen.blit(two, tworect)
    screen.blit(three, threerect)
    screen.blit(sub, subrect)
    screen.blit(zero, zerorect)
    screen.blit(add, addrect)
    screen.blit(eq, eqrect)
    screen.blit(back, backrect)
    screen.blit(ce, cerect)
    #screen.blit(copy, copyrect)

def showString(string, screen):
    if string == "":
        showText(screen, 9, 9, "0", size=25)
    else:
        showText(screen, 9, 9, string, size=25)
    #print(string)

def solve(toSolve):
    partA = []
    again = 0
    toSolve = toSolve.split()
    if len(toSolve) == 1:
        return str(toSolve[0])

# Plus

# x + x
    elif toSolve[1] == "+" and len(toSolve) == 3:
        return str(int(toSolve[0])+int(toSolve[2]))
# x + x | x
    elif toSolve[1] == "+" and toSolve[3] == "|" and len(toSolve) == 5:
        return str(Fractal.add(0, int(toSolve[2]), 1, int(toSolve[4]), int(toSolve[0]), 0))
# x + x _ x | x
    elif toSolve[1] == "+" and toSolve[3] == "_" and toSolve[5] == "|" and len(toSolve) == 7:
        return str(Fractal.add(0, int(toSolve[4]), 1, int(toSolve[6]), int(toSolve[0]), int(toSolve[2])))
# x | x + x
    elif toSolve[1] == "|" and toSolve[3] == "+" and len(toSolve) == 5:
        return str(Fractal.add(int(toSolve[0]), 0, int(toSolve[2]), 1, 0, int(toSolve[4])))
# x _ x | x + x
    elif toSolve[1] == "_" and toSolve[3] == "|" and toSolve[5] == "+" and len(toSolve) == 7:
        return str(Fractal.add(int(toSolve[2]), 0, int(toSolve[4]), 1, int(toSolve[0]), int(toSolve[6])))
# x | x + x | x
    elif toSolve[1] == "|" and toSolve[3] == "+" and toSolve[5] == "|" and len(toSolve) == 7:
        return str(Fractal.add(int(toSolve[0]), int(toSolve[4]), int(toSolve[2]), int(toSolve[6]), 0, 0))
# x | x + x _ x | x
    elif toSolve[1] == "|" and toSolve[3] == "+" and toSolve[5] == "_" and toSolve[7] == "|" and len(toSolve) == 9:
        return str(Fractal.add(int(toSolve[0]), int(toSolve[6]), int(toSolve[2]), int(toSolve[8]), 0, int(toSolve[4])))
# x _ x | x + x | x
    elif toSolve[1] == "_" and toSolve[3] == "|" and toSolve[5] == "+" and toSolve[7] == "|" and len(toSolve) == 9:
        return str(Fractal.add(int(toSolve[2]), int(toSolve[6]), int(toSolve[4]), int(toSolve[8]), int(toSolve[0]), 0))
# x _ x | x + x _ x | x
    elif toSolve[1] == "_" and toSolve[3] == "|" and toSolve[5] == "+" and toSolve[7] == "_" and toSolve[9] == "|" and len(toSolve)== 11:
        return str(Fractal.add(int(toSolve[2]), int(toSolve[8]), int(toSolve[4]), int(toSolve[10]), int(toSolve[0]), int(toSolve[6])))
# Minus

# x - x
    elif toSolve[1] == "-" and len(toSolve) == 3:
        return str(int(toSolve[0])-int(toSolve[2]))
# x - x | x
    elif toSolve[1] == "-" and toSolve[3] == "|" and len(toSolve) == 5:
        return str(Fractal.subtract(0, int(toSolve[2]), 1, int(toSolve[4]), int(toSolve[0]), 0))
# x - x _ x | x
    elif toSolve[1] == "-" and toSolve[3] == "_" and toSolve[5] == "|" and len(toSolve) == 7:
        return str(Fractal.subtract(0, int(toSolve[4]), 1, int(toSolve[6]), int(toSolve[0]), int(toSolve[2])))
# x | x - x
    elif toSolve[1] == "|" and toSolve[3] == "-" and len(toSolve) == 5:
        return str(Fractal.subtract(int(toSolve[0]), 0, int(toSolve[2]), 1, 0, int(toSolve[4])))
# x _ x | x - x
    elif toSolve[1] == "_" and toSolve[3] == "|" and toSolve[5] == "-" and len(toSolve) == 7:
        return str(Fractal.subtract(int(toSolve[2]), 0, int(toSolve[4]), 1, int(toSolve[0]), int(toSolve[6])))
# x | x - x | x
    elif toSolve[1] == "|" and toSolve[3] == "-" and toSolve[5] == "|" and len(toSolve) == 7:
        return str(Fractal.subtract(int(toSolve[0]), int(toSolve[4]), int(toSolve[2]), int(toSolve[6]), 0, 0))
# x | x - x _ x | x
    elif toSolve[1] == "|" and toSolve[3] == "-" and toSolve[5] == "_" and toSolve[7] == "|" and len(toSolve) == 9:
        return str(Fractal.subtract(int(toSolve[0]), int(toSolve[6]), int(toSolve[2]), int(toSolve[8]), 0, int(toSolve[4])))
# x _ x | x - x | x
    elif toSolve[1] == "_" and toSolve[3] == "|" and toSolve[5] == "-" and toSolve[7] == "|" and len(toSolve) == 9:
        return str(Fractal.subtract(int(toSolve[2]), int(toSolve[6]), int(toSolve[4]), int(toSolve[8]), int(toSolve[0]), 0))
# x _ x | x - x _ x | x
    elif toSolve[1] == "_" and toSolve[3] == "|" and toSolve[5] == "-" and toSolve[7] == "_" and toSolve[9] == "|" and len(toSolve)== 11:
        return str(Fractal.subtract(int(toSolve[2]), int(toSolve[8]), int(toSolve[4]), int(toSolve[10]), int(toSolve[0]), int(toSolve[6])))

# Times

# x * x
    elif toSolve[1] == "*" and len(toSolve) == 3:
        return str(int(toSolve[0])*int(toSolve[2]))
# x * x | x
    elif toSolve[1] == "*" and toSolve[3] == "|" and len(toSolve) == 5:
        return str(Fractal.multiply(0, int(toSolve[2]), 1, int(toSolve[4]), int(toSolve[0]), 0))
# x * x _ x | x
    elif toSolve[1] == "*" and toSolve[3] == "_" and toSolve[5] == "|" and len(toSolve) == 7:
        return str(Fractal.multiply(0, int(toSolve[4]), 1, int(toSolve[6]), int(toSolve[0]), int(toSolve[2])))
# x | x * x
    elif toSolve[1] == "|" and toSolve[3] == "*" and len(toSolve) == 5:
        return str(Fractal.multiply(int(toSolve[0]), 0, int(toSolve[2]), 1, 0, int(toSolve[4])))
# x _ x | x * x
    elif toSolve[1] == "_" and toSolve[3] == "|" and toSolve[5] == "*" and len(toSolve) == 7:
        return str(Fractal.multiply(int(toSolve[2]), 0, int(toSolve[4]), 1, int(toSolve[0]), int(toSolve[6])))
# x | x * x | x
    elif toSolve[1] == "|" and toSolve[3] == "*" and toSolve[5] == "|" and len(toSolve) == 7:
        return str(Fractal.multiply(int(toSolve[0]), int(toSolve[4]), int(toSolve[2]), int(toSolve[6]), 0, 0))
# x | x * x _ x | x
    elif toSolve[1] == "|" and toSolve[3] == "*" and toSolve[5] == "_" and toSolve[7] == "|" and len(toSolve) == 9:
        return str(Fractal.multiply(int(toSolve[0]), int(toSolve[6]), int(toSolve[2]), int(toSolve[8]), 0, int(toSolve[4])))
# x _ x | x * x | x
    elif toSolve[1] == "_" and toSolve[3] == "|" and toSolve[5] == "*" and toSolve[7] == "|" and len(toSolve) == 9:
        return str(Fractal.multiply(int(toSolve[2]), int(toSolve[6]), int(toSolve[4]), int(toSolve[8]), int(toSolve[0]), 0))
# x _ x | x * x _ x | x
    elif toSolve[1] == "_" and toSolve[3] == "|" and toSolve[5] == "*" and toSolve[7] == "_" and toSolve[9] == "|" and len(toSolve)== 11:
        return str(Fractal.multiply(int(toSolve[2]), int(toSolve[8]), int(toSolve[4]), int(toSolve[10]), int(toSolve[0]), int(toSolve[6])))

# Divide

# x / x
    elif toSolve[1] == "/" and len(toSolve) == 3:
        return str(int(toSolve[0])//int(toSolve[2]))
# x / x | x
    elif toSolve[1] == "/" and toSolve[3] == "|" and len(toSolve) == 5:
        return str(Fractal.divide(0, int(toSolve[2]), 1, int(toSolve[4]), int(toSolve[0]), 0))
# x / x _ x | x
    elif toSolve[1] == "/" and toSolve[3] == "_" and toSolve[5] == "|" and len(toSolve) == 7:
        return str(Fractal.divide(0, int(toSolve[4]), 1, int(toSolve[6]), int(toSolve[0]), int(toSolve[2])))
# x | x / x
    elif toSolve[1] == "|" and toSolve[3] == "/" and len(toSolve) == 5:
        return str(Fractal.divide(int(toSolve[0]), 0, int(toSolve[2]), 1, 0, int(toSolve[4])))
# x _ x | x / x
    elif toSolve[1] == "_" and toSolve[3] == "|" and toSolve[5] == "/" and len(toSolve) == 7:
        return str(Fractal.divide(int(toSolve[2]), 0, int(toSolve[4]), 1, int(toSolve[0]), int(toSolve[6])))
# x | x / x | x
    elif toSolve[1] == "|" and toSolve[3] == "/" and toSolve[5] == "|" and len(toSolve) == 7:
        return str(Fractal.divide(int(toSolve[0]), int(toSolve[4]), int(toSolve[2]), int(toSolve[6]), 0, 0))
# x | x / x _ x | x
    elif toSolve[1] == "|" and toSolve[3] == "/" and toSolve[5] == "_" and toSolve[7] == "|" and len(toSolve) == 9:
        return str(Fractal.divide(int(toSolve[0]), int(toSolve[6]), int(toSolve[2]), int(toSolve[8]), 0, int(toSolve[4])))
# x _ x | x / x | x
    elif toSolve[1] == "_" and toSolve[3] == "|" and toSolve[5] == "/" and toSolve[7] == "|" and len(toSolve) == 9:
        return str(Fractal.divide(int(toSolve[2]), int(toSolve[6]), int(toSolve[4]), int(toSolve[8]), int(toSolve[0]), 0))
# x _ x | x / x _ x | x
    elif toSolve[1] == "_" and toSolve[3] == "|" and toSolve[5] == "/" and toSolve[7] == "_" and toSolve[9] == "|" and len(toSolve)== 11:
        return str(Fractal.divide(int(toSolve[2]), int(toSolve[8]), int(toSolve[4]), int(toSolve[10]), int(toSolve[0]), int(toSolve[6])))


    else:
        return str(toSolve)
    #return "0"

#Loop
while running:
    toShow = ""
    showButtons(screen)
    
    while True:
        showString(toShow, screen)
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                logEvent = "Mouse Button Down"
                description = "Location: %s, %s" % (str(x), str(y))
                log = "%s%s" % (log, logUtils.getLog(logEvent, description))
                writeLog(logFile, log)
# Zero
                if x >= 7 and y >= 173 and x <= 41 and y <= 200:
                    screen.blit(zerob, zerorect)
# One
                if x >= 7 and y >= 139 and x <= 41 and y <= 166:
                    screen.blit(oneb, onerect)
# Two
                if x >= 48 and y >= 139 and x <= 82 and y <= 166:
                    screen.blit(twob, tworect)
# Three
                if x >= 89 and y >= 139 and x <= 123 and y <= 166:
                    screen.blit(threeb, threerect)
# Four
                if x >= 7 and y >= 105 and x <= 41 and y <= 132:
                    screen.blit(fourb, fourrect)
# Five
                if x >= 48 and y >= 105 and x <= 82 and y <= 132:
                    screen.blit(fiveb, fiverect)
# Six
                if x >= 89 and y >= 105 and x <= 123 and y <= 132:
                    screen.blit(sixb, sixrect)
# Seven
                if x >= 7 and y >= 71 and x <= 41 and y <= 98:
                    screen.blit(sevenb, sevenrect)
# Eight
                if x >= 48 and y >= 71 and x <= 82 and y <= 98:
                    screen.blit(eightb, eightrect)
# Nine
                if x > 89 and y >= 71 and x <= 123 and y <= 98:
                    screen.blit(nineb, ninerect)
# Plus
                if x >= 130 and y >= 173 and x <= 164 and y <= 200:
                    screen.blit(addb, addrect)
# Minus
                if x >= 130 and y >= 139 and x <= 164 and y <= 166:
                    screen.blit(subb, subrect)
# Times
                if x >= 130 and y >= 105 and x <= 164 and y <= 132:
                    screen.blit(multb, multrect)
# Divide
                if x >= 130 and y >= 71 and x <= 164 and y <= 98:
                    screen.blit(divb, divrect)
# Fraction
                if x >= 171 and y >= 71 and x <= 205 and y <= 98:
                    screen.blit(fractb, fractrect)
# Space
                if x >= 171 and y >= 105 and x <= 205 and y <= 132:
                    screen.blit(mixb, mixrect)
# Clear
                if x >= 77 and y >= 37 and x <= 137 and y <= 64:
                    screen.blit(ceb, cerect)
# Delete
                if x >= 7 and y >= 37 and x <= 68 and y <= 64:
                    screen.blit(backb, backrect)
# Solve
                if x >= 171 and y >= 139 and x <= 205 and y <= 200:
                    screen.blit(eqb, eqrect)
# Copy
#                if x >= 48 and y >= 173 and x <= 123 and y <= 200:
#                    screen.blit(copyb, copyrect)
            if event.type == MOUSEBUTTONUP and event.button == 1:
                x, y = event.pos
                logEvent = "Mouse Button Up"
                description = "Location: %s, %s" % (str(x), str(y))
                log = "%s%s" % (log, logUtils.getLog(logEvent, description))
                writeLog(logFile, log)
# Zero
                if x >= 7 and y >= 173 and x <= 41 and y <= 200:
                    if toShow != "":
                        toShow = toShow + "0"
# One
                if x >= 7 and y >= 139 and x <= 41 and y <= 166:
                    toShow = toShow + "1"
# Two
                if x >= 48 and y >= 139 and x <= 82 and y <= 166:
                    toShow = toShow + "2"
# Three
                if x >= 89 and y >= 139 and x <= 123 and y <= 166:
                    toShow = toShow + "3"
# Four
                if x >= 7 and y >= 105 and x <= 41 and y <= 132:
                    toShow = toShow + "4"
# Five
                if x >= 48 and y >= 105 and x <= 82 and y <= 132:
                    toShow = toShow + "5"
# Six
                if x >= 89 and y >= 105 and x <= 123 and y <= 132:
                    toShow = toShow + "6"
# Seven
                if x >= 7 and y >= 71 and x <= 41 and y <= 98:
                    toShow = toShow + "7"
# Eight
                if x >= 48 and y >= 71 and x <= 82 and y <= 98:
                    toShow = toShow + "8"
# Nine
                if x > 89 and y >= 71 and x <= 123 and y <= 98:
                    toShow = toShow + "9"
# Plus
                if x >= 130 and y >= 173 and x <= 164 and y <= 200:
                    if toShow != "" and toShow[len(toShow)-1] != " ":
                        toShow = toShow + " + "
# Minus
                if x >= 130 and y >= 139 and x <= 164 and y <= 166:
                    if toShow != "" and toShow[len(toShow)-1] != " ":
                        toShow = toShow + " - "
# Times
                if x >= 130 and y >= 105 and x <= 164 and y <= 132:
                    if toShow != "" and toShow[len(toShow)-1] != " ":
                        toShow = toShow + " * "
# Divide
                if x >= 130 and y >= 71 and x <= 164 and y <= 98:
                    if toShow != "" and toShow[len(toShow)-1] != " ":
                        toShow = toShow + " / "
# Fraction
                if x >= 171 and y >= 71 and x <= 205 and y <= 98:
                    if toShow != "" and toShow[len(toShow)-1] != " ":
                        toShow = toShow + " | "
# Space
                if x >= 171 and y >= 105 and x <= 205 and y <= 132:
                    if toShow != "" and toShow[len(toShow)-1] != " ":
                        toShow = toShow + " _ "
# Clear
                if x >= 77 and y >= 37 and x <= 137 and y <= 64:
                    toShow = ""
# Delete
                if x >= 7 and y >= 37 and x <= 68 and y <= 64:
                    toShow = toShow[0:len(toShow)-1]
# Solve
                if x >= 171 and y >= 139 and x <= 205 and y <= 200:
                    toShow = toShow + " = " + str(solve(toShow))
                    logEvent = "Equation Solved"
                    description = "Equation: %s" % (toShow)
                    log = "%s%s" % (log, logUtils.getLog(logEvent, description))
                    writeLog(logFile, log)
# Copy
#                if x >= 48 and y >= 173 and x <= 123 and y <= 166:
#                    addToClipboard(toShow)
                showButtons(screen)
            if event.type == KEYUP:
                logEvent = "Key Up"
                description = "Key: %s" % (str(event.key))
                log = "%s%s" % (log, logUtils.getLog(logEvent, description))
                writeLog(logFile, log)
                if event.key == K_0 or event.key == K_KP0:
                    if toShow != "":
                        toShow = toShow + "0"
                if event.key == K_1 or event.key == K_KP1:
                    toShow = toShow + "1"
                if event.key == K_2 or event.key == K_KP2:
                    toShow = toShow + "2"
                if event.key == K_3 or event.key == K_KP3:
                    toShow = toShow + "3"
                if event.key == K_4 or event.key == K_KP4:
                    toShow = toShow + "4"
                if event.key == K_5 or event.key == K_KP5:
                    toShow = toShow + "5"
                if event.key == K_6 or event.key == K_KP6:
                    toShow = toShow + "6"
                if event.key == K_7 or event.key == K_KP7:
                    toShow = toShow + "7"
                if event.key == K_8 or event.key == K_KP8:
                    toShow = toShow + "8"
                if event.key == K_9 or event.key == K_KP9:
                    toShow = toShow + "9"
                if event.key == K_PLUS or event.key == K_KP_PLUS:
                    if toShow != "" and toShow[len(toShow)-1] != " ":
                        toShow = toShow + " + "
                if event.key == K_MINUS or event.key == K_KP_MINUS:
                    if toShow != "" and toShow[len(toShow)-1] != " ":
                        toShow = toShow + " - "
                if event.key == K_ASTERISK or event.key == K_KP_MULTIPLY:
                    if toShow != "" and toShow[len(toShow)-1] != " ":
                        toShow = toShow + " * "
                if event.key == K_SLASH or event.key == K_KP_DIVIDE:
                    if toShow != "" and toShow[len(toShow)-1] != " ":
                        toShow = toShow + " / "
                if event.key == K_BACKSLASH:
                    if toShow != "" and toShow[len(toShow)-1] != " ":
                        toShow = toShow + " | "
                if event.key == K_PERIOD or event.key == K_KP_PERIOD:
                    if toShow != "" and toShow[len(toShow)-1] != " ":
                        toShow = toShow + " _ "
                if event.key == K_SPACE:
                    toShow = ""
                if event.key == K_BACKSPACE:
                    toShow = toShow[0:len(toShow)-1]
                if event.key == K_EQUALS or event.key == K_KP_ENTER or event.key == K_KP_EQUALS:
                    toShow = toShow + " = " + str(solve(toShow))
                    logEvent = "Equation Solved"
                    description = "Equation: %s" % (toShow)
                    log = "%s%s" % (log, logUtils.getLog(logEvent, description))
                    writeLog(logFile, log)
                showButtons(screen)
                if event.key == K_ESCAPE:
                    logEvent = "System Exit"
                    description = "Program terminated"
                    log = "%s%s" % (log, logUtils.getLog(logEvent, description))
                    writeLog(logFile, log)
                    terminate()
            if event.type == QUIT:
                logEvent = "System Exit"
                description = "Program terminated"
                log = "%s%s" % (log, logUtils.getLog(logEvent, description))
                writeLog(logFile, log)
                terminate()
        pygame.display.update()
