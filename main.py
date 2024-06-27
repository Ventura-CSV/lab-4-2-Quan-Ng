def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    total = 0
    for i in range(5):
        num = int(input('Enter a Number: '))
        total = num + total

    print("total:",total)
    
   

    ########################################
    # Do not delete the return statement
    ########################################
    return total


if __name__ == '__main__':
    main()
