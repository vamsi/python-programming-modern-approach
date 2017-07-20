def make_omelette(stir=True, flame=0, *ingredients):
    '''
    Function that makes omelette with required flaming.
    Please use it casrefully otherwise ommelete might burn
    '''
    for ingredient in ingredients:
        print("Taking {}".format(ingredient))

    if stir is True:
        print("Stirring...{} with egg".format(ingredients))

    if stir is False:
        print("Taking egg")

    print("Pouring it on to the pan")
    print("Flaming at level {}".format(flame))
    print("Your omelette ready !")
    return ingredients

# make_omelette(False, 4, "salt", "pepper")
