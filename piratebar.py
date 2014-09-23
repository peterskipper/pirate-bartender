import random

#some global dicts
questions = {
    "strong": "Do ye like yer drinks strong (y/n)? ",
    "salty": "Do ye like it with a salty tang (y/n)? ",
    "bitter": "Are ye a lubber who likes it bitter (y/n)? ",
    "sweet": "Would ye like a bit of sweetness with yer poison (y/n)? ",
    "fruity": "Are ye one for a fruity finish (y/n)? "
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["stick of olives", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

pirate_adjs = ["Leeward", "Scurvy", "Starboard", "Salty", "Golden", "Iron", "Ill-Gotten", "Swashbucklin'", "Treacherous", "Fearsome", "Greedy", "Brutal", "Mutinous", "Stormy"]
pirate_nouns = ["Cutlass", "Galleon", "Gangplank", "Spyglass", "Henry Morgan", "Rear Admiral", "Doubloon", "Crow's Nest",  "Shiver-Me-Timbers",  "Treasure Map", "First Mate"]

customers = {}

stock = {}

def fill_stock(stock):
    stuff = [item for type in ingredients for item in ingredients[type]]
    for item in stuff:
        stock[item] = random.randint(2,7)

def get_order():
    """Create and return a new dict with user's drink preferences"""
    #initialize prefs with logical defaults, all False
    prefs = {}
    for key in questions:
        resp = raw_input(questions[key])
        prefs[key] = resp.lower() in ['y', 'yes']
    return prefs

def make_order(prefs):
    """Choose ingredients that match user preferences and return list of drink ingredients"""
    drink = []
    for key in prefs:
        if prefs[key]:
            choice = random.choice(ingredients[key])
            drink.append(choice)
            stock[choice] -= 1
            if stock[choice] == 0:
                print "Headed to the back room for more " + choice
                stock[choice] += 9 
    return drink

def name_drink():
    return random.choice(pirate_adjs) + ' ' + random.choice(pirate_nouns)

def customer():
    name = raw_input("What's yer name, sailor? ").lower()
    if name in customers:
        usual = raw_input("Would ye like the usual (y/n)? ")
        if usual.lower() in ['y', 'yes']:
            return customers[name]
        else:
            prefs = get_order()
            return prefs
    else:
        prefs = get_order()
        customers[name] = prefs
        return prefs

def main():
    print "Welcome to The Tattered Sail!\n"
    fill_stock(stock)
    while True:
        preferences = customer()
        drink = make_order(preferences)
        print "\n\nArrr! Have a " + name_drink() + "!"
        print
        print "It's got",
        for ingredient in drink:
            if ingredient == drink[-1]:
                print "and a " + ingredient + "."
            else:
                print "a " + ingredient + ",",
        stay = raw_input("\nWould ye like another beverage (y/n)? ")
        if stay.lower() in ['n', 'no']:
            break
    print "Stay Jolly, Roger!  See ye again soon!"


if __name__ == '__main__':
    main()