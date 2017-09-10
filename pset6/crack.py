#Assume that each password has been hashed with C’s DES-based (not MD5-based) crypt function.
#Assume that each password is no longer than (gasp) four character
#Assume that each password is composed entirely of alphabetical characters (uppercase and/or lowercase).
import sys
import crypt
import itertools

def main():
    if len(sys.argv) != 2:
        print("Usage: python crack.py hash")
        return 1
    hash = sys.argv[1]
    salt = hash[0] + hash[1]
    for i in range(5): 
        for j in itertools.product('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm', repeat = i):   
            word = ''.join(map(str, j))
            if hash == crypt.crypt(word, salt):
                print(word)
                return 0
    return 1
if __name__ == "__main__":
    main()