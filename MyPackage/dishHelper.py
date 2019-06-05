import json
import random
import os

data = {}
data['dishes'] = []

ingredientsCounter = {}
dishesCounter = {}

def calculateProducts(meatEaters, vegetarians, vegans):
    for i in range(meatEaters):
        while True:
            randDish = random.randint(0, len(data['dishes'])-1)
            type = data['dishes'][randDish]['type']
            if type == 'Meat':
                for k, v in data['dishes'][randDish]['ingredients'].items():
                    if k not in ingredientsCounter:
                        ingredientsCounter[k] = round(v, 3)
                    else:
                        ingredientsCounter[k] += round(v, 3)
                if data['dishes'][randDish]['name'] not in dishesCounter:
                    dishesCounter[data['dishes'][randDish]['name']] = 1
                else:
                    dishesCounter[data['dishes'][randDish]['name']] += 1
                break
    for i in range(vegetarians):
        while True:
            randDish = random.randint(0, len(data['dishes'])-1)
            type = data['dishes'][randDish]['type']
            if type == 'Vegetarian':
                for k, v in data['dishes'][randDish]['ingredients'].items():
                    if k not in ingredientsCounter:
                        ingredientsCounter[k] = round(v, 3)
                    else:
                        ingredientsCounter[k] += round(v, 3)
                if data['dishes'][randDish]['name'] not in dishesCounter:
                    dishesCounter[data['dishes'][randDish]['name']] = 1
                else:
                    dishesCounter[data['dishes'][randDish]['name']] += 1
                break

    for i in range(vegans):
        while True:
            randDish = random.randint(0, len(data['dishes'])-1)
            type = data['dishes'][randDish]['type']
            if type == 'Vegan':
                for k, v in data['dishes'][randDish]['ingredients'].items():
                    if k not in ingredientsCounter:
                        ingredientsCounter[k] = round(v, 3)
                    else:
                        ingredientsCounter[k] += round(v, 3)
                if data['dishes'][randDish]['name'] not in dishesCounter:
                    dishesCounter[data['dishes'][randDish]['name']] = 1
                else:
                    dishesCounter[data['dishes'][randDish]['name']] += 1
                break

    for k, v in ingredientsCounter.items():
        ingredientsCounter[k] = round(v, 3)
    print(ingredientsCounter)
    print(dishesCounter)

def getDishes():
    return dishesCounter

def getIngredients():
    return ingredientsCounter

def saveGeneratedIngredients(filename):
    with open(filename, 'w') as outfile:
        json.dump(ingredientsCounter, outfile, indent=4)

def saveGeneratedDishes(filename):
    with open(filename, 'w') as outfile:
        json.dump(dishesCounter, outfile, indent=4)

def saveDishes():
    with open('packageData.dat', 'w') as outfile:
        json.dump(data, outfile, indent=4)

def loadDishes():
    this_dir, this_filename = os.path.split(__file__)
    DATA_PATH = os.path.join(this_dir, "packageData.dat")
    global data
    with open(DATA_PATH, "r") as read_file:
        data = json.load(read_file)

def loadDishesFromPath(path):
    global data
    with open(path, "r") as read_file:
        data = json.load(read_file)