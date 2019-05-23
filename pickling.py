import pickle
from object_oriented import Racers
"""
function to open the text tiles, read the data inside the txt files
split them by their commas , and return accordingly to the pop() method.
Since Racers is a class-list. 
"""
def txt_files(text_files):
    try:
        with open(text_files) as f:
            readData = f.readline()
        temp = readData.strip().split(",")
        return (Racers(temp.pop(0),temp.pop(0),temp)) # we pop(return) the racer name, team, and then the times.
    except IOError as err:
        print("File error" +(str(err)))


"""
putting/writing data into pickle 

"""

def pickling_Data(files):
    f1_Racers = {}

    for i in files:
        racers = txt_files(i)
        f1_Racers[racers.n] = racers
    try:
        with open("racers.pickle","wb") as racer_files:
            pickle.dump(f1_Racers,racer_files)
    except IOError as err:
        print("File Error" + str(err))
    return(f1_Racers)

"""
reading data from pickle 
"""

def reading_data():
    f1_Racers = {}

    try:
        with open("racers.pickle","rb") as racer_files:
            f1_Racers = pickle.load(racer_files)
    except IOError as err:
        print("File Error" + str(err))
    return (f1_Racers)


"""
the files that will go through the process
"""

file_racers= ["daniel_ricciardo.txt","lewis_hamilton.txt","pierre_gasly.txt","sebastian_vettel.txt"]
info = pickling_Data(file_racers)
print(info)

for i in info:
    print(info[i].n +" "+ info[i].t)

copy = reading_data()
for i in copy:
    print(copy[i].n +" ***team : "+ copy[i].t +"** best times: "+ str(copy[i].bestTimes()))
