
## Terms :

    1- Attribute

    2- Property

    3- Methods

    4-Encapsulation (hiding data)

    5- Polymorphism

    6- Abstraction

    7- Inheritance

    8- instantiating
    

- `self`: 
 The self variable is a reference to the object itself, so by using it you can read and update the properties of the object.

- `method` : A method is a piece of code that is called by a name that is associated with an object

- `methods` often don't return anything explicitly because they often mutate the properties of the object instead.

- `Methods` Vs. `Functions`:

    - A method is implicitly passed the object on which it was called. In other words, you won't see all the inputs in the parameter list
    - A method is able to operate on data that is contained within the class. In other words, you won't see all the outputs in the return statement.

### Class Variables vs Instance Variables

`Instance variables`
Instance variables vary from object to object and are declared in the constructor.

ex : 
```python
    class Wall():
        def __init__(self,height):
            self.height = height
```

`Class variables`
Class variables remain the same between instances of the same class and are declared at the top-level of a class.

```python
    class Wall():
        height = 10

    south_wall = Wall()
    print(south_wall.height)
    # prints "10"

    Wall.height = 20 # updates all instances of a Wall

    print(south_wall.height)
    # prints "20"
```

`Class vs instance variables – which should I use?`
Generally speaking, stay away from class variables. Just like global variables, class variables are usually a bad idea because they make it hard to keep track of which parts of your program are making data updates.

### The Four Pillars of OOP

##### OOP Pillar #1 – Encapsulation

Encapsulation is the practice of hiding information inside of a "black box" so that other developers working with the code don't have to worry about it.

A basic example of encapsulation would be a function. The caller of a function doesn't need to worry too much about what happens inside – they just need to understand the inputs and outputs.

ex : 
```python 
python_acceleration = calc_acceleration(initial_speed, final_speed, time)
```
In the example above, to use the calc_acceleration function, we don't really need to understand what goes on inside. That's the goal of encapsulation: it makes our lives easier as developers and helps us write cleaner code.

`Encapsulation in OOP`
In the context of object-oriented programming, we can practice good encapsulation by using private and public members.

- The idea is that if we want the users of our class to interact with something directly, we make it `public`. If they don't need to use a certain method or property, we make that `private` in order to keep the usage instructions for our class simple.

`Encapsulation in Python`
In order to enforce encapsulation in Python, developers prefix properties and classes that they intend to be private with a double underscore.
```python 
    class Wall():
        def __init__(self, height):
            # this stops us from accessing the __height
            # property directly on an instance of a Wall
            self.__height = height

        def get_height(self):
            return self.__height
# if I called that method to an instance it will give this error : AttributeError: Wall instance has no attribute '__height'            
```

> In the example above, we don't want users of the Wall class to be able to change its height. We make the __height property private and expose a public get_height method so that users can still read the height of a wall without being tempted to update it.

This will stop developers from being able to do something like:
```python 
# front_wall is an instance of a Wall
front_wall.__height = 10 # this results in an error
```
NOTE :

##### OOP Pillar #2 – Abstraction
Abstraction is one of the key concepts of object-oriented programming. The goal of abstraction is to handle complexity by hiding unnecessary details.

> Abstraction and encapsulation typically go hand in hand, and if we aren't careful with our definitions, they can seem like the same thing.

`Abstraction` vs `encapsulation`

- Abstraction is a technique that helps us identify what information and behavior should be encapsulated, and what should be exposed.
- Encapsulation is the technique for organizing the code to encapsulate what should be hidden, and make visible what is intended to be visible.

`So are we encapsulating or abstracting our code when we make things private?`

Both. We are almost always doing both. The process of using the double underscore is a form of encapsulation. The process of deciding which data deserves to be hidden behind the double underscore is abstraction.

##### OOP Pillar #3 – Inheritance

`What is inheritance?`

Inheritance allows one class (aka `the child class`) to inherit the properties and methods of another class (aka `the parent class`).

>This powerful language feature helps us avoid writing a lot of the same code twice. It allows us to DRY (don't repeat yourself) up our code.

-syntax 
```python
class Animal:
    # parent "Animal" class

class Cow(Animal):
    # child class "Cow" inherits "Animal"
```    

- in order to use the constructor of the parent class, we can use Python's built in super() method.
```python
    class Animal:
    def __init__(self, num_legs):
        self.num_legs = num_legs

    class Cow(Animal):
        def __init__(self):
            # call the parent constructor to
            # give the cow some legs
            super().__init__(4)
```

`When should I use inheritance?`
Inheritance is a powerful tool, but it is a really bad idea to try to overuse it. You should only use inheritance when every instance of the child class can also be considered the same type as the parent class.

When a child class inherits from a parent, it inherits everything. If you only want to share some functionality, inheritance probably is not the best answer. In that case you would probably just want to share some functions, or maybe make a new parent class that both classes inherit from.

> All cats are animals but not all animals are cats.
[image](https://www.freecodecamp.org/news/content/images/size/w1600/2022/10/LwZVCId.png)

## ***Inheritance hierarchy***
There is no limit to how deeply we can nest an inheritance tree. For example, a `Cat` can inherit from `Animal` which inherits from `LivingThing`.

That said, we should always be careful that each time we inherit from a base class that the child is a *strict* subset of the parent. You should never think to yourself "my child class needs a couple of the parent's methods, but not these other ones" and still decide to inherit from that parent.

`Multiple children`

So far we've worked with linear class inheritance. In reality, inheritance structures often form trees, not lines. A class can have as many direct child classes as the programmer wants.

You'll often find in production software that it's more likely that an `inheritance tree` is `wide` than `deep`. In other words, instead of a deep tree like:
`Organism -> Animal -> Mammal -> Feline -> Cat`

You will more often see a wide tree:

Dragon -> Drake
        -> Wyvern
        -> Hydra
        -> Druk

`Why are inheritance trees often wide instead of deep?`

Like we talked about earlier, in good software a child class is a strict subset of its parent class.

In a deep tree, that means the children need to be perfect members of all the parent class "types". That simply doesn't happen very often in the real world. It's much more likely that you'll have a base class that simply has many sibling classes that are slightly different variations of the base.

`Vehicle`->`Truck`
        -> `Car`
        -> `Boat`
        -> `Train`

#### OOP Pillar #4 – Polymorphism
`Polymorphisms Roots`
- "poly" means "many".
- "morph" means "to change" or "form".

Polymorphism in programming is the ability to present the same interface (function or method signatures) for many different underlying forms (data types).


`Polymorphism with shapes`
Let's look at a simple example:
```python
    class Creature():
    def move(self):
        print("the creature moves")

```
> In this example the child classes, `Dragon` and `Kraken` are `overriding` the behavior of their parent class's `move()` method.

A classic example is a Shape class that `Rectangle`, `Circle`, and `Triangle` can inherit from.

With polymorphism, each of these classes will have different underlying data. The circle needs a center and radius. The rectangle needs two co-ordinates for the top left and bottom right corners. The triangle needs coordinates for the corners.

By making each class responsible for its data and its code, you can achieve polymorphism.

In this example, each class would have its own `Draw()` method. This allows the code that uses the different shapes to be simple and easy, and more importantly, it can treat shapes as the same even though they are different. It hides the complexities of the difference behind a clean abstraction.

```python 
    shapes = [Circle(5, 10), Rectangle(1, 3, 5, 6)]
    for shape in shapes:
        print(shape.Draw())
```
```python
    class Human:
        def hit_by_fire(self):
            self.health -= 5
            return self.health

    class Archer:
        def hit_by_fire(self):
            self.health -= 10
            return self.health
```
Both methods have the same name, take 0 inputs, and return integers. If any of those things are different, they would have different function signatures.

Here is an example of different signatures.
