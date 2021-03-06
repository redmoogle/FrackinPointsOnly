import os
import jstyleson as json

files = os.listdir("./zb/researchTree")
for file in files:
    with open(f"./zb/researchTree/{file}", 'r') as config:
        jsonobj = json.load(config)
        researchTree = jsonobj["researchTree"]
        for catagory in researchTree:
            researchCatagory = catagory
            catagoryObj = researchTree[catagory] # Incase theres multiple catagories in one file
            for key in catagoryObj:
                try:
                    price = catagoryObj[key]["price"]
                except KeyError: # Not a catagory
                    break
                try:
                    scicost = price = catagoryObj[key]["price"][0]
                    catagoryObj[key]["price"] = [scicost]
                except IndexError:
                    pass # Some of them cost nothing
                researchTree[catagory] = catagoryObj

    with open(f"./zb/researchTree/{file}", 'w+') as config:
        jsonobj["researchTree"] = researchTree
        json.dump(jsonobj, config, indent=4)