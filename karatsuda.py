from math import floor
def karatsuda(x,y):
    if (x < 10) or (y < 10):
        return x*y
    lenght = max(len(str(x)),len(str(y)))
    mid = int(floor(float(lenght)/2))
    higherx,lowerx,highery,lowery = int(floor(x/10**mid)),int(x%(10**mid)),int(floor(y/10**mid)), int(y%(10**mid))
    nb1,nb2,nb3 = karatsuda(lowerx,lowery),karatsuda((lowerx+higherx),(lowery+highery)),karatsuda(higherx,highery)
    return ((nb3*10**(2*mid))+((nb2-nb3-nb1)*10**(mid))+ nb1)
print("le produit est : ",karatsuda(eval(input("entré le premier nombre a multiplié : ")),eval(input("entré le deuxième nombre a multiplié : "))))
