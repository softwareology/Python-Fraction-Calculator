#Py 3.2
#Add-on Script for Fractal.py
#Finds equaivilant fractions

def find(na, nb, da, db):
    dc = da*db
    na *= db
    nb *= da
    return na, nb, dc

def improp(w, n, d):
    n = w * d + n
    return n

def low(nom, denom):
    primes=[]
    try:
        rem = denom % nom
        if rem == 0:
            denom /= nom
            nom /= nom
            return int(nom), int(denom)
        else:
            while nom not in primes:
                if nom==0:
                    return 0, int(denom)
                for i in range(2, int(denom)):
                    for x in range(2, i):
                        if i % x == 0:
                            break
                    else:
                        primes.append(i)
                for p in range(len(primes)):
                    if denom % int(primes[p]) == 0 and nom % int(primes[p]) == 0:
                        denom /= primes[p]
                        nom /= primes[p]
        return int(nom), int(denom)
    except:
        while nom not in primes:
            if nom==0:
                return 0, int(denom)
            for i in range(2, int(denom)):
                for x in range(2, i):
                    if i % x == 0:
                        break
                else:
                    primes.append(i)
            for p in range(len(primes)):
                if denom % int(primes[p]) == 0 and nom % int(primes[p]) == 0:
                    denom /= primes[p]
                    nom /= primes[p]
    return int(nom), int(denom)

