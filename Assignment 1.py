# For a list of learning goals and success criteria for this assignment, please see
# this link: https://github.com/mrseidel-classes/ICS3U/wiki/Python-Assignment-1

# -----------------------------------------------------------------------------
# Name:        Assignment 1
# Purpose:     Allows user to build a complete character for Pathfinder Second Edition
#
# Author:      628333
# Created:     24-Oct-2019
# Updated:     1-Nov-2019
# -----------------------------------------------------------------------------

# Note: It is recommended that you run the program with the console covering approximately half the screen


# stores information about codes for text styles/colours
class TextStyle:  # stored in a class for organization
    bold = '\033[1m'
    underline = '\033[4m'
    reset = '\033[0m'
    italics = '\033[3m'
    green = '\033[92m'
    red = '\033[91m'


# stores the character's attributes
class CharacterInformation:  # stored in a class for organization
    name = ''
    age = 0
    height = 0
    ancestry = ''
    heritage = ''
    ancestryFeat = ''
    background = ''
    characterClass = ''
    spell = 'None'
    items = []
    stats = {"Hit Points": 0, "Size": "", "Speed": 0}
    abilityScores = {"Strength": 10, "Dexterity": 10, "Constitution": 10, "Intelligence": 10, "Wisdom": 10, "Charisma": 10, }

# returns user's final input with confirmation
def anyInput(*options):
    while True:  # runs until user input is in the list of options
        anyChoice = input("Selection: ")
        choices = [*options]

        def confirm(functionName):
            print("Confirm? (Y/N)")

            while True:  # runs until user input is Y or N
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

        else:
            print("Sorry, that was an invalid input. Try again.")
            
# ---------------------------------------------------Introduction-------------------------------------------------------

print("Welcome to Buildrew™ - A Pathfinder Second Edition character builder.")
print()

# creating an account
print(TextStyle.underline + "Create an Account" + TextStyle.reset)
username = input("Username: ")
password = input("Password: ")
print()
print("Hello, " + username + "!")
print("Let's start building your character.")
print()

# --------------------------------------------------------Name----------------------------------------------------------

CharacterInformation.name = input("Please input your character's name: ")

# --------------------------------------------------------Age-----------------------------------------------------------

while True:
    try:
        age = int(input("Please input your character's age (yrs): "))
        if age>0:
            CharacterInformation.age = age
            break
        else:
            print("Sorry, you must input a positive integer as your character's age. Please try again.")
            continue
    except ValueError:
        print("Sorry, you must input an integer as your character's age. Please try again.")
        continue

# -------------------------------------------------------Height---------------------------------------------------------

while True:
    try:
        height = float(input("Please input your character's height (ft): "))
        if height>0:
            CharacterInformation.height = height
            break
        else:
            print("Sorry, you must input a positive integer as your character's height. Please try again.")
            continue
    except ValueError:
        print("Sorry, you must input an integer as your character's height. Please try again.")
        continue

# -----------------------------------------------------Ancestry---------------------------------------------------------

# lists the choices available for the character's ancestry
print()
print(TextStyle.bold + "Please input your character's ancestry" + TextStyle.reset)
print("A - Dwarf")
print("B - Elf")
print("C - Gnome")
print("D - Goblin")
print("E - Halfling")
print("F - Human")
print()

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
print()

# -------------------------------------------------Heritage choices-----------------------------------------------------
# converts input into the real heritage name

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

# ------------------------------------------Free ability boost choices--------------------------------------------------
# converts input into real ability boost name

freeBoostChoices = {
    'A': "Strength",
    'B': "Dexterity",
    'C': "Constitution",
    'D': "Intelligence",
    'E': "Wisdom",
    'F': "Charisma"
}

# based on the ancestry, takes user input for free ability boosts
def freeAbilityBoost (amount):
    if amount == 2:
        print("Thanks to your ancestry, you have (" + str(amount) + ") free ability boosts.")
    else:
        print("Thanks to your ancestry, you have (" + str(amount) + ") free ability boost.")
    print("Please input the ability boost(s) you have chosen")
    print("A - Strength")
    print("B - Dexterity")
    print("C - Constitution")
    print("D - Intelligence")
    print("E - Wisdom")
    print("F - Charisma")
    print()

    for i in range(amount):
        finalBoostInput = anyInput('A', 'B', 'C', 'D', 'E', 'F')
        CharacterInformation.abilityScores[freeBoostChoices[finalBoostInput]] += 2
        if(amount==2 and i!=1):
            print("You have (1) remaining ability boost to choose from")

# ------------------------------------------Ancestry Feat choices--------------------------------------------------
# converts input into the real ancestry feat name

dwarfAFChoices = {
    "A": "Avenge In Glory",
    "B": "Clan’s Edge",
    "C": "Dwarven Lore",
    "D": "Dwarven Weapon Familiarity",
    "E": "Forge-Day’s Rest",
    "F": "Rock Runner",
    "G": "Stonecunning",
    "H": "Surface Culture",
    "I": "Unburdened Iron",
    "J": "Vengeful Hatred"
}

elfAFChoices = {
    "A": "Ancestral Longevity",
    "B": "Elemental WrathFeat",
    "C": "Elven Lore",
    "D": "Elven Verve",
    "E": "Elven Weapon Familiarity",
    "F": "Forlorn",
    "G": "Nimble Elf",
    "H": "Share Thoughts",
    "I": "Otherworldly Magic",
    "J": "Unwavering Mien",
    "K": "Wildborn Magic",
    "L": "Woodcraft"
}

gnomeAFChoices = {
    "A": "Animal Accomplice",
    "B": "Burrow Elocutionist",
    "C": "Fey Fellowship",
    "D": "Fey World Magic",
    "E": "Gnome Obsession",
    "F": "Gnome Polyglot",
    "G": "Gnome Weapon Familiarity",
    "H": "Grim Insight",
    "I": "Illusion Sense",
    "J": "Inventive Offensive",
    "K": "Life-Giving Magic",
    "L": "Natural Performer",
    "M": "Theoretical Acumen",
    "N": "Unexpected Shift",
    "O": "Vibrant Display",
}

goblinAFChoices = {
    "A": "Bouncy Goblin",
    "B": "Burn It!",
    "C": "City Scavenger",
    "D": "Fang Sharpener",
    "E": "Goblin Lore",
    "F": "Goblin Scuttle",
    "G": "Goblin Song",
    "H": "Goblin Weapon Familiarity",
    "I": "Hard Tail",
    "J": "Junk Tinker",
    "K": "Rough Rider",
    "L": "Very Sneaky"
}

halflingAFChoices = {
    "A": "Adroit Manipulation",
    "B": "Distracting Shadows",
    "C": "Halfling Lore",
    "D": "Halfling Luck",
    "E": "Halfling Weapon Familiarity",
    "F": "Innocuous",
    "G": "Intuitive Cooperation",
    "H": "Sure Feet",
    "I": "Titan Slinger",
    "J": "Unassuming Dedication",
    "K": "Unfettered Halfling",
    "L": "Watchful Halfling"
}

humanAFChoices = {
    "A": "Adapted Cantrip",
    "B": "Arcane Tattoos",
    "C": "Astrology",
    "D": "Construct Summoner",
    "E": "Cooperative Nature",
    "F": "Courteous Comeback",
    "G": "Devil’s Advocate",
    "H": "Dragon Spit",
    "I": "General Training",
    "J": "Gloomseer",
    "K": "Haughty Obstinacy",
    "L": "Keep Up Appearances",
}


# --------------------------------------Heritage, Boost and Ancestry Feat-----------------------------------------------
# saves user input for ancestry, heritage and ancestry feat

# adds appropriate statistics to the character
if CharacterInformation.ancestry == 'Dwarf':
    CharacterInformation.stats["Hit Points"] = 10
    CharacterInformation.stats["Size"] = "Medium"
    CharacterInformation.stats["Speed"] = 20
    CharacterInformation.abilityScores["Constitution"] = 12
    CharacterInformation.abilityScores["Wisdom"] = 12
    CharacterInformation.abilityScores["Charisma"] = 8
    freeAbilityBoost(1)

    # heritage printout message
    print()
    print(TextStyle.bold + "Next, input your character's heritage" + TextStyle.reset)
    print("A - Ancient-Blooded Dwarf")
    print("B - Anvil Dwarf")
    print("C - Death Warden Dwarf")
    print("D - Elemental Heart Dwarf")
    print("E - Forge Dwarf")
    print("F - Oathkeeper Dwarf")
    print("G - Rock Dwarf")
    print("H - Strong-blooded Dwarf")
    print()
    # user input for heritage choice
    finalHeritageInput = anyInput('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
    CharacterInformation.heritage = dwarfHeritageChoices[finalHeritageInput]

    print()
    print(TextStyle.bold + "Next, input your character's ancestry feat" + TextStyle.reset)
    print("A - Avenge In Glory")
    print("B - Clan’s Edge")
    print("C - Dwarven Lore")
    print("D - Dwarven Weapon Familiarity")
    print("E - Forge-Day’s Rest")
    print("F - Rock Runner")
    print("G - Stonecunning")
    print("H - Surface Culture")
    print("I - Unburdened Iron")
    print("J - Vengeful Hatred")
    print()
    # user input for ancestry feat choice
    finalAFInput = anyInput('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J')
    CharacterInformation.ancestryFeat = dwarfAFChoices[finalAFInput]

elif CharacterInformation.ancestry == 'Elf':
    CharacterInformation.stats["Hit Points"] = 6
    CharacterInformation.stats["Size"] = "Medium"
    CharacterInformation.stats["Speed"] = 30
    CharacterInformation.abilityScores["Dexterity"] = 12
    CharacterInformation.abilityScores["Intelligence"] = 12
    CharacterInformation.abilityScores["Constitution"] = 8
    freeAbilityBoost(1)

    print()
    print(TextStyle.bold + "Next, input your character's heritage" + TextStyle.reset)
    print("A - Ancient Elf")
    print("B - Arctic Elf")
    print("C - Cavern Elf")
    print("D - Desert Elf")
    print("E - Seer Elf")
    print("F - Whisper Elf")
    print("G - Woodland Elf")
    print()
    finalHeritageInput = anyInput('A', 'B', 'C', 'D', 'E', 'F', 'G')
    CharacterInformation.heritage = elfHeritageChoices[finalHeritageInput]

    print()
    print(TextStyle.bold + "Next, input your character's ancestry feat" + TextStyle.reset)
    print("A - Ancestral Longevity")
    print("B - Elemental WrathFeat")
    print("C - Elven Lore")
    print("D - Elven Verve")
    print("E - Elven Weapon Familiarity")
    print("F - Forlorn")
    print("G - Nimble Elf")
    print("H - Share Thoughts")
    print("I - Otherworldly Magic")
    print("J - Unwavering Mien")
    print("K - Wildborn Magic")
    print("L - Woodcraft")
    print()
    finalAFInput = anyInput('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L')
    CharacterInformation.ancestryFeat = elfAFChoices[finalAFInput]

elif CharacterInformation.ancestry == 'Gnome':
    CharacterInformation.stats["Hit Points"] = 8
    CharacterInformation.stats["Size"] = "Small"
    CharacterInformation.stats["Speed"] = 25
    CharacterInformation.abilityScores["Constitution"] = 12
    CharacterInformation.abilityScores["Charisma"] = 12
    CharacterInformation.abilityScores["Strength"] = 8
    freeAbilityBoost(1)

    print()
    print(TextStyle.bold + "Next, input your character's heritage" + TextStyle.reset)
    print("A - Chameleon Gnome")
    print("B - Fey-Touched Gnome")
    print("C - Sensate Gnome")
    print("D - Umbral Gnome")
    print("E - Vivacious Gnome")
    print("F - Wellspring Gnome")
    print()
    finalHeritageInput = anyInput('A', 'B', 'C', 'D', 'E', 'F')
    CharacterInformation.heritage = gnomeHeritageChoices[finalHeritageInput]

    print()
    print(TextStyle.bold + "Next, input your character's ancestry feat" + TextStyle.reset)
    print("A - Animal Accomplice")
    print("B - Burrow Elocutionist")
    print("C - Fey Fellowship")
    print("D - Fey World Magic")
    print("E - Gnome Obsession")
    print("F - Gnome Polyglot")
    print("G - Gnome Weapon Familiarity")
    print("H - Grim Insight")
    print("I - Illusion Sense")
    print("J - Inventive Offensive")
    print("K - Life-Giving Magic")
    print("L - Natural Performer")
    print("M - Theoretical Acumen")
    print("N - Unexpected Shift")
    print("O - Vibrant Display")
    finalAFInput = anyInput('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O')
    CharacterInformation.ancestryFeat = gnomeAFChoices[finalAFInput]

elif CharacterInformation.ancestry == 'Goblin':
    CharacterInformation.stats["Hit Points"] = 6
    CharacterInformation.stats["Size"] = "Small"
    CharacterInformation.stats["Speed"] = 25
    CharacterInformation.abilityScores["Dexterity"] = 12
    CharacterInformation.abilityScores["Charisma"] = 12
    CharacterInformation.abilityScores["Strength"] = 8
    freeAbilityBoost(1)

    print()
    print(TextStyle.bold + "Next, input your character's heritage" + TextStyle.reset)
    print("A - Charhide Goblin")
    print("B - Irongut Goblin")
    print("C - Razortooth Goblin")
    print("D - Snow Goblin")
    print("E - Tailed Goblin")
    print("F - Treedweller Elf")
    print("G - Unbreakable Goblin")
    print()
    finalHeritageInput = anyInput('A', 'B', 'C', 'D', 'E', 'F', 'G')
    CharacterInformation.heritage = goblinHeritageChoices[finalHeritageInput]

    print()
    print(TextStyle.bold + "Next, input your character's ancestry feat" + TextStyle.reset)
    print("A - Bouncy Goblin")
    print("B - Burn It!")
    print("C - City Scavenger")
    print("D - Fang Sharpener")
    print("E - Goblin Lore")
    print("F - Goblin Scuttle")
    print("G - Goblin Song")
    print("H - Goblin Weapon Familiarity")
    print("I - Hard Tail")
    print("J - Junk Tinker")
    print("K - Rough Rider")
    print("L - Very Sneaky")
    finalAFInput = anyInput('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L')
    CharacterInformation.ancestryFeat = goblinAFChoices[finalAFInput]

elif CharacterInformation.ancestry == 'Hafling':
    CharacterInformation.stats["Hit Points", "Size", "Speed"] = 6, "Small", 25
    CharacterInformation.abilityScores["Dexterity", "Wisdom", "Strength"] = 12, 12, 8
    CharacterInformation.stats["Hit Points"] = 6
    CharacterInformation.stats["Size"] = "Small"
    CharacterInformation.stats["Speed"] = 25
    CharacterInformation.abilityScores["Dexterity"] = 12
    CharacterInformation.abilityScores["Wisdom"] = 12
    CharacterInformation.abilityScores["Strength"] = 8
    freeAbilityBoost(1)

    print()
    print(TextStyle.bold + "Next, input your character's heritage" + TextStyle.reset)
    print("A - Gutsy Halfling")
    print("B - Hillock Halfling")
    print("C - Nomadic Halfling")
    print("D - Twilight Halfling")
    print("E - Wildwood Halfling")
    print()
    finalHeritageInput = anyInput('A', 'B', 'C', 'D', 'E')
    CharacterInformation.heritage = halflingHeritageChoices[finalHeritageInput]

    print()
    print(TextStyle.bold + "Next, input your character's ancestry feat" + TextStyle.reset)
    print("A - Adroit Manipulation")
    print("B - Distracting Shadows")
    print("C - Halfling Lore")
    print("D - Halfling Luck")
    print("E - Halfling Weapon Familiarity")
    print("F - Innocuous")
    print("G - Intuitive Cooperation")
    print("H - Sure Feet")
    print("I - Titan Slinger")
    print("J - Unassuming Dedication")
    print("K - Unfettered Halfling")
    print("L - Watchful Halfling")
    finalAFInput = anyInput('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K','L')
    CharacterInformation.ancestryFeat = halflingAFChoices[finalAFInput]

elif CharacterInformation.ancestry == 'Human':
    CharacterInformation.stats["Hit Points"] = 8
    CharacterInformation.stats["Size"] = "Medium"
    CharacterInformation.stats["Speed"] = 25
    CharacterInformation.abilityScores["Intelligence"] = 12
    freeAbilityBoost(2)

    print()
    print(TextStyle.bold + "Next, input your character's heritage" + TextStyle.reset)
    print("A - Skilled Heritage")
    print("B - Versatile Heritage")
    print("C - Wintertouched Heritage")
    print()
    finalHeritageInput = anyInput('A', 'B', 'C')
    CharacterInformation.heritage = humanHeritageChoices[finalHeritageInput]

    print()
    print(TextStyle.bold + "Next, input your character's ancestry feat" + TextStyle.reset)
    print("A - Adapted Cantrip")
    print("B - Arcane Tattoos")
    print("C - Astrology")
    print("D - Construct Summoner")
    print("E - Cooperative Nature")
    print("F - Courteous Comeback")
    print("G - Devil’s Advocate")
    print("H - Dragon Spit")
    print("I - General Training")
    print("J - Gloomseer")
    print("K - Haughty Obstinacy")
    print("L - Keep Up Appearances")
    finalAFInput = anyInput('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L')
    CharacterInformation.ancestryFeat = humanAFChoices[finalAFInput]

# ----------------------------------------------------Background--------------------------------------------------------

# taking user input for the character's background
# Note: does not list all choices due to the immense amount.
print()
print(TextStyle.bold + "Now, input your character's background" + TextStyle.reset)
print(TextStyle.italics + "Note: Choices are not listed due to the immense amount.")
print("=>Please refer to a pathfinder 2e guide OR")
print("the code (Lines 580-716)" + TextStyle.reset)
print()

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
print()
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
print()

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

finalClassInput = anyInput('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L')
CharacterInformation.characterClass = classChoices[finalClassInput.upper()]

# -------------------------------------------------------Items----------------------------------------------------------

goldPieces = 15
# user input for class choice
print("Please input your character's items")
print("Balance: 15GP")

# converts input into the actual item name
itemChoices = {
    'A': "Jellyfish Lamp",
    "B": "Pesh",
    "C": "Swim Fins",
    "D": "Archaic Wayfinder",
    "E": "Black Pearl Aeon Stone",
    "F": "Blessed Tattoo",
    "G": "Final Blade",
    "H": "Sun Orchid Elixir"
}

# used for converting the item into GP
itemPrices = {
    "Jellyfish Lamp": 2,
    "Pesh": 2,
    "Swim Fins": 5,
    "Archaic Wayfinder": 30,
    "Black Pearl Aeon Stone": 20,
    "Blessed Tattoo": 90,
    "Final Blade": 40,
    "Sun Orchid Elixir": 50
}

condition = 0 #used to break outer loop
while condition == 0:
    print()
    print(
        f"{'A - Jellyfish Lamp':<30}{'2 GP':>10}",
        f"\n{'B - Pesh':<30}{'2 GP':>10}",
        f"\n{'C - Swim Fins':<30}{'5 GP':>10}",
        f"\n{'D - Archaic Wayfinder':<30}{'30 GP':>10}",
        f"\n{'E - Black Pearl Aeon Stone':<30}{'20 GP':>10}",
        f"\n{'F - Blessed Tattoo':<30}{'90 GP':>10}",
        f"\n{'G - Final Blade':<30}{'40 GP':>10}",
        f"\n{'H - Sun Orchid Elixir':<30}{'50 GP':>10}",
          )
    print()

    item = ''
    finalItemInput = anyInput('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
    item = (itemChoices[finalItemInput.upper()])

    # makes sure user has enough GP to buy items
    if itemPrices[item] <= goldPieces:
        goldPieces -= itemPrices[item]
        CharacterInformation.items.append(item)
    else:
        print()
        print("You do not have enough Gold Pieces to purchase your selected item.")
        print("Please try again.")
        continue
    if goldPieces >= 2:  # less than least costing item -> cannot buy any further
        print()
        print("Would you like to input another item? (Y/N)")
        while True:
            print("Balance: " + str(goldPieces) + "GP")
            decision = input("Selection: ").upper()
            if decision == 'Y':
                break
            elif decision == 'N':
                condition = 1
                break
            else:
                print("Invalid input. Please try again.")
                continue
    else:
        print("You do not have enough gold pieces to purchase any items.")
        break

# -------------------------------------------------------Spells---------------------------------------------------------
print()
# a list of all the classes that do not use spells
classWithoutSpells = ["ALCHEMIST", "BARBARIAN", "FIGHTER", "MONK", "RANGER", "ROGUE"]

if CharacterInformation.characterClass.upper() not in classWithoutSpells:
    print("Please input your character's spell")
    print(TextStyle.italics + "Note: Choices are not listed due to the immense amount.")
    print("=>Please refer to a pathfinder 2e guide OR")
    print("the code (Lines 811-892)" + TextStyle.reset)
    print()
    finalSpellInput = anyInput(
        "ACID SPLASH",
        "AIR BUBBLE",
        "ALARM",
        "ANT HAUL",
        "BANE",
        "BLESS",
        "BURNING HANDS",
        "CHARM",
        "CHILL TOUCH",
        "COLOR SPRAY",
        "COMMAND",
        "CREATE WATER",
        "DANCING LIGHTS",
        "DAZE",
        "DETECT ALIGNMENT",
        "DETECT MAGIC",
        "DETECT POISON",
        "DISRUPT UNDEAD",
        "DISRUPTING WEAPONS",
        "DIVINE LANCE",
        "ELECTRIC ARC",
        "FEAR",
        "FEATHER FALL",
        "FLEET STEP",
        "FLOATING DISK",
        "FORBIDDING WARD",
        "GHOST SOUND",
        "GOBLIN POX",
        "GREASE",
        "GRIM TENDRILS",
        "GUIDANCE",
        "GUST OF WIND",
        "HARM",
        "HEAL",
        "HYDRAULIC PUSH",
        "ILLUSORY DISGUISE",
        "ILLUSORY OBJECT",
        "ITEM FACADE",
        "JUMP",
        "KNOW DIRECTION",
        "LIGHT",
        "LOCK",
        "LONGSTRIDER",
        "MAGE ARMOR",
        "MAGE HAND",
        "MAGIC AURA",
        "MAGIC FANG",
        "MAGIC MISSILE",
        "MAGIC WEAPON",
        "MENDING",
        "MESSAGE",
        "MINDLINK",
        "NEGATE AROMA",
        "PASS WITHOUT TRACE",
        "PEST FORM",
        "PHANTOM PAIN",
        "PRESTIDIGITATION",
        "PRODUCE FLAME",
        "PROTECTION",
        "PURIFY FOOD AND DRINK",
        "RAY OF ENFEEBLEMENT",
        "RAY OF FROST",
        "READ AURA",
        "SANCTUARY",
        "SHIELD",
        "SHILLELAGH",
        "SHOCKING GRASP",
        "SIGIL",
        "SLEEP",
        "SOOTHE",
        "SPIDER STING",
        "SPIRIT LINK",
        "STABILIZE",
        "SUMMON ANIMAL",
        "SUMMON CONSTRUCT",
        "SUMMON FEY",
        "SUMMON PLANT OR FUNGUS",
        "TANGLEFOOT",
        "TELEKINETIC PROJECTILE",
        "TRUE STRIKE",
        "UNSEEN SERVANT",
        "VENTRILOQUISM"
    )
    CharacterInformation.spell = finalSpellInput

else:
    print("Note: Your character's class does not use spells.")

# ------------------------------------Displays the character's information----------------------------------------------

print("Good job! You have completed your character.")
print()
print("------------------------------- Character Information Summary -------------------------------")
print()

print(TextStyle.underline + "Character Description" + TextStyle.reset)
print("Name: " + CharacterInformation.name)
print("Age: " + str(CharacterInformation.age) + " years old")
print("Height: " + str(CharacterInformation.height) + " feet tall")
print("Hit Points: " + str(CharacterInformation.stats['Hit Points']))
print("Size: " + CharacterInformation.stats['Size'])
print("Speed: " + str(CharacterInformation.stats['Speed']) + " feet")
print()

print(TextStyle.underline + "Character Attributes" + TextStyle.reset)
print("Ancestry: " + CharacterInformation.ancestry)
print("Heritage: " + CharacterInformation.heritage)
print("Ancestry Feat: " + CharacterInformation.ancestryFeat)
print("Background: " + CharacterInformation.background)
print("Class: " + CharacterInformation.characterClass)
print()

print(TextStyle.underline + "Inventory" + TextStyle.reset)
print("Spell: " + CharacterInformation.spell)
itemList = ', '.join(CharacterInformation.items)
print("Items: " + itemList)

print(" ")
print(TextStyle.underline + "Ability Scores" + TextStyle.reset)
print("Strength: " + str(CharacterInformation.abilityScores['Strength']))
print("Dexterity: " + str(CharacterInformation.abilityScores['Dexterity']))
print("Constitution: " + str(CharacterInformation.abilityScores['Constitution']))
print("Intelligence: " + str(CharacterInformation.abilityScores['Intelligence']))
print("Wisdom: " + str(CharacterInformation.abilityScores['Wisdom']))
print("Charisma: " + str(CharacterInformation.abilityScores['Charisma']))
print("---------------------------------------------------------------------------------------------")

# --------------------------------------(Post character creation) - User feedback---------------------------------------
print()
print(">>Thank you for using Buildrew™. Would you like to rate your experience? (Y/N)")

#takes user input for the rating
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
                        print(TextStyle.green + '★', end='')
                    for i in range(5 - int(rating)):
                        print(TextStyle.red + '☆' + TextStyle.reset, end='')
                    break
                else:
                    print("Sorry, please input an integer between 1 to 5")
            except ValueError:
                print("Sorry, please input an integer between 1 to 5")
        print()
        print(TextStyle.reset + "Thank you. Your feedback is greatly appreciated!")
        break
    elif rateInput.upper() == 'N':
        print("No problem! Have fun!")
        break
    else:
        print("Sorry, that was an invalid input. Try again")

