import json

class Cost():
    """description of class"""
    with open(r"recipes.JSON") as json_file:
        recipes=json.load(json_file)
    price_list={"Bauxite":20,"Coal":20,"Quartz":20,"Hematite":20,
            "Chromite":20,"Malachite":20,"Limestone":20,"Natron":20,
            "Petalite":20,"Garnierite":20,"Acanthite":20,"Pyrite":20,
            "Cobaltite":20,"Cryolite":20,"Kolbeckite":20,"Gold Nuggets":20,
            "Rhodonite":20,"Columbite":20,"Illmenite":20,"Vanadinite":20}    

    def __init__(self):
        pass


    def find(self,element):
        for i in range (len(self.recipes)):
            if (self.recipes[i]["name"]==element):
                print('1')
                return self.recipes[i]
        return False


    def get_cost(self,element,number):

        recipe=self.find(element)
        cost=0
        if recipe != False:
            if recipe["type"]=="Ore":
                return self.price_list[element]*number
            elif recipe["type"]!="Catalyst":
                for key in recipe["input"]:
                    cost=cost+self.get_cost(key,recipe[key])
                return cost
            else:
                return 0
        return 0
