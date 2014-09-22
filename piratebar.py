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

def get_order():
    """Create and return a new dict with user's drink preferences"""
    #initialize prefs with logical defaults, all False
    prefs = { "strong": False, "salty": False, "bitter": False, "sweet": False, "fruity": False}
    for key in questions:
        resp = raw_input(questions[key])
        if resp == 'y' or resp == 'yes':
            prefs[key] = True
    return prefs

def make_order(prefs):
    """Choose ingredients that match user preferences and return list of drink ingredients"""
    drink = []
    for key in prefs:
        if prefs[key]:
            drink.append(random.choice(ingredients[key]))
    return drink

if __name__ == '__main__':
    preferences = get_order()
    drink = make_order(preferences)
    print "Arrr! Here's a cocktail with",
    for ingredient in drink:
        if ingredient == drink[-1]:
            print "and a " + ingredient + "."
        else:
            print "a " + ingredient + ",",