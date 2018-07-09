number_of_lines = int(input())
dict_of_teams = {}
for i in range(number_of_lines):
    team1, sc1, team2, sc2 = input().split(";")
    if team1 not in dict_of_teams:
        dict_of_teams[team1] = {"plays": 0, "wins": 0, "draws": 0, "loses": 0, "score": 0}
    if team2 not in dict_of_teams:
        dict_of_teams[team2] = {"plays": 0, "wins": 0, "draws": 0, "loses": 0, "score": 0}
    if team1 in dict_of_teams:
        dict_of_teams[team1]["plays"] += 1
        if sc1 > sc2:
            dict_of_teams[team1]["wins"] += 1
            dict_of_teams[team2]["loses"] += 1
            dict_of_teams[team1]["score"] += 3
    if team2 in dict_of_teams:
        dict_of_teams[team2]["plays"] += 1
        if sc2 > sc1:
            dict_of_teams[team2]["wins"] += 1
            dict_of_teams[team1]["loses"] += 1
            dict_of_teams[team2]["score"] += 3
    if sc2 == sc1:
        dict_of_teams[team1]["draws"] += 1
        dict_of_teams[team2]["draws"] += 1
        dict_of_teams[team1]["score"] += int(dict_of_teams[team1]["draws"])
        dict_of_teams[team2]["score"] += int(dict_of_teams[team2]["draws"])


for team in dict_of_teams:
    print(team, dict_of_teams[team]["plays"],
                dict_of_teams[team1]["wins"],
                dict_of_teams[team1]["draws"],
                dict_of_teams[team1]["loses"],
                dict_of_teams[team2]["score"],
                sep = " ")
