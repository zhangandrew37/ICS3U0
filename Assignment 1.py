# For a list of learning goals and success criteria for this assignment, please see
# this link: https://github.com/mrseidel-classes/ICS3U/wiki/Python-Assignment-1

# -----------------------------------------------------------------------------
# Name:        Assignment 1
# Purpose:     Allows user to build a complete character for Pathfinder Second Edition
#
# Author:      628333
# Created:     24-Oct-2019
# Updated:     26-Oct-2019
# -----------------------------------------------------------------------------
# TODO
# - format print the --> aligned left [equipment           cost] <-- aligned right
# - write print message for background
# - ability boosts (after background
# - class feats + skill feats ???
# - buying items with gp (use dictionary)

# -----------------------------------Classes and Functions used throughout the code-------------------------------------


# stores information about codes for text styles/colours
class TextStyle:  # stored in a class for organization
    bold = '\033[1m'
    underline = '\033[4m'
    reset = '\033[0m'
    italics = '\033[3m'
    green = '\033[92m'
    red = '\033[91m'


# stores the character's information/attributes
class CharacterInformation:
    name = ''
    age = ''
    height = ''
    ancestry = ''
    heritage = ''
    ancestryFeat = ''
    background = ''
    characterClass = ''
    classFeat = ''
    equipment = []
    abilityBoosts = []
    abilityFlaws = []
    stats = {"Hit Points": 0, "Size": "", "Speed": 0}
    abilityScores = {"Strength": 10, "Dexterity": 10, "Constitution": 10, "Intelligence": 10, "Wisdom": 10, "Charisma": 10,}


# returns user's final input for the character's background
def anyInput(*options):
    while True:  # runs until user input is in the list of options
        anyChoice = input("Selection: ")
        choices = [*options]

        # user confirmation of their input selection
        def confirm(functionName):
            print("Confirm? (Y/N)")

            while True:  # runs until user input is correct
                userInput = input()
                if userInput.upper() == 'Y':
                    print("Selection has been saved.")
                    break
                elif userInput.upper() == 'N':
                    return functionName(*options)
                else:
                    print("Sorry, that was an invalid input. Try again")

        if anyChoice.upper() in choices:
            confirm(anyInput)
            return anyChoice.upper()
            break

        else:
            print("Sorry, that was an invalid input. Try again.")


# ---------------------------------------------------Introduction-------------------------------------------------------

# introducing the program
print("Welcome to Buildrew™ - A Pathfinder Second Edition character builder.")
print()  # organization of output

# creating an account
print(TextStyle.underline + "Create an Account" + TextStyle.reset)
username = input("Username: ")
password = input("Password: ")
print()  # organization of output
print("Hello, " + username + "!")
print("Let's start building your character.")
print()  # organization of output


# -----------------------------------------------------Ancestry---------------------------------------------------------

# lists the choices available for the character's ancestry
print('\033[0m' + "Please input your character's ancestry" + TextStyle.reset)
print("A - Dwarf")
print("B - Elf")
print("C - Gnome")
print("D - Goblin")
print("E - Halfling")
print("F - Human")
print()  # organization of output

# takes in user input for ancestry choice
finalAncestryInput = anyInput('A', 'B', 'C', 'D', 'E', 'F')

# converts the user's input into the appropriate ancestry
ancestryChoices = {
    "A": "Dwarf",
    "B": "Elf",
    "C": "Gnome",
    "D": "Goblin",
    "E": "Halfling",
    "F": "Human"
}
CharacterInformation.ancestry = ancestryChoices[finalAncestryInput.upper()]
print()  # organization of output


# ------------------------------------------------------Heritage--------------------------------------------------------

# user input for heritage choice
print(TextStyle.bold + "Next, input your character's heritage" + TextStyle.reset)

dwarfHeritageChoices = {
    'A': "Ancient-Blooded Dwarf",
    'B': "Anvil Dwarf",
    'C': "Death Warden Dwarf",
    'D': "Elemental Heart Dwarf",
    'E': "Forge Dwarf",
    'F': "Oathkeeper Dwarf",
    'G': "Rock Dwarf",
    'H': "Strong-blooded Dwarf"
}

elfHeritageChoices = {
    'A': "Ancient Elf",
    'B': "Arctic Elf",
    'C': "Cavern Elf",
    'D': "Desert Elf",
    'E': "Seer Elf",
    'F': "Whisper Elf",
    'G': "Woodland Elf",
}

gnomeHeritageChoices = {
    'A': "Chameleon Gnome",
    'B': "Fey-Touched Gnome",
    'C': "Sensate Gnome",
    'D': "Umbral Gnome",
    'E': "Vivacious Gnome",
    'F': "Wellspring Gnome"
}

goblinHeritageChoices = {
    'A': "Charhide Goblin",
    'B': "Irongut Goblin",
    'C': "Razortooth Goblin",
    'D': "Snow Goblin",
    'E': "Tailed Goblin",
    'F': "Treedweller Goblin",
    'G': "Unbreakable Goblin"
}

halflingHeritageChoices = {
    'A': "Gutsy Halfling",
    'B': "Hillock Halfling",
    'C': "Nomadic Halfling",
    'D': "Twilight Halfling",
    'E': "Wildwood Halfling"
}

humanHeritageChoices = {
    'A': "Skilled Heritage",
    'B': "Versatile Heritage",
    'C': "Wintertouched Heritage"
}

# adds appropriate statistics to the character
# saves user input for the character's heritage
if CharacterInformation.ancestry == 'Dwarf':
    CharacterInformation.stats["Hit Points", "Size", "Speed"] = 10, "Medium", 20
    print("A - Ancient-Blooded Dwarf")
    print("B - Anvil Dwarf")
    print("C - Death Warden Dwarf")
    print("D - Elemental Heart Dwarf")
    print("E - Forge Dwarf")
    print("F - Oathkeeper Dwarf")
    print("G - Rock Dwarf")
    print("H - Strong-blooded Dwarf")
    print()  # organization of output
    finalHeritageInput = anyInput('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
    CharacterInformation.heritage = dwarfHeritageChoices[finalHeritageInput]

elif CharacterInformation.ancestry == 'Elf':
    CharacterInformation.stats["Hit Points", "Size", "Speed"] = 6, "Medium", 30
    print("A - Ancient Elf")
    print("B - Arctic Elf")
    print("C - Cavern Elf")
    print("D - Desert Elf")
    print("E - Seer Elf")
    print("F - Whisper Elf")
    print("G - Woodland Elf")
    print()  # organization of output
    finalHeritageInput = anyInput('A', 'B', 'C', 'D', 'E', 'F', 'G')
    CharacterInformation.heritage = dwarfHeritageChoices[finalHeritageInput]

elif CharacterInformation.ancestry == 'Gnome':
    CharacterInformation.stats["Hit Points", "Size", "Speed"] = 8, "Small", 25
    print("A - Chameleon Gnome")
    print("B - Fey-Touched Gnome")
    print("C - Sensate Gnome")
    print("D - Umbral Gnome")
    print("E - Vivacious Gnome")
    print("F - Wellspring Gnome")
    print()  # organization of output
    finalHeritageInput = anyInput('A', 'B', 'C', 'D', 'E', 'F')
    CharacterInformation.heritage = dwarfHeritageChoices[finalHeritageInput]

elif CharacterInformation.ancestry == 'Goblin':
    CharacterInformation.stats["Hit= Points", "Size", "Speed"] = 6, "Small", 25
    print("A - Charhide Goblin")
    print("B - Irongut Goblin")
    print("C - Razortooth Goblin")
    print("D - Snow Goblin")
    print("E - Tailed Goblin")
    print("F - Treedweller Elf")
    print("G - Unbreakable Goblin")
    print()  # organization of output
    finalHeritageInput = anyInput('A', 'B', 'C', 'D', 'E', 'F', 'G')
    CharacterInformation.heritage = dwarfHeritageChoices[finalHeritageInput]

elif CharacterInformation.ancestry == 'Hafling':
    CharacterInformation.stats["Hit Points", "Size", "Speed"] = 6, "Small", 25
    print("A - Gutsy Halfling")
    print("B - Hillock Halfling")
    print("C - Nomadic Halfling")
    print("D - Twilight Halfling")
    print("E - Wildwood Halfling")
    print()  # organization of output
    finalHeritageInput = anyInput('A', 'B', 'C', 'D', 'E', 'F', 'E')
    CharacterInformation.heritage = dwarfHeritageChoices[finalHeritageInput]

elif CharacterInformation.ancestry == 'Human':
    CharacterInformation.stats["Hit Points", "Size", "Speed"] = 8, "Medium", 25
    print("A - Skilled Heritage")
    print("B - Versatile Heritage")
    print("C - Wintertouched Heritage")
    finalHeritageInput = anyInput('A', 'B', 'C', 'D', 'E', 'F', 'C')
    print()  # organization of output
    CharacterInformation.heritage = dwarfHeritageChoices[finalHeritageInput]

# ----------------------------------------------------Background--------------------------------------------------------

# taking user input for the character's background
# Note: does not list all choices due to the immense amount.
print()  # organization of output
print(TextStyle.bold + "Now, input your character's background" + TextStyle.reset)
print(TextStyle.italics + "Note: Choices are not listed due to the immense amount.")
print(TextStyle.italics + "=>Please refer to a pathfinder 2e guide OR")
print(TextStyle.italics + "the code (Lines 255-357)" + TextStyle.reset)
print()  # organization of output
finalBackgroundInput = anyInput(
    "ACADEMIC",
    "ACOLYTE",
    "ACROBAT",
    "ADHERENT",
    "ANIMAL WHISPERER",
    "ARCHAEOLOGIST",
    "ARTIFACT SEEKER",
    "ARTISAN",
    "ARTIST",
    "ASPIRING FREE CAPTAIN",
    "ASPIRING RIVER MONARCH",
    "BARKEEP",
    "BARRISTER",
    "BLACK MARKET SMUGGLER",
    "BOUNTY HUNTER",
    "BRIGHT LION",
    "CHARLATAN",
    "CHARMER",
    "CHILD OF SQUALOR",
    "CHILD OF THE CITY",
    "CRIMINAL",
    "CRUSADER",
    "CURSED FAMILY",
    "DESERT TRACKER",
    "DETECTIVE",
    "EMISSARY",
    "ENTERTAINER",
    "EXPATRIATE",
    "FAITHFUL",
    "FARMHAND",
    "FIELD MEDIC",
    "FOLLOWER",
    "FORTUNE TELLER",
    "FREED SLAVE",
    "GAMBLER",
    "GLADIATOR",
    "GOBLINBLOOD ORPHAN",
    "GRAND COUNCIL BUREAUCRAT",
    "GUARD",
    "GUERRILLA",
    "HERBALIST",
    "HERMIT",
    "HOPEFUL",
    "HUNTER",
    "INLANDER",
    "LABORER",
    "LOYALIST",
    "LUMBERJACK",
    "MAMMOTH SPEAKER",
    "MANTIS SCION",
    "MARTIAL DISCIPLE",
    "MENAGERIE DUNG SWEEPER",
    "MERCENARY",
    "MERCHANT",
    "MINER",
    "MYSTIC",
    "NAME - BEARER",
    "NOBLE",
    "NOMAD",
    "ONYX TRADER",
    "OOZE - TENDER",
    "PARTISAN",
    "PEARL DIVER",
    "PERFECTION SEEKER",
    "PRESS - GANGED",
    "PRISONER",
    "PRODIGY",
    "PURVEYOR OF THE BIZARRE",
    "QUICK",
    "RAIDER",
    "RANCHER",
    "REBEL",
    "RECLAIMER",
    "REFORMER",
    "REFUGEE",
    "RESTORER",
    "SAILOR",
    "SCAVENGER",
    "SCHEMER",
    "SCHOLAR",
    "SCHOLAR OF THE ANCIENTS",
    "SCION",
    "SCOUT",
    "SECULAR MEDIC",
    "SHADOW HAUNTED",
    "SLAYER",
    "SMUGGLER",
    "STORM SURVIVOR",
    "STREET URCHIN",
    "SURVIVOR",
    "TINKER",
    "TRADE CONSORTIUM UNDERLING",
    "TRAVELER",
    "UNDERSEA ENTHUSIAST",
    "UNIFIER",
    "WANDERER",
    "WARRIOR",
    "WAVETOUCHED",
    "WILDBORNE",
    "WINTER’S CHILD",
    "WITCH WARY",
    "WONDER TASTER"
)
CharacterInformation.background = finalBackgroundInput


# ---------------------------------------------------------Class--------------------------------------------------------

# user input for class choice
print()  # organization of output
print("Please input your character's class")
print("A - Alchemist")
print("B - Barbarian")
print("C - Bard")
print("D - Champion")
print("E - Cleric")
print("F - Druid")
print("G - Fighter")
print("H - Monk")
print("I - Ranger")
print("J - Rogue")
print("K - Sorcerer")
print("L - Wizard")
print()  # organization of output

finalClassInput = anyInput('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L')
classChoices = {
    "A": "Alchemist",
    "B": "Barbarian",
    "C": "Bard",
    "D": "Champion",
    "E": "Cleric",
    "F": "Druid",
    "G": "Fighter",
    "H": "Monk",
    "I": "Ranger",
    "J": "Rogue",
    "K": "Sorcerer",
    "L": "Wizard"
}
CharacterInformation.characterClass = classChoices[finalClassInput.upper()]


# -------------------------------------------------------Items----------------------------------------------------------

itemChoices = {

}

# (Post character creation) - User feedback
print()  # organization of output
print("Good job! You have completed your character.")
print("Thank you for using Buildrew™. Would you like to rate your experience? (Y/N)")
while True:
    rateInput = input()
    if rateInput.upper() == 'Y':
        print("Please give a rating from 1-5.")
        print("1 - Didn't work at all")
        print("2 - Confusing")
        print("3 - Not bad, but not great either")
        print("4 - Worked well, but bumped into some problems")
        print("5 - Excellent! Would use again.")
        while True:
            try:
                rating = int(input("Rating: "))
                if rating == 1 or rating == 2 or rating == 3 or rating == 4 or rating == 5:
                    for i in range(int(rating)):
                        print(TextStyle.green + '★', end = '')
                    for i in range(5 - int(rating)):
                        print(TextStyle.red + '☆' + TextStyle.reset, end = '')
                    break
                else:
                    print("Sorry, please input an integer between 1 to 5")
            except ValueError:
                print("Sorry, please input an integer between 1 to 5")
        print()  # organization of output
        print(TextStyle.reset + "Thank you. Your feedback is greatly appreciated!")
        break
    elif rateInput.upper() == 'N':
        print("No problem! Have fun!")
    else:
        print("Sorry, that was an invalid input. Try again")
