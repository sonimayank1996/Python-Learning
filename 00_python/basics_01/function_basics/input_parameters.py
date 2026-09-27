def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("darjling", "Yes", "Low") #positional
make_chai(tea="darjling", sugar="Yes", milk="Low") #keywords

def special_chai(*ingrediants, **extra): # *ingrediants = args, **extra = kwargs = keyword args
    print("Ingrediants", ingrediants)
    print("Extra", extra)

special_chai("Lemon", "plain", sweetener="Honey", type= "Garlic")
