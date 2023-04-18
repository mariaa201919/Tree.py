class Tree:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    
    def get_type(self):
        if self.height > 20:
            return "Tall tree"
        elif self.height < 10:
            return "Short tree"
        else:
            return "Medium-sized tree"

oak = Tree("Oak", 15)
maple = Tree("Maple", 20)

print(f"The {oak.name} is a {oak.get_type()}.")
print(f"The {maple.name} is a {maple.get_type()}.")
