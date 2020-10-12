import json

class Cost():
    """description of class"""
    with open(r"recipes.JSON") as json_file:
        recipes=json.load(json_file)
    with open(r"skills.JSON") as json_file:
        skills=json.load(json_file)
    price_list={"Bauxite":20,"Coal":20,"Quartz":20,"Hematite":20,
            "Chromite":20,"Malachite":20,"Limestone":20,"Natron":20,
            "Petalite":20,"Garnierite":20,"Acanthite":20,"Pyrite":20,
            "Cobaltite":20,"Cryolite":20,"Kolbeckite":20,"Gold Nuggets":20,
            "Rhodonite":20,"Columbite":20,"Illmenite":20,"Vanadinite":20}    

    itemTier: ["Basic",
           "Uncommon",
           "Advanced",
           "Rare",
           "Exotic"]

    def __init__(self):
        pass


    def find(self,element):
        for i in range (len(self.recipes)):
            if (self.recipes[i]["name"]==element):
                print('1')
                return self.recipes[i]
        return False

    def findSkill(self,recipe):
        craftingSkills= {"input":1,"output":1,"time":1}              
        for i in skills:
            if (skills[i].has_key("target")==False):
                for j in skills[i]["data"]:
                    if (skills[i]["data"][j]==recipe["name"]):
                        value=skills[i]["targets"][j]["amount"]*skills[i]["values"][j]
                        craftingSkills[skills[i]["targets"][j]["type"]]=value
            else:
                if(skills[i]["target"]==recipe["type"]):
                    for j in skills[i]["data"]:
                        if (skills[i]["data"][j]==recipe["name"]):
                            value=skills[i]["targets"][j]["amount"]*skills[i]["values"][j]
                            craftingSkills[skills[i]["targets"][j]["type"]]=value
                        elif (skills[i]["data"][j]=="Efficiency"):
                            value=skills[i]["targets"][j]["amount"]*skills[i]["values"][j]
                            craftingSkills[skills[i]["targets"][j]["type"]]=value
                        elif (tier(skills[i]["data"][j])==recipe["tier"]):
                            if (recipe["type"]!="Intermediary Part"):
                                value=skills[i]["targets"][j]["amount"]*skills[i]["values"][j]
                                craftingSkills[skills[i]["targets"][j]["type"]]=value
                            else:
                                value=0.1*skills[i]["values"][j]
                                craftingSkills[skills[i]["targets"][j]["type"]]=value



    def tier(self,name):
        for i in itemTier:
            if (itemTier[i]==name):
                return i
        return False

    def get_cost(self,element,number):

        recipe=self.find(element)
        cost=0
        if recipe != False:
            if recipe["type"]=="Ore":
                return self.price_list[element]*(number/recipe["outputQuantity"])
            elif recipe["type"]!="Catalyst":
                for key in recipe["input"]:
                    outputQuantity=recipe["outputQuantity"]
                    numberNeeded= recipe["input"][key]*(number/outputQuantity)
                    cost=cost+self.get_cost(key,numberNeeded)
                return cost
            else:
                return 0
        return 0
