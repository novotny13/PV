def generatorSudychCisel(od, do):
    i = od
    while(i <= do):
        if(i%2 == 0):
            yield i
        i=i+1

for x in generatorSudychCisel(1,100):
    print(x)