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

    if not all(isinstance(stat, int) for stat in stats):
        return "All stats should be integers"
    if any(stat < 1 for stat in stats):
        return "All stats should be no less than 1"
    if any(stat > 4 for stat in stats):
        return "All stats should be no more than 4"
    if sum(stats) != 7:
        return "The character should start with 7 points"

    def format_line(label, value):
        full_dots = '●' * value
        empty_dots = '○' * (10 - value)
        return f"{label} {full_dots}{empty_dots}"

    character_sheet = (
        f"{name}\n"
        f"{format_line('STR', strength)}\n"
        f"{format_line('INT', intelligence)}\n"
        f"{format_line('CHA', charisma)}"
    )

    return character_sheet

print(create_character('ren', 4, 2, 1))

