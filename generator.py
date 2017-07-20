# name-generator
import random

superhero1 = ["spider", "super", "mighty", "captain", "laser", "killer", "mega", "cat", "mutant", "dare", "purple", "fish-reader", "wacky", "contagious", "iron", "wonder"]
superhero2 = ["man", "woman", "bug", "kid", "baby", "poo", "marker", "dawg", "yogurt", "king", "queen", "alien", "joker", "cookie", "kiwi", "sneeze" ]

random1 = random.randint(0,15)
random2 = random.randint(0,15)

print("Your superhero name is:")
print ((superhero1[random1])+(superhero2[random2]))

#menu-generator
import random
soups = ["noodle soup", "chicken soup", "veggie soup", "french onion soup", "porridge"]
main_dish = ["steak", "pasta", "pizza", "cheeseburger", "spaghetti", "fish", "sushi"]
sauce = ["sriracha", "pesto", "wasabi", "caramel", "soy sauce", "white sauce", "hot fudge", "melted cheese", "dirt", "vinegar", "mustard", "relish", "ketchup", "sour cream", "horseradish"]
dessert = ["cupcake", "ice cream", "cookies", "pie", "strawberry shortcake", "pebbles", "sliced raggy tie", "rotten fruit and worm", "utensils you ate with", "worms", "rat", "sliced snake", "compost", "garbage"]

randomA = random.randint(0,4)
randomB = random.randint(0,6)
randomC = random.randint(0,14)
randomD = random.randint(0,13)

print ("Your meal is:")
print (soups[randomA])
print (main_dish[randomB])
print (sauce[randomC])
print (dessert[randomD])

#haiku-generator
import random

line1= ["The fat bee stings me","crunchy chewy brown", "napkin in trash can"]
line2= ['mosquito in winter time', "tickling my toes and heart"]
line3=["I don not cry though","time almost up"]

randomx= random.randint(0,2)
randomy= random.randint(0,1)
randome= random.randint(0,1)

print("Your haiku is:")
print(line1[randomx])
print(line2[randomy])
print(line3[randome])
