import json
import ssl
import http.client

context = ssl._create_unverified_context()
conn = http.client.HTTPSConnection("football-web-pages1.p.rapidapi.com", context=context)

headers = {
    'x-rapidapi-key': "45dfc4c064msh14441388a82d595p138ec2jsn29e66be3c434",
    'x-rapidapi-host': "football-web-pages1.p.rapidapi.com"
}

# conn.request("GET", "/appearances.json?team=258", headers=headers)

# #Isthmian Premier Div is comp=11
# #Dulwich team=258
# res = conn.getresponse()
# data = res.read()
# # print(data.decode("utf-8"))

# parse_json = json.loads(data)

# # print(parse_json['appearances']['players'][])

# players = parse_json['appearances']['players']

# for player in players:
#     num_of_appearances = len(player['appearances'])
#     print(player['first-name'] + ' ' + player['last-name'])
#     print(num_of_appearances)
    

class Functions:

#generates a menu to select a team
    def team_picker():
        conn.request("GET", "/teams.json?comp=11", headers=headers)

        res = conn.getresponse()
        data = res.read()

        teams_json = json.loads(data)
        teams = teams_json['teams']

        teams_dict = {}

        for team in teams:
            teams_dict[team['full-name']] = team['id']
        #select a team from the list, store team id in a dict
        #get team id from dict using team as key
        #return team id for use in api link
        
        while True:
            team_key = input('''
Select your team from the Isthmian Premier League:
1.\tBillericay Town
2.\tBognor Regis Town
3.\tBowers & Pitsea
4.\tCanvey Island
5.\tCarshalton Athletic
6.\tChatham Town
7.\tCheshunt
8.\tChichester City
9.\tCray Valley PM
10.\tCray Wanderers
11.\tDartford
12.\tDover Athletic
13.\tDulwich Hamlet
14.\tFolkestone Invicta
15.\tHashtag United
16.\tHastings United
17.\tHendon
18.\tHorsham
19.\tLewes
20.\tPotters Bar Town
21.\tWhitehawk
22.\tWingate & Finchley

Please type the name of your team: 
''')
            if team_key in teams_dict:
                print(f'You have selected {team_key}!')
                user_team = teams_dict[team_key]
                menu_generator(user_team)  
            else:
                'Please choose from the available teams listed'
        


#generates a menu for the user to choose which option they require
def menu_generator(user_team):
    while True:
        menu = int(input('''
Select from one of the following options below:
1. Display your teams attendance figures
2. Display your teams form guide
3. Display your teams top goalscorer
4. Display your teams biggest win
5. Display your teams biggest loss
6. Display your teams league position over the season
7. Display your teams appearance statistics
8. Exit the programme

Make your selection: '''))
    
        #run if statements to execute menu functions
        if menu == 1:
            display_attendance(user_team)
        elif menu == 2:
            display_form_guide(user_team)
        elif menu == 3:
            display_top_scorers(user_team)
        elif menu == 4:
            display_big_win(user_team)
        elif menu == 5:
            display_big_loss(user_team)
        elif menu == 6:
            display_position_graph(user_team)
        elif menu == 7:
            display_appearances(user_team)
        elif menu == 8:
            exit()
        else:
            print('You have not selected a valid option, please choose a number between 1 and 7')
    

#function to display team attendance in a graph
def display_attendance(team):
    conn.request("GET", f"/attendances.json?team={team}", headers=headers)

    res = conn.getresponse()
    data = res.read()
    attendance_json = json.loads(data)

    print(attendance_json['attendances']['matches'])

    for game in attendance_json['attendances']['matches']:
        print(game['away-team']['name'])
        print(game['attendance'])
        print(game['date'])


#function to display last five match results
def display_form_guide(team):
    pass


#function to display top goalscorers in a bar chart
def display_top_scorers(team):
    pass


#function to display biggest win
def display_big_win(team):
    pass



#function to display biggest loss
def display_big_loss(team):
    pass


#function to display league position in line graph
def display_position_graph(team):
    pass


def display_appearances(team):
    conn.request("GET", f"/appearances.json?team={team}", headers=headers)

    #Isthmian Premier Div is comp=11
    #Dulwich team=258
    res = conn.getresponse()
    data = res.read()
    parse_json = json.loads(data)

    players = parse_json['appearances']['players']

    for player in players:
        num_of_appearances = len(player['appearances'])
        print(player['first-name'] + ' ' + player['last-name'])
        print(num_of_appearances)