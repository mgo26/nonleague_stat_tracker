import json
import ssl
import http.client
import matplotlib.pyplot as plt

context = ssl._create_unverified_context()
conn = http.client.HTTPSConnection("football-web-pages1.p.rapidapi.com", context=context)

headers = {
    'x-rapidapi-key': "45dfc4c064msh14441388a82d595p138ec2jsn29e66be3c434",
    'x-rapidapi-host': "football-web-pages1.p.rapidapi.com"
}


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
                team_name = team_key
                menu_generator(user_team, team_name)  
            else:
                'Please choose from the available teams listed'
        


#generates a menu for the user to choose which option they require
def menu_generator(user_team, team_name):
    while True:
        menu = int(input('''
Select from one of the following options below:
1. Display your teams attendance figures
2. Display your teams form guide
3. Display your teams top five goalscorers
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
            display_form_guide(user_team, team_name)
        elif menu == 3:
            display_top_scorers(user_team)
        elif menu == 4:
            display_big_win(user_team, team_name)
        elif menu == 5:
            display_big_loss(user_team, team_name)
        elif menu == 6:
            display_position_graph(user_team, team_name)
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

    for game in attendance_json['attendances']['matches']:
        print(game['away-team']['name'])
        print(game['attendance'])
        print(game['date'])


#function to display last six match results
def display_form_guide(team, team_name):
    conn.request("GET", f"/form-guide.json?team={team}", headers=headers)
    res = conn.getresponse()
    data = res.read()
    form_json = json.loads(data)

    form_guide = []
    for form_team in form_json['form-guide']['teams']:
        if form_team['id'] == team:
            team_form_guide = form_team
            
    for match in team_form_guide['matches']:
        if match['home-team']['name'] == team_name:
            if match['home-team']['score'] > match['away-team']['score']:
                match['result'] = 'W'
            elif match['home-team']['score'] == match['away-team']['score']:
                match['result'] = 'D'
            else:
                match['result'] = 'L'
        else:
            if match['home-team']['score'] > match['away-team']['score']:
                match['result'] = 'L'
            elif match['home-team']['score'] == match['away-team']['score']:
                match['result'] = 'D'
            else:
                match['result'] = 'W'         
    
    #Seperate loop to ensure the results are added in the correct order and cleaner code    
    for match in team_form_guide['matches']:
        form_guide.append(match['result'])
        
    print(' '.join(form_guide))


#function to display top goalscorers in a bar chart
def display_top_scorers(team):
    conn.request("GET", f"/goalscorers.json?comp=11&team={team}", headers=headers)
    res = conn.getresponse()
    data = res.read()
    goalscorers = json.loads(data)

    for player in goalscorers['goalscorers']['players']:
        goal_counter = 0
        for game in player['goals']:
            if game['match']['competition']['id'] == 11:
                goal_counter += 1
        
        if goal_counter == 1:   
            print(f"{player['first-name']} {player['last-name']} has scored {goal_counter} goal this season.")
        else:
            print(f"{player['first-name']} {player['last-name']} has scored {goal_counter} goals this season.")


#function to display biggest win
def display_big_win(team, team_name):
    
    conn.request("GET", f"/records.json?team={team}", headers=headers)
    res = conn.getresponse()
    data = res.read()
    records = json.loads(data)

    for record in records['records']['records']:
        if record['description'] == 'Biggest Victory' and record['type'] == 'All Matches':
            if record['matches'][0]['home-team']['id'] == team:
                home_score = record['matches'][0]['home-team']['score']
                away_score = record['matches'][0]['away-team']['score']
                opposition = record['matches'][0]['away-team']['name']
                print(f'{team_name} defeated {opposition} {home_score} - {away_score}')
            else:
                home_score = record['matches'][0]['home-team']['score']
                away_score = record['matches'][0]['away-team']['score']
                opposition = record['matches'][0]['home-team']['name']
                print(f'{team_name} defeated {opposition} {away_score} - {home_score}')



#function to display biggest loss
def display_big_loss(team, team_name):
    conn.request("GET", "/records.json?team=258", headers=headers)
    res = conn.getresponse()
    data = res.read()
    records = json.loads(data)

    for record in records['records']['records']:
        if record['description'] == 'Heaviest Defeat' and record['type'] == 'All Matches':
            if record['matches'][0]['home-team']['id'] == team:
                home_score = record['matches'][0]['home-team']['score']
                away_score = record['matches'][0]['away-team']['score']
                opposition = record['matches'][0]['away-team']['name']
                print(f'{team_name} lost to {opposition} {away_score} - {home_score}')
            else:
                home_score = record['matches'][0]['home-team']['score']
                away_score = record['matches'][0]['away-team']['score']
                opposition = record['matches'][0]['home-team']['name']
                print(f'{team_name} lost to {opposition} {home_score} - {away_score}')

#function to display league position in line graph
def display_position_graph(team, team_name):
    conn.request("GET", f"/league-progress.json?team={team}", headers=headers)
    res = conn.getresponse()
    data = res.read()
    league_progress = json.loads(data)

    league_position = []
    games_played = []

    for game in league_progress['league-progress']['progress']:
        league_position.append(game['position'])
        games_played.append(game['played'])
        

    fig, ax = plt.subplots()
    ax.plot(games_played, league_position, linewidth=3)

    #Set title and label axes
    ax.set_title(f'League Position of {team_name} over time', fontsize=24)
    ax.set_xlabel('Games played', fontsize=14)
    ax.set_ylabel('League Position', fontsize=14)
    # ax.set_xticklabels(games_played.astype(int))

    #set the size of tick labels
    ax.tick_params(labelsize=14)

    plt.gca().invert_yaxis()

    plt.show()


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
        
        
#function to check if user wants to return to main menu
def back_to_menu():
    pass