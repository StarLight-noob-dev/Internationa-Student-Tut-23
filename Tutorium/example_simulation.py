import random as r

class People:
    def __init__(self, n:str, l:str, s:float) -> None:
        self.name = n
        self.last = l
        self.sentiment = s

class City:
    def __init__(self, name:str, people:list[People]) -> None:
        self.name = name
        self.population = people

    def get_avg(self)->float:
        avg = 0.0
        
        for x in self.population:
            avg += x.sentiment

        return round((avg/len(self.population)),2)
    

def main():

    names = ["James", "Mary","Robert","Patricia","John","Jennifer","Michael","Linda","David","Elizabeth","William","Barbara","Richard"]
    last = ["Carlos","Rom","Luck","Water","Rohan","Manfred"]

    people = [People(n,l,round(r.random()*100,2)) for n,l in zip(names, last)]

    for x in people:
        print(x.name)

    frankfurt = City("Frankfurt", people)

    leave = r.random()*100
    stay = r.randint(50, 60)
    
    for person in frankfurt.population:
        if person.sentiment < leave:
            #person leaves else stays
            pass
    
    if frankfurt.get_avg() > stay:
        # Add new people to city
        pass

    return

main()