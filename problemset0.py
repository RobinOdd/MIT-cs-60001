import math

def main():
    num_x = int(input("Enter a number \"x\": ")) # asks the user for input
    num_y = int(input("Enter a number \"y\": "))

    print("x**y = ", num_x ** num_y) # prints out x raised to the power of y
    print("log(x) = ", math.log(num_x, 2)) # prints out the log (base 2) of x

main()
