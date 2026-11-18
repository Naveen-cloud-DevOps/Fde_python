def addition(a, b):
    return a + b
print("calculator module is loaded")

if __name__ == "__main__":
    print("This is the calculator module.") 
    print("addition", addition(10, 5))  

    #guard method is used to check whether the module is being run directly or being imported. If the module is being run directly, the code inside the if block will be executed. If the module is being imported, the code inside the if block will not be executed.
    # when this condtion will be wrong if any one import this module in another module then this condition will be false and the code inside the if block will not be executed.