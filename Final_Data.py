"""

function to open data ,reads  and separates by commas
"""
def readD():
    with open("   ")

with open ("Lewis.txt") as lewis:
    data = lewis.readline()
lewis1= data.strip().split(",")
with open("Max.txt") as max:
    data= max.readline()
max1 = data.strip().split(",")
with open("vettel.txt") as vt:
    data = vt.readline()
vt1 = data.strip().split(",")


pure_lewis= []
pure_max= []
puer_vt=[]


"""
if there are -  . :, in the txt files we change it to : 
"""


def neat(time_lap):
    if "." in time_lap:
        separator = "."
    elif "-" in time_lap:
        separator = "-"
    else:
        return(time_lap)
    (minutes,seconds) = time_lap.split(separator)

    return(minutes+":"+seconds)

for i in lewis1:
    pure_lewis.append(neat(i))
for i in max1:
    pure_max.append(neat(i))
for i in vt1:
    puer_vt.append(neat(i))

"""
sort functions after organising data
"""
def sort ():
    for i in