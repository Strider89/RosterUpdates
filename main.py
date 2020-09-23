import csv


def create_dicts(csv_file):
    roster_data = {}
    with open(csv_file) as new_roster:
        reader = csv.DictReader(new_roster)
        for row in reader:
            roster_data.update({row['Name'] : row['Days']})
    return roster_data

def find_additions(roster1,roster2):
    additions = []
    for person in roster2:
        if person not in roster1:
            additions.append(person)
    return additions

def find_terminations(roster1,roster2):
    terminations = []
    for person in roster1:
        if person not in roster2:
            terminations.append(person)
    return terminations

#change order of roster parameters for additions and terminations
def find_changes(roster1,roster2):
    changes = []
    for person in roster1:
        if person not in roster2:
            changes.append(person)
    return changes

def find_day_changes(roster1,roster2):
    day_changes = {}
    same_keys = roster1.keys() & roster2.keys()
    #print(same_keys)
    for name in same_keys:
        #print(roster1.get(name))
        #print(roster2.get(name))
        if roster1.get(name) != roster2.get(name):
            #print(name)
            #print(roster2.get(name))
            day_changes.update({name : roster2.get(name) })
    return day_changes

roster1 = create_dicts('roster1.csv')
roster2 = create_dicts('Roster2.csv')

additions = find_changes(roster1,roster2)
print(additions)
terminations = find_changes(roster2,roster1)
print(terminations)
day_changes = find_day_changes(roster1,roster2)
#print(day_changes)










        







        
       
