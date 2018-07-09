
def teams(input_lines):
    return_list = []
    for i in range(len(input_lines)):
        return_list.append(input_lines[i][0])
        return_list.append(input_lines[i][2])
    return return_list

def get_team_names(input_lines):
    return set(teams(input_lines))


def count_amount_of_games(input_lines, team):
    return teams(input_lines).count(team)

def count_winnings(input_lines, team):
    winnings = 0
    for line in input_lines:
        if team in line:
            if team == line[0]:
                if line[1] > line[3]:
                    winnings += 1
            else:
                if line[3] > line[1]:
                    winnings += 1
    return winnings

def count_of_loses(input_lines, team):
    loses = 0
    for line in input_lines:
        if team in line:
            if team == line[0]:
                if line[1] < line[3]:
                    loses += 1
            else:
                if line[3] < line[1]:
                    loses += 1
    return loses

def count_of_draws(input_lines, team):
    draws = 0
    for line in input_lines:
        if team in line:
                if line[1] == line[3]:
                    draws += 1
    return draws

def count_credits(input_lines, team):
    wins = int(count_winnings(input_lines, team))
    loses = int(count_of_loses(input_lines, team))
    draws = int(count_of_draws(input_lines, team))
    return (wins*3 + loses*0 + draws*1)


if __name__ == '__main__':
    num_of_games = input()
    input_lines = list(input().split(";") for i in range(int(num_of_games)))
    for i in get_team_names(input_lines):
        print(i+":", count_amount_of_games(input_lines, i), count_winnings(input_lines, i),
              count_of_draws(input_lines, i), count_of_loses(input_lines, i),
              count_credits(input_lines, i), sep=" ")
