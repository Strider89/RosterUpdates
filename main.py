import csv

roster1_data = {}
roster2_data = {}

additions = []
terminations = []
day_changes = {}

with open('roster1.csv') as old_roster:
    reader = csv.DictReader(old_roster)
    for row in reader:
        roster1_data.update({row['Name'] : row['Days']})

print(roster1_data)

with open('roster2.csv') as new_roster:
    reader = csv.DictReader(new_roster)
    for row in reader:
        roster2_data.update({row['Name'] : row['Days']})

#print(roster2_data)

def find_additions(roster1,roster2):
    for person in roster2:
        if person not in roster1:
            additions.append(person)

def find_terminations(roster1,roster2):
    for person in roster1:
        if person not in roster2:
            terminations.append(person)


def find_day_changes(roster1,roster2):
    differences = roster2.items() - roster1.items()
    #print(differences)
    for item in differences:
        print(item)

    
    






find_additions(roster1_data,roster2_data)
#print("Added: ", Additions)
find_terminations(roster1_data,roster2_data)
#print("Terminated: ", Terminations)
find_day_changes(roster1_data,roster2_data)





        







        
       
