# sports statistics - lesosn 317 (18/06/25)

# Stores overall goals scored, overall goals conceded and number of games played
# Calculates goal difference
# If they played 10 games, calculate the average goals per game
# Display all relevant statistics

overallgoals = int(input("how many goals were scored overall?: "))
concededgoals = int(input("how many goals were conceded?: ")) # goals for the other team
numberofgames = int(input("how many games were played?: "))

myteamgoals = overallgoals - concededgoals

if numberofgames == 10:
    average = overallgoals / numberofgames
    print("average number of goals scored per game: ", average)

print("overall goals: ", overallgoals)
print("overall games by team: ", myteamgoals)
print("overall goals conceded: ", concededgoals) 
print("number of games: ", numberofgames)