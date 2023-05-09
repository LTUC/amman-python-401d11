# class ?  create instances (object )

# starwars game


class ForceUser: # parent class


    @classmethod
    def force_only(cls):
        return 'this method only for  forceuser class!'

    @classmethod
    def get_count(cls):
        return JediMaster.count + SithLord.count

   

    def __str__(self):
        return f'I am {self.name}, my mantra is {self.get_code()}' # it will print the instance in prettier way 

    def __repr__(self):
        return 'JediMaster("name")' # add technical info about instances

    def attacking(self):
        return f'{self.name} is Force attacking!'
    def getting_hit(self):
        return f'{self.name} is being attacked!'
   


    

class JediMaster(ForceUser): #child 
    count = 0

    def __init__(self,name='Random Master'):
        self.name = name
        self.alignment = "Good Master"
        JediMaster.count += 1
       

    @staticmethod
    def get_code():
        return   'There is no emotion, there is only PEACE.' 
    
    @classmethod
    def get_count(cls):
        return cls.count
    
       

    

   
        
class SithLord(ForceUser):
    count =0
    def __init__(self,name='Random Master'):
        self.name = name
        self.alignment = "Bad Master"
        SithLord.count += 1

    @staticmethod
    def get_code():
        return   'Peace is a lie, there is only PASSION!'     
    
    @classmethod
    def get_count(cls):
        return cls.count





if __name__ == '__main__':
    random = JediMaster()
    yoda = JediMaster("YODA")
    mace = JediMaster("MACE")
    luke = JediMaster("LUKE")
    vade = SithLord("Vade")
    print(yoda.name)
    print(mace.name)
    print(random.name)
    print(luke.name)

    print(luke.attacking())
    print(mace.attacking())
    print(yoda.attacking())
    print(luke.getting_hit())
    print(mace.getting_hit())
    print(yoda.getting_hit())
    print(vade.name)
    print(vade.attacking())
    print(vade.getting_hit())
    print(yoda.force_only())

    ### __str__ and __repr__
    print(yoda) # to show the __str__ (no need to call the method)
    print(yoda.__repr__())
  
  
   




