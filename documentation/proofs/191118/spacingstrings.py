import datetime

now = datetime.datetime.now()
newFileName = "spacingstrings" + now.strftime("%Y_%m_%d-%H_%M_%S")

# Text from external source
path = "spacingstrings.txt"
strings = open(path, "r", encoding="utf-8")
stringstext = strings.read()
strings.close()
#stringstext = stringstext.split("\n")

# Text from external source
path = "spacingstrings_roman.txt"
strings = open(path, "r", encoding="utf-8")
stringsroman = strings.read()
strings.close()
#stringstext = stringstext.split("\n")

# Text from external source
path = "spacingstrings_italic.txt"
strings = open(path, "r", encoding="utf-8")
stringsitalic = strings.read()
strings.close()
#stringstext = stringstext.split("\n")

# Variables
fnames = ["Fraunces", "Fraunces Italic", "Recur Mono"]
frauncesVals = listFontVariations(fnames[0])
wghtMin = frauncesVals['wght']['minValue']
wghtMax = frauncesVals['wght']['maxValue']
opMin = frauncesVals['opsz']['minValue']
opMax = frauncesVals['opsz']['maxValue']

wghtVals = (wghtMin, wghtMax)
opVals = (opMin, opMax)

print(wghtVals)

margin = 50
gutter = 25
columns = (4,2)
print(width())
print(width()/2)
sizeincrements = 72
masters = len(wghtVals) + len(opVals)
fSize = (24,24)
# weightmin = frauncesVals[0()]


## Start of Script ##
# For Fraunces and for Fraunces Italic:
for f in range(0,2,1):
    # For all values in wghtVals
    for x in (1, 1000):
        if f == 0:
            stringstextr = stringstext + stringsroman
        if f == 1: 
            stringstextr = stringstext + stringsitalic
        # For all values in opVals, draw a new page
        #for goofy in (0,100):
        for y in (9.1, 144):
            stringstextr2 = stringstextr
            while len(stringstextr2) > 0:
                newPage("TabloidLandscape")
                font(fnames[2], 9)
                fontVariations(resetVariations=True)
                text("OpSz: %s, Wght: %s, " % (y,x), (50,50))
                # For number of values specified in columns, draw a new column.
                for z in range(0,4,1):
                    boxWidth = width()/4
                    fontVariations(wght = x, opsz = y)
                    font(fnames[f], 24)
                    stringstextr2 = textBox(stringstextr2, ((margin+(boxWidth*z)),margin+20,boxWidth,height()-margin*2))
                    
#saveImage("PDFs/%s.pdf" % (newFileName))