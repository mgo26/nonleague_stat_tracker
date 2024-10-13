#generates a menu to select a team
def team_picker():
    pass


#generates a menu for the user to choose which option they require
def menu_generator():
    while True:
        menu = input('''
Select from one of the following options below:
1. Display your teams attendance figures
2. Display your teams form guide
3. Display your teams top goalscorer
4. Display your teams biggest win
5. Display your teams biggest loss
6. Display your teams league position over the season
7. Exit the programme

Make your selection: ''')
        
        #run if statements to execute menu functions
        if menu == 1:
            display_attendance()
        elif menu == 2:
            display_form_guide()
        elif menu == 3:
            display_top_scorers()
        elif menu == 4:
            display_big_win()
        elif menu == 5:
            display_big_loss()
        elif menu == 6:
            display_position_graph()
        elif menu == 7:
            exit()
        else:
            print('You have not selected a valid option, please choose a number between 1 and 7')
    

#function to display team attendance in a graph
def display_attendance(team):
    pass


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


menu_generator()