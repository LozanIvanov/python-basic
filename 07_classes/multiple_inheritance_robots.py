class Robot:
    def __init__(self,name):
        self.name=name
    def identify(self):
        print(f"Iam robot {self.name}")    

class Walker:
    def move(self):
        print("Walking on the ground")
class Flyer:
    def move(self):
        print("Flying in the air")
class Swimmer:
    def move(self):
        print("Swimming in the water")  

class FlyingRobot(Robot,Flyer):
     pass                
    
class AmphibiousRobot(Robot,Walker,Swimmer):
     pass
class AdvancedRobot(Robot,Walker,Swimmer,Flyer):
    pass       
  
r1 = FlyingRobot("Eagle-1")
r2 = AmphibiousRobot("Hydra-7")
r3 = AdvancedRobot("XR-3000")  

r1.identify()
r1.move()

r2.identify()
r2.move()

r3.identify()
r3.move()