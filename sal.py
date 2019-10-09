def main():
    height = int(input("Number of branches: "))
    if height < 0:
        print("Only positive numbers.")
    else:
        for i in range(height):
            print((" " * (height-i)),('#' * (2*i+1)))
        print(height*" ", "#")
        print("Merry Christmas")
main()

