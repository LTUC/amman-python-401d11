
# print("**************************************")
# print("**    Welcome to the Snakes Cafe!   **")
# print("**    Please see our menu below.    **")
# print("**")
# print("** To quit at any time, type \"quit\" **")
# print("**************************************")

# refactore it & keep it DRY
Appetizers = ["Wings",'Cookies'," Spring Rolls"]


def intro():
    print('''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

''')

def user_insertion():
    user_input=input(">")  
    return user_input        

def main():
    user_input = user_insertion()
    while(user_input.lower() != "quit"):
   
        # if user_input.lower() == "quit":
        #     end_application()        
            if user_input in Appetizers:
                print(user_input)
                #TODO: handle the order numbers
               
            else:
                print("sorry we dont have this item !")
                
            user_input = user_insertion()    

    end_application()


def end_application():
    print("thanks for using snakes cafe application !")          

#invoke the function 
if __name__=="__main__": 
    intro()  
    main()

                 
















