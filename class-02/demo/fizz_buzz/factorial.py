def fact(n):
    '''
    this function calculate the factorial for anumber 
    :param n:int
    :return: int
    '''
    if type(n) != int:
        return "please enter a number"

    if n == 1 or n == 0:
        return 1
    # else:
    #     ans=1
    #     while n>1:
    #         ans=ans*n
    #         n=n-1
    # return ans
    return n*fact(n-1)


if __name__ == "__main__":
    print(fact(5))

    def sum_series(n, x=0, y=1):
        print(n, x, y)

    sum_series(10, 3, 6)
