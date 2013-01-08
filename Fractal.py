#Uses Python 3.2

import findEqual

CANCEL = -1

def add(na, nb, da, db, wa, wb):
    na = findEqual.improp(wa, na, da)
    nb = findEqual.improp(wb, nb, db)
    na, nb, dc = findEqual.find(na, nb, da, db)
    nc = na + nb
    if nc < 0:
        print("""This version of
the Fraction
Calculator cannot
support negative
fractions. Press
[ENTER] to re-enter
the equation.""")
        input("")
        return "0"
    if nc >= dc:
        try:
            nd = int(nc/dc)
        except:
            print("Cannot divide by Zero.")
            print("Press [ENTER] to")
            print("re-enter the equation.")
            input("")
            return "0"
        ne = nc % dc
        whole = nd
        nom = ne
        denom = dc
        nom, denom = findEqual.low(nom, denom)
        if nom != 0:
            return str(whole) + " " + str(nom) + "|" + str(denom)
        else:
            return str(whole)
    else:
        if nc != 0:
            nc, dc = findEqual.low(nc, dc)
            return str(nc) + "|" + str(dc)
        else:
            return "0"

#Subtract function
def subtract(na, nb, da, db, wa, wb):
    na = findEqual.improp(wa, na, da)
    nb = findEqual.improp(wb, nb, db)
    na, nb, dc = findEqual.find(na, nb, da, db)
    nc = na - nb
    if nc < 0:
        print("""This version of
the Fraction
Calculator cannot
support negative
numbers. Press
[ENTER] to re-enter
the equation.""")
        input("")
        return
    if nc >= dc:
        try:
            nd = int(nc/dc)
        except:
            print("Cannot divide by Zero.")
            print("Press [ENTER] to")
            print("re-enter the equation.")
            input("")
            return
        ne = nc % dc
        whole = nd
        nom = ne
        denom = dc
        nom, denom = findEqual.low(nom, denom)
        if nom != 0:
            return str(whole) + " " + str(nom) + "|" + str(denom)
        else:
            return str(whole)
    else:
        if nc != 0:
            nc, dc = findEqual.low(nc, dc)
            return str(nc) + "|" + str(dc)
        else:
            return "0"

#Multiply function
def multiply(na, nb, da, db, wa, wb):
    na = findEqual.improp(wa, na, da)
    nb = findEqual.improp(wb, nb, db)
    dc = da * db
    nc = na * nb
    if nc < 0:
       print("""This version of
the Fraction
Calculator cannot
support negative
numbers. Press
[ENTER] to re-enter
the equation.""")
       input("")
       return
    if nc >= dc:
        try:
            nd = int(nc/dc)
        except:
            print("Cannot divide by Zero.")
            print("Press [ENTER] to")
            print("re-enter the equation.")
            input("")
            return
        ne = nc % dc
        whole = nd
        nom = ne
        denom = dc
        nom, denom = findEqual.low(nom, denom)
        if nom != 0:
            return str(whole) + " " + str(nom) + "|" + str(denom)
        else:
            return str(whole)
    else:
        if nc != 0:
            nc, dc = findEqual.low(nc, dc)
            return str(nc) + "|" + str(dc)
        else:
            return "0"

#Divide function
def divide(na, nb, da, db, wa, wb):
    na = findEqual.improp(wa, na, da)
    nb = findEqual.improp(wb, nb, db)
    dc = da * nb
    nc = na * db
    if nc < 0:
        print("""This version of
the Fraction
Calculator cannot
support negative
numbers. Press
[ENTER] to re-enter
the equation.""")
        input("")
        return
    if nc >= dc:
        try:
            nd = int(nc/dc)
        except:
            print("Cannot divide by Zero.")
            print("Press [ENTER] to")
            print("re-enter the equation.")
            input("")
            return
        ne = nc % dc
        whole = nd
        nom = ne
        denom = dc
        nom, denom = findEqual.low(nom, denom)
        if nom != 0:
            return str(whole) + " " + str(nom) + "|" + str(denom)
        else:
            return str(whole)
    else:
        if nc != 0:
            nc, dc = findEqual.low(nc, dc)
            return str(nc) + "|" + str(dc)
        else:
            return "0"

