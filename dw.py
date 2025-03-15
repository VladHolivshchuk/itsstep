import random as r
#class Car:
 #speed = 160
 #def __init__(self,speed):
  #  self.speed=speed
 #def info(self):
     #print("Швидкість:", self.speed)

#sp=int(input("Максимальна швидкість:"))
#auto = Car(sp)
#print("Швидкість:", auto.speed)
#auto.info()
#auto2=Car(180)
#auto2.info()

# class Pupils:
#     count=0
#     def __init__(self,name,height,):
#        self.name=name
#        self.height=height
#        Pupils.count+=1
#     def __str__(self):
#         print("Ім'я уасника:", self.name, "Зріст:", self.height)
#     def __bool__(self):
#         return self.name!=None
#     def __len__(self):
#         return self.height
#
# p1=Pupils("Ігор", 155)
# p1.__str__()
# p2=Pupils("Оля", 167)
# p2.__str__()
# p3=Pupils("Артем", 150)
# p3.__str__()
# print(p1.count, "Участники змагань")
# print(p1.__bool__())
# print(bool(p2))
# print(p3.__len__())
# print(len(p3))

class Student:
    def __init__(self, name):
        self.name=name
        self.happy=r.randint(10, 100)
        self.progress=r.randint(0, 12)
        self.alive=True
    def study(self):
        print('Chas dlya navchannya')
        self.happy-=r.randint(1,50)
        self.progress+=r.randint(1, 12)
    def sleep(self):
        print('Chas dlya sleep')
        self.happy+=r.randint(1, 50)
    def chill(self):
        print('Chas dlya chila')
        self.happy+=r.randint(1,50)
        self.progress-=r.randint(1, 12)
    def DeadLines(self):
        print('Vstigae?')
        if 1<self.progress<5:
            print("Vas poshti IskluCHILi")

        elif self.progress<1:
            print("GGWP!")

        elif 5<self.progress<12:
            print("Good Job!")

    def eveyday(self):
        print('Level of happy', self.happy)
        print('Progress study', self.progress)
    def studylife(self,day):
        day='Dday #'+str(day)
        print(day)
        res=r.randint(1,3)
        if res==1:
            self.study()
        elif res==2:
            self.chill()
        else:
            self.sleep()
        self.eveyday()
        self.DeadLines()


st1=Student('Oleg')
#print(st1.progress)
print("Student`s life", st1.name)
for k in range(1,8):
    if st1.alive==False:
        break
    st1.studylife(k)



