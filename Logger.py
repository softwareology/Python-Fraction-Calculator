import logUtils

"""
Python Logger Script

Programmer: Thomas Boland
"""


def writeLog(file, log):
    fileObject = open(file, 'w')
    fileObject.write(log)
    fileObject.close()
    return None


if __name__ == "__main__":
    file = "%s.log" % (input("Log title: "))
    log = ""
    while True:
        event = input("Log event: ")
        description = input("Log description:\n")
        log = "%s%s" % (log, logUtils.getLog(event, description))
        writeLog(file, log)
