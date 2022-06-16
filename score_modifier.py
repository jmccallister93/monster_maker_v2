def calculate_score_modifier(ability_score):
    keys = []
    values = []

    score = 0
    for s in range(0, 31, 2): #Loop through every other value 0-30 for score
        keys.append(str(s))

    modifier = -6
    for m in range(16): #Loop through every value to get modifier 
        modifier = modifier + 1
        values.append(str(modifier))

    modifier_dict = dict(zip(keys,values))

    for ability_score in modifier_dict:
        if ability_score == "1" or ability_score == "2":
            print(modifier_dict[ability_score])
        elif ability_score == "3" or ability_score == "4":
            print(modifier_dict[ability_score])

    return modifier_dict

ability_score = 4
calculate_score_modifier(ability_score)
