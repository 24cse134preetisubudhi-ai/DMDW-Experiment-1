class Employee:
    def __init__(self):
        self.empid=int(input("enter employee id:"))
        self.name=input("enter employee name:")
        self.basic_pay=float(input("enter basic pay:"))
        self.ta=float(input("enter TA"))
        self.da=float(input("enter DS"))
    def calc(self):
        self.gross_pay=self.basic_pay+(0.10*self.ta)+(0.40*self.da)
    def display(self):
        print("\n employee details")
        print("employee id:",self.empid)
        print("employee name:",self.name)
        print("basic pay:",self.basic_pay)
        print("TA:",self.ta)
        print("DA:",self.da)
        print("gross pay:",self.gross_pay)
e=Employee()
e.calc()
e.disp()
    
