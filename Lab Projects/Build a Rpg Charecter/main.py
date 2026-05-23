def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return "The character name should be a string"
    if name == "":
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"

    stats = [strength, intelligence, charisma]
    
    for s in stats:
        if type(s) is not int:
            return "All stats should be integers"

    for s in stats:
        if s < 1:
            return "All stats should be no less than 1"
            
    for s in stats:
        if s > 4:
            return "All stats should be no more than 4"

    if sum(stats) != 7:
        return "The character should start with 7 points"

    str_bar = "●" * strength + "○" * (10 - strength)
    int_bar = "●" * intelligence + "○" * (10 - intelligence)
    cha_bar = "●" * charisma + "○" * (10 - charisma)

    return f"{name}\nSTR {str_bar}\nINT {int_bar}\nCHA {cha_bar}"