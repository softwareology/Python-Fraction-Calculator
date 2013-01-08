from datetime import datetime


def getDateTime():
    dateTimeNow = str(datetime.now())
    
    date = dateTimeNow[0:10]
    time = dateTimeNow[11:19]
    
    year = date[0:4]
    month = date[5:7]
    day = date[8:10]
    
    hour = time[0:2]
    minute = time[3:5]
    second = time[6:8]
    return year, month, day, hour, minute, second

def getLogPrefix(year, month, day, hour, minute, second):
    dateP = "[%s/%s/%s]" % (year, month, day)
    timeP = "[%s:%s:%s]" % (hour, minute, second)
    Prefix = "%s%s" % (dateP, timeP)
    return Prefix

def getFullEvent(prefix, event, description):
    partA = "[Event: %s]" % (event)
    full = "%s%s %s\n" % (prefix, partA, description)
    return full

def getLog(event, description):
    y, m, d, h, mi, s = getDateTime()
    prefix = getLogPrefix(y, m, d, h, mi, s)
    fullEvent = getFullEvent(prefix, event, description)
    return fullEvent
