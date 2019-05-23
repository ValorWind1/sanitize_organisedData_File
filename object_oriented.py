class Racers(list):
    def __init__(self,the_name,teams,lap_time=[]):
        list.__init__([])
        self.n = the_name
        self.t = teams
        self.extend(lap_time)

    def bestTimes(self):
        return(sorted(set([organize(i) for i in self]))[0:5])

def organize(time_lap):
    if "," in time_lap:
        punctuation = ","
    elif "." in time_lap:
        punctuation = "."
    elif "-" in time_lap:
        punctuation ="-"
    else:
        return(time_lap)
    (minute,seconds) = time_lap.split(punctuation)
    return (minute+":"+seconds)