import json

class Cost():
    """description of class"""
    with open(r"recipiesUpdated.JSON") as json_file:
        recipes=json.load(json_file)
    with open(r"skills.JSON") as json_file:
        skills=json.load(json_file)
    price_list={"Bauxite":25,"Coal":25,"Quartz":25,"Hematite":25,
            "Chromite":55,"Malachite":65,"Limestone":65,"Natron":49,
            "Petalite":144,"Garnierite":115,"Acanthite":155,"Pyrite":105,
            "Cobaltite":552,"Cryolite":660,"Kolbeckite":401,"Gold Nuggets":360,
            "Rhodonite":310,"Columbite":750,"Illmenite":550,"Vanadinite":550}    

    itemTier= ["Basic",
           "Uncommon",
           "Advanced",
           "Rare",
           "Exotic"]

    def __init__(self):
        pass


    def findElement(self,element):
        elementSplit=element.split()
        elementSplitLength=len(elementSplit)
        out=[]
        for i in range (len(self.recipes)):
            nameSplit=self.recipes[i]["name"].split()
            nameSplitLength=len(nameSplit)
            m=0
            if ((nameSplitLength>=elementSplitLength) and (nameSplitLength<=elementSplitLength+1)):
                for j in range(elementSplitLength):
                    if (self.match(elementSplit[j],nameSplit)==True):
                        m+=1
                if (m==nameSplitLength):
                    out.clear()
                    out.append(self.recipes[i]["name"])
                    return out
                elif (m==nameSplitLength-1):
                    out.append(self.recipes[i]["name"])
        return out

    def match(self, elementPart,nameSplit):
        for i in range (len(nameSplit)):
            if (nameSplit[i]==elementPart):
                return True
        return False

    def find(self,element):
        return self.recipes[element]

    def findSkill(self,recipe,element):
        craftingSkills= {"Input":0,"Output":0,"Time":0,"Speed":0}              
        for i in range (len(self.skills)):
            if (("target" in self.skills[i])==False):
                for j in range (len(self.skills[i]["data"])):
                    if (self.skills[i]["data"][j]==element):
                        value=self.skills[i]["targets"][j]["amount"]*self.skills[i]["values"][j]
                        craftingSkills[self.skills[i]["targets"][j]["type"]]=value
            else:
                if(self.skills[i]["target"]==recipe["type"]):
                    for j in range  (len(self.skills[i]["data"])):
                        if (self.skills[i]["data"][j]==element):
                            value=self.skills[i]["targets"][j]["amount"]*self.skills[i]["values"][j]
                            craftingSkills[self.skills[i]["targets"][j]["type"]]+=value
                        elif (self.skills[i]["data"][j]=="Efficiency"):
                            amount=self.skills[i]["targets"][j]["amount"]
                            skillLevel=self.skills[i]["values"][j]
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
        skill=self.findSkill(recipe,element)
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
