from abc import ABC, abstractmethod

class Person :
    def __init__(self, name, age):#constructor
        self.name = name
        self.age = age

    def older_age(self) :
          self.age = self.age+10



#instance variable 

class Wall():
        width= 120 #class variable 
        # def __init__(self,height):
        #     self.height = height #instance variable


       
        def __init__(self, height):
            # this stops us from accessing the __height
            # property directly on an instance of a Wall
            self.__height = height

        def get_height(self):
            return self.__height
        # def get_height(self):
        #     return self.__height




class Animal:
    def __init__(self, num_legs):# constructor
        self.num_legs = num_legs

class Cow(Animal):
    
      def __init__(self,num_legs,weight):# constructor
            # call the parent constructor to
            # give the cow some legs
            super().__init__(num_legs)
            self.weight=weight


# class Shape(ABC):
#     def __init__(self,num_legs):# constructor
#           self.num_legs =num_legs
          
#     @abstractmethod
#     def area(self):
#         pass      


# class Triangle(Shape):
#     def area(self):
#         return self.num_legs*4   

# class Circle(Shape):
#    def area(self):
#         return self.num_legs*raduis  


class Pet(ABC): #base/super/parent
    count =0

    def __init__(self,name):
        self.name = name
        Pet.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

    # @abstractmethod
    # def __str__(self) -> str:
    #     return F"HELLO MY NAME IS {self.name}"
    @abstractmethod # I have to put it in every child class 
    def some_functionality(self):
        pass


    @abstractmethod
    def speak(self):
        pass




class Dog(Pet):

    def __str__(self) -> str:
        return F"HELLO MY NAME IS {self.name}"
    def __repr__(self):
        return F" {self.name} is an instance from Dog class"
    
    def some_functionality(self):
        pass
    def speak(self):
        print("whooof")


class Cat(Pet):

    # def __str__(self) -> str:
    #     return F"HELLO MY NAME IS {self.name}"

    def some_functionality(self):
        pass
    def speak(self):
        print("meoww") 


    def change_name(self):  # instance method
        return f"Mr. {self.name}"    

    @staticmethod 
    def special_char():
        print("liks to jump ")

    @staticmethod 
    def special_char_02(): # static method 
        print("cats always funny ")         


class Hamester(Pet):
    def __str__(self) -> str:
        return F"HELLO MY NAME IS {self.name}"
     
    def some_functionality(self):
        pass
    def speak(self):
        print("memememe")  




if __name__ == '__main__':
    # wall_01 = Wall(100)
    # wall_02 = Wall(200)
    # print(wall_01.width)
    # print(wall_02.width)
    # Wall.width = 500
    # print(wall_01.width)
    # print(wall_02.width)
    # wall_01 = Wall(100)
    # print(wall_01.get_height())
    # print(wall_01.__height)
    # cow= Cow(4)
    # print(cow.num_legs)
    # boxer = Pet("boxer")
    spike = Dog("spike")

    sherry= Cat("sherry")
    tony = Hamester("tony")

    print(spike)
    print(spike.__repr__())
    # print(boxer.name)
    print(sherry.name)
    print(spike.name)
    spike.speak()
    sherry.speak()
    sherry.special_char()
    # Cat.special_char()
    Cat.special_char_02()
    print(Pet.get_count())


    # print(isinstance(boxer,Pet))











