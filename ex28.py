age=int(input("entrer l'age d'Amal : "))
s=0
for i in range(1,age+1) :
    s=s+(500+(i*3))
print("le compte d'amal à l'age ",age," est : ",s)