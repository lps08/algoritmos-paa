# Python3 program to calculate pow(x,n)
 
# Function to calculate x
# raised to the power y
 
def power(x, y):
 
    if (y == 0):
        return 1
    elif (int(y % 2) == 0):
        return (power(x, int(y / 2)) *
                power(x, int(y / 2)))
    else:
        return (x * power(x, int(y / 2)) *
                power(x, int(y / 2)))
 
 
# Driver Code
if __name__ == "__main__":
    x = 2
    y = 3

    print(int(3/2))
 
    # Function call
    print(power(x, y))