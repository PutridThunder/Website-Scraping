from bs4 import BeautifulSoup
import requests
import pandas as pd

#####################################################################################################################

# Setup to collect all data from the site
# requests downloads the html, beautifulsoup parses it

site = 'https://www.scrapethissite.com/pages/forms/'
r = requests.get(site)
webtext = BeautifulSoup(r.text, 'html.parser')

#####################################################################################################################
# turns every class of name, wins and losses,
# (they are the hockey team names, wins and losses)
# into seperate lists

Teams = [x.get_text().strip(" \n") for x in webtext.find_all(class_= 'name')]
Vic = [x.get_text().strip(" \n") for x in webtext.find_all(class_= 'wins')]
Los = [x.get_text().strip(" \n") for x in webtext.find_all(class_= 'losses')]

#####################################################################################################################

# using a dictionary is a common way to display information with pandas
# put all the information into a dictionary, all the columns will already be named
# add in index to give out custom indexes

Dict = {'Names': Teams, 'Wins': Vic, 'Losses':Los}
frame = pd.DataFrame(Dict, index=[f'Team {x+1}' for x in range(len(Dict['Names']))])

print('Before:')
print(frame)
print('\n\n#########################################################\n\n')

#####################################################################################################################

# calculate the win-loss precentages of each team
# as well as merging each team's information into a single list
# the new list being a list of tuples

TeamsData = []

def gamestats(win, los):
    totalplays = int(win) + int(los)
    return round(int(win)/totalplays, 2)

for i,x,y in zip(Teams,Vic, Los):
    st = gamestats(x,y)
    print(f'{i.upper()} has a winrate of {st} with {x} WINS {y} LOSSES')
    TeamsData.append((st, i, x, y))
print('\n\n#########################################################\n\n')

#####################################################################################################################

# organising the single list by hightst to lowest winrate
# moving all the tuples around, which holds
# the names and all other information of each team
# reprinting everything to see the difference
# between when it was first given to us and
# after we organised it all

TeamsData.sort(reverse=True)

print('After:')
print(pd.DataFrame(TeamsData, index=[f'Team {x+1}' for x in range(len(TeamsData))], columns=['Winrate', 'Teams', 'Wins', 'Losses']))
print('\n\n#########################################################\n\n')

for i in range(len(TeamsData)):
    print(f'{str(TeamsData[i][1]).upper()} has a winrate of {TeamsData[i][0]} with {TeamsData[i][2]} wins and {TeamsData[i][3]} losses')

print('\n\n#########################################################')
