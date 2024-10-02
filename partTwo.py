import math  

def main():
    input1 = int(input("Gimme number"))
    input2 = int(input("Gimme number part 2"))
    pythag(input1, input2)
#TO DO

def pythag(A,B):
    ans = math.sqrt((A**2) + (B**2))
    print(ans)
    #TO DO  

main()
