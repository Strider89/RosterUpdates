import csv


def create_dicts(csv_file):
    roster_data = {}
    with open(csv_file) as new_roster:
        reader = csv.DictReader(new_roster)
        for row in reader:
            roster_data.update({row['Name'] : row['Days']})
    return roster_data

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
    for name in same_keys:
        if roster1.get(name) != roster2.get(name):
            day_changes.update({name : roster2.get(name) })
    return day_changes


def create_report_terminal(additions,terminations,day_changes):
    print("The following students were added:")
    for person in additions:
        print(str(person) + " is new to the roster")
    print("The following students were terminated:")
    for person in terminations:
        print(str(person) + " is terminated from the roster")
    print("The follwing students changed their days:")
    for key in day_changes:
        if day_changes.get(key) == 'M':
            print(str(key) + " days changed to Monday")
        elif day_changes.get(key) == 'MT':
            print(str(key) + " days changed to Monday, Tuesday")
        elif day_changes.get(key) == 'MTW':
            print(str(key) + " days changed to Monday, Tuesday, Wednesday")
        elif day_changes.get(key) == 'MTWThu':
            print(str(key) + " days changed to Monday, Tuesday, Wednesday, Thursday")
        else:
            print(str(key) + " days changed to Monday, Tuesday, Wednesday, Thursday, Friday")

def create_file_report(additions, terminations, day_changes):
    with open('Roster_Report.txt', 'w') as report:
        for person in additions:
            report.write(str(person) + " is new to the roster \n")
        for person in terminations:
            report.write(str(person) + " is terminated from the roster \n")
        for key in day_changes:
            if day_changes.get(key) == 'M':
                report.write(str(key) + " days changed to Monday \n")
            elif day_changes.get(key) == 'MT':
                report.write(str(key) + " days changed to Monday, Tuesday \n")
            elif day_changes.get(key) == 'MTW':
                report.write(str(key) + " days changed to Monday, Tuesday, Wednesday \n")
            elif day_changes.get(key) == 'MTWThu':
                report.write(str(key) + " days changed to Monday, Tuesday, Wednesday, Thursday \n")
            else:
                report.write(str(key) + " days changed to Monday, Tuesday, Wednesday, Thursday, Friday \n")




        

roster1 = create_dicts('roster1.csv')
roster2 = create_dicts('Roster2.csv')

additions = find_changes(roster2,roster1)
#print("Additions: ",additions)
terminations = find_changes(roster1,roster2)
#print("Terminations: ",terminations)
day_changes = find_day_changes(roster1,roster2)
#print("Day Changes", day_changes)

create_report_terminal(additions,terminations,day_changes)

create_file_report(additions,terminations,day_changes)













        







        
       
