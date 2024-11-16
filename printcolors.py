def printColered(text, color):
    return '<p style="font-size: 50px; color:' + color + ';">' + text + '<p/p>'

def printGreen(text):
    return printColered(text, "green")

def printBlack(text):
    return printColered(text, "black")

def printRed(text):
    return printColered(text, "red")