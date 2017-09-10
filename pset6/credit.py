
def main():
    while True:
        b = input("Number: ")
        if b.isdigit():
            break
    a=[]
    count = 0
    for i in range(len(b)):
        a.append(int(b[i]))
    for i in range(1,len(a), 2):
        count += a[i-1] + (a[i]*2)%10 + (a[i]*2)//10
    if len(a)%2 == 1:
        count +=a[len(a)-1]
    if count%10 != 0:
        print("INVALID")
    elif a[0]==4:
        print("VISA")
    elif a[0]==3 and (a[1]==4 or a[1]==7):
        print("AMEX")
    elif a[0]==5 and (a[1]>0 and a[1]<6):
        print("MASTERCARD")
    return 0

if __name__ == "__main__":
    main()