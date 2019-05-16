"""

function to open data ,reads  and separates by commas

"""
def readD(textfile):

    try:
        with open(textfile) as text_file:
            data = text_file.readline()
        return (data.strip().split(","))
    except IOError as error:
        print("File Error" +str(error))



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


"""
sort functions after organising data , and print 
"""

lewis=readD("Lewis.txt")

max=readD("Max.txt")

vtl=readD("vettel.txt")



print(sorted(set([neat(i) for i in lewis]))[0:3])
print(sorted(set([neat(i) for i in max]))[0:3])
print(sorted(set([neat(i) for i in vtl]))[0:3])



