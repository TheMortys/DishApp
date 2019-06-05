import json
import random
import os

data = {}
data['dishes'] =[]

ingredientsCounter = {}
dishesCounter = {}

def calculateProducts(meatEaters, vegetarians, vegans):
    for i in range(meatEaters):
        while True:
            randDish = random.randint(0, len(data['dishes'])-1)
