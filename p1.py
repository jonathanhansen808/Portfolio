import csv

#Fifa19.csv is a csv file with the stats of all FIFA players

fifa_file = open('Fifa19.csv', encoding='utf-8')
file_reader = csv.reader(fifa_file)
player_data = list(file_reader)
fifa_file.close()
header = player_data[0]
player_data = player_data[1:]
for row in player_data:
    for idx in [2,4]:
        row[idx] = float(row[idx])
        
#Non-pandas version of loc

def cell(row_idx, col_name):
    col_idx = header.index(col_name)
    val = player_data[row_idx][col_idx]
    return val

#Manipulates strings of wages to standardize them across currencies

def transition(value):
    if value[-1].lower() == "m":
        stripped = value[1:-1]
        stripped_float = float(stripped)
        millions = stripped_float * 1000000
        return millions
    if value[-1].lower() == "k":
        k_stripped = value[1:-1]
        k_stripped_float = float(k_stripped)
        k_thousands = k_stripped_float * 100000
        return k_thousands
    if value[-1].isdigit():
        digit_stripped = value[1:]
        digit_stripped_float = float(digit_stripped)
        return digit_stripped_float
    else: 
        pass
    
def get_column(col_name):
    new_list = []
    for i in range(len(player_data)):
        if col_name == 7:
            [s[1:-1] for s in player_data]
        column = player_data[i][col_name]
        new_list.append(column)
    return new_list

def get_oldest_player_name(idx):
    oldest_age = 0
    name_oldest_age = 0
    for i in range(len(player_data)):
        row = player_data[i]
        age = row[idx]  
        if age > oldest_age:
            oldest_age = age
            max_idx = i
            name_oldest_age = player_data[max_idx][1]           
    return name_oldest_age

def get_highest_paid(idx):
    highest_paid = 0
    name_of_highest_val = " "
    for i in range(len(player_data)):
        row = player_data[i]
        val = transition(row[7])
        if val > highest_paid:
            highest_paid = val
            max_idx = i
            name_of_highest_val = player_data[max_idx][idx]
    return name_of_highest_val

def get_highest_val(col_idx):
    highest_val = 0
    for i in range(len(player_data)):
        row = player_data[i]
        val = transition(row[6])
        if val > highest_val:
            highest_val = val
            max_idx = i
            name_of_highest_val = player_data[max_idx][col_idx]
    return name_of_highest_val

#Returns dictionary with the stat categories and values for player by player name

def player_to_dict(name):
    for row in player_data:
        if row[1] == name:
            player_vals = row
            player_keys = header
            dic = {}
            for i in range(len(player_keys)):
                dic[player_keys[i]] = player_vals[i]
    return dic

#Returns the club the specified player plays for

def player_club(name):
    x = player_to_dict(name)
    return x.get("Club")

def fifa_avg(col_name):
    count = 0
    total = 0
    average = 0 
    net = get_column(col_name)
    for i in range(len(player_data)):
        total += net[i]
        count += 1 
    average = total / count 
    return average 

#Returns a count of the number of players playing for a specific country

def player_count(country):
    count = 0
    cols = get_column(3)
    for i in range(len(player_data)):
        if cols[i] == country:
            count += 1
    return(count)

#Returns dictionary with the stat categories and values for player by ID

def player_to_dict(player_id):
    for row in player_data:
        if int(row[0]) == player_id:
            player_vals = row
            player_keys = header
            dic = {}

            for i in range(len(player_keys)):
                dic[player_keys[i]] = player_vals[i]
    return dic

#Returns a dictionary with the countries as keys and the values being the amount of soccer players playing for that country 

def amount_of_players(column_idx):
    keys = list(set(get_column(column_idx)))
    dic = {}
    for i in keys:
        dic[i] = player_count(i)
    return dic

#Returns a dictionary with jersey numbers as key and the values being the amount of soccer players playing with that jersey number

def jersey():
    count = 0 
    cols = get_column(9)
    return cols

numbers = jersey()

def players_to_jersey(numbers):
    jersey_dict = {}
    for i in numbers:
        if i in jersey_dict:
            jersey_dict[i] += 1 
        else:
            jersey_dict[i] = 1
    return jersey_dict

#Returns a dictionary with jersey numbers being the keys and the average overall rating of all players with that jersey number as the value 

def avg_per_jersey(column_idx, variable):
    keys = list(set(get_column(column_idx)))
    new_dic = {}
    for jersey in keys:
        overall_jersey = 0
        player_overall = 0
        for row in player_data:
            if row[column_idx] == jersey:
                overall_jersey += row[variable]
                player_overall += 1
                new_dic[jersey] = overall_jersey/player_overall
    return new_dic

#Returns the highest rated jersey number from the dictionary created above

jerseys = avg_per_jersey(9,4)

def highest_avg_overall():
    best_jersey = None
    for jersey in jerseys:
        if best_jersey == None or jerseys[jersey] > jerseys[best_jersey]:
            best_jersey = jersey 
    return best_jersey