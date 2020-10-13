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

    itemTier= ["Basic",
           "Uncommon",
           "Advanced",
           "Rare",
           "Exotic"]

    def __init__(self):
        pass


    def find(self,element):
        for i in range (len(self.recipes)):
            if (self.recipes[i]["name"]==element):
                return self.recipes[i]
        return False

    def findSkill(self,recipe):
        craftingSkills= {"Input":0,"Output":0,"Time":0}              
        for i in range (len(self.skills)):
            if (("target" in self.skills[i])==False):
                for j in range (len(self.skills[i]["data"])):
                    if (self.skills[i]["data"][j]==recipe["name"]):
                        value+=self.skills[i]["targets"][j]["amount"]*self.skills[i]["values"][j]
                        craftingSkills[self.skills[i]["targets"][j]["type"]]=value
            else:
                if(self.skills[i]["target"]==recipe["type"]):
                    for j in range  (len(self.skills[i]["data"])):
                        if (self.skills[i]["data"][j]==recipe["name"]):
                            value=self.skills[i]["targets"][j]["amount"]*self.skills[i]["values"][j]
                            craftingSkills[self.skills[i]["targets"][j]["type"]]+=value
                        elif (self.skills[i]["data"][j]=="Efficiency"):
                            value=self.skills[i]["targets"][j]["amount"]*self.skills[i]["values"][j]
                            craftingSkills[self.skills[i]["targets"][j]["type"]]+=value
                        elif (self.tier(self.skills[i]["data"][j])==recipe["tier"]):
                            if ((recipe["type"]=="Intermediary Part") and (self.skills[i]["targets"][j]["type"]=="Output")):
                                value=0.1*self.skills[i]["values"][j]
                                craftingSkills[self.skills[i]["targets"][j]["type"]]+=value
                            else:
                                value=self.skills[i]["targets"][j]["amount"]*self.skills[i]["values"][j]
                                craftingSkills[self.skills[i]["targets"][j]["type"]]+=value
        return craftingSkills


    def tier(self,name):
        for i in range (len(self.itemTier)):
            if (self.itemTier[i]==name):
                return i+1
        return False

    def get_cost(self,element,number):

        recipe=self.find(element)
        skill=self.findSkill(recipe)
        cost=0
        if recipe != False:
            if recipe["type"]=="Ore":
                return self.price_list[element]*number
            elif recipe["type"]!="Catalyst":
                for key in recipe["input"]:
                    outputQuantity=recipe["outputQuantity"]*(1+skill["Output"])
                    numberNeeded= (recipe["input"][key]*(1-skill["Input"]))*(number/outputQuantity)
                    cost+=self.get_cost(key,numberNeeded)
                return cost
            else:
                return 0
        return 0
