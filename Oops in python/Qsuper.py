class car:
    def __init__(self,type):
        self.type = type
    
    @staticmethod
    def start():
        print("Car is starting") 
    
    @staticmethod
    def stop():
        print("Car is stopping")
    
class Toyotacar(car):
    def __init__(self, model, type):
        super().__init__(type)
        self.model = model

car1 = Toyotacar("pirus","electric")
print(car1.type)
print(car1.model)
