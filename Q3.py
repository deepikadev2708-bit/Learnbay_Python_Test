# Parent class
class product:
    def __init__(self, id, Name):
        self.id = id
        self.Name = Name
    def display_product(self):
        print(f"Id: {self.id}")
        print(f"Product Name: {self.Name}")

#child 1
class butter(product):
    count = 50 
    category = "butter"

    def display_butter_details(self):
        print(f"Id: {self.id}")
        print(f"Product Name: {self.Name}")
        print(f"Count: {self.count}")
        print(f"Category: {self.category}")


#child 2
class milk(product):
    count = 90
    category = "milk"

    def display_milk_details(self):
        print(f"Id: {self.id}")
        print(f"Product Name: {self.Name}")
        print(f"Count: {self.count}")
        print(f"Category: {self.category}")

#child 3
class choco(product):
    count = 56
    category = "choco"

    def display_choco_details(self):
        print(f"Id: {self.id}")
        print(f"Product Name: {self.Name}")
        print(f"Count: {self.count}")
        print(f"Category: {self.category}")

p1 = butter(1, "Amul Butter")
p1.display_butter_details()

p2 = milk(2, "Amul Milk")
p2.display_milk_details()

p3 = choco(3, "Amul Choco")
p3.display_choco_details()