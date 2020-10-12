def cryptageRSA():
    string = input("Entrez la phrase à crypte : ").lower()
    c = eval(input("Entrez c : "))
    n = eval(input("Entrez n : "))
    for p in string:
        if 97<=ord(p)<=122:
            if ((ord(p)-96)**c)%n >= 10 :
                print(((ord(p)-96)**c)%n,end = " ")
            else:
                print("0",end="")
                print(((ord(p)-96)**c)%n,end = " ")
        else:
            print("00",end=" ")

def decryptage():
    string = input("Entrez la phrase à decrypte : ")
    d = eval(input("Entrez d : "))
    n = eval(input("Entrez n : "))
    string = string.split(" ")
    for c in string:
        if c == "00":
            print(" ",end="")
        else:
            print(chr(((int(c))**d)%n+96),end = "")

i=5
while i !=0:
    print()
    i = eval(input("1 = Cryp,2 = Decryp , 0 = Arrêt : "))
    if i == 1:
        cryptageRSA()
    if i == 2:
        decryptage()
