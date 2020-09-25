class Cost():
    """description of class"""


    def __init__(self, element,number):
        pass


    def find(self,element):
        for i in range (0, len(recipes)):
            if (recipes[i]["name"]==element):
                return recipes[i]
        return False


    def get_cost(self,element,number):
        recipe=find(element)
        if recipe != False:
            if recipe["type"]=="Ore":
                return price_list[element]*number
            elif recipe["type"]!="Catalyst":
                for key in recipe:
                    cost=cost+get_cost(key,recipe[key])
                return cost
            else:
                return 0
        return 0
