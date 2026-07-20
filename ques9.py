class product:
    def input(self):
        self.product_no=int(input("enter product number:"))
        self.product_name=input("enter product name")
        self.cost=float(input("enter cost"))
        self.quantity=int(input("enter quantity:"))
    def calculate(self):
        self.total_amount=self.cost*self.quantity
    def display(self):
        print("product no:",self.product_no)
        print("product name:",self.product_name)
        print("cost:",self.cost)
        print("qantity:",self.quantity)
        print("total amount:",self.total_amount)
products=[]
for i in range(5):
    print("\n enter product",i+1)
    p=product()
    p.input()
    p.calculate()
    products.append(p)
highest=product[0]
for p in products:
    if p.total_amount>highest.total_amouny:
        highest=p
print("\n product with highest total amount:")
highest.display
        
