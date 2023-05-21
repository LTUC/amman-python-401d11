## - problem domain :
define a function that takes 2 linkedlists and return a counter for the number of duplicates nodes between them.

## - test cases:

    * empty lists 
    * all nodes are duplicates 
    * no duplicates 
    * mismatching size 
    * 



## - Input-output:
input -> 2 linkeslists 
output -> imteger represents the number of duplicates .

## - Visualisation:
 1 -> 3 -> 4 -> 5 -> 6 ->None
                        ^
 [1,3,4,5,6]

 1 -> 5 -> 7 -> 9 -> 10 -> None
^

## - algo:
- define a function that takes 2 ll that called defin_duplicates.
- create new `counter` variable 
- create new list with the name `lst`
- loop through the fist ll and append each element inside the 'lst`
- assing 2 current noeds that takes the head of each linkedlist 
- loop theought the second ll and check if the value is exisit in the lst or not 
- if yes the counter will be increased by +1
- return the counter as output. 

## - Big(o):
time -> o(2,3n )-> o(n)
space -> o(n) 


## - code:
```python
def defin_duplicates(ll1,ll2):
    counter = 0
    lst = []
    curr_01 = ll1.head
    curr_02 = ll2.head

    while curr_01:
        lst.append(curr_01.value)
        curr_01=curr_01.next

    while curr_02:
        if curr_02.value in lst :
            counter+=1
        curr_02=curr_02.next       

    return counter 





## - walk through :

 1 -> 1 -> 4 -> 5 -> 6 ->None

  1 -> 1-> 7 -> 9 -> 10 -> None
