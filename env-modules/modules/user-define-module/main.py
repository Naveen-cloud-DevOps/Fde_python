from addition import addition
from subtraction import subtraction
from multiplication import multiplication
from divison import divison


def main():
    print("addition", addition(10, 5))
    print("subtraction", subtraction(10, 5))        
    print("multiplication", multiplication(10, 5))
    print("division", divison(10, 5))


if __name__ == "__main__": #guard
    main()



# when this condition is true then only the main function will be executed. If any one import this module in another module then this condition will be false and the code inside the if block will not be executed.