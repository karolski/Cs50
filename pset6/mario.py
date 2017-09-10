
def main():
    while True:
        h = input("Height:")
        if h.isnumeric() and int(h) < 24:
            h=int(h)
            break
    for n in range(h):
        print(" "*(h-n-1) + "#"*(n+1) + "  " + "#"*(n+1) )


if __name__ == "__main__":
    main()