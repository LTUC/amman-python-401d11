import math
def square_finder_comprehention():
    lst=[1,2,3,4,5]
    squares= [num*num for num in lst]  #[num**2 for num in lst] / [math.pow(num) for num in lst]
    print(squares)
    assert squares == [1,4,9,16,25]


# square_finder_comprehention()    

def square_finder_iterattor():
    lst=[1,2,3,4,5]
    # lst = [5,2,6,9,8]
    squares=[]
    for num in range(len(lst)):
        square = lst[num]*lst[num]
        squares.append(square)

    # squares= #TODO 
    print(squares)
    # try: 
    #      assert squares == [1,4,9,16,25]
    # except  AssertionError:
        # print("wong answer")   


# square_finder_iterattor()   

# print(math.pow(2,2))