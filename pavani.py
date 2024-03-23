class carshowroom:
    def _init_(self):
        self.cgst=12
        self.sgst=14
        self.tax=3
    def company(self):
        while True:
            print("toyota,mercedes,mahendra")
            self.name=input("enter a brand")
            if self.name=="toyota":
                print("welcome to toyota company")
                self.model()
                break
            elif self.name=="mercedes":
                print("welcome to mercedes company")
                self.model()
                break
            elif self.name=="mahendra":
                print("welcome to mahendra company")
                self.model()
                break
            else:
                print("enter a valid company")
    def model(self):
            if self.name=="toyota":
                while True:
                     print("innova,fortuner")
                     self.m=input("enter a model")
                     if self.m=="innova":
                         print("you have choosen innova")
                         self.price()
                         break
                     elif self.m=="fortuner":
                         print("you have choosen fortuner")
                         self.price()
                         break
                     else:
                         print("enter a valid brand")
            elif self.name=="mercedes":
                while True:
                    print("amg g_vegan")
                    self.m=input("enter a model")
                    if self.m=="amg":
                        print("you have choosen amg")
                        self.price()
                        break
                    elif self.m=="g_vegan":
                        print("you have choosen g_vegan")
                        self.price()
                        break
                    else:
                        print("enter a valid model")
            else:
                while True:
                    self.m=input("enter a model")
                    if self.m=="scorpio":
                        print("you have choosen scorpio")
                        self.price()
                        break
            return self.m
    def price(self):
            if self.m=="innova":
                self.p=7000000
            elif self.m=="fortuner":
                self.p=8000000
            elif self.m=="amg":
                self.p=2000000
            elif self.m=="g_vegan":
                self.p=4222226
            else:
                self.p=50000000
            print(self.p+self.cgst+self.sgst+self.tax)
total=carshowroom()
total.company()
total.price()