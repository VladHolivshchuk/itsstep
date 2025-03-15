class Car:
 speed = 160
 def __init__(self,speed):
    self.speed=speed
 def info(self):
     print("Швидкість:", self.speed)

sp=int(input("Максимальна швидкість:"))
auto = Car(sp)
#print("Швидкість:", auto.speed)
auto.info()
auto2=Car(180)
auto2.info()






