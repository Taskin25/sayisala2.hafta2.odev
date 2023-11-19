def f(x):
    return x ** 3 + 4 * x ** 2 - 10
x_alt=1
x_ust=2
max_iterasyon=4

def IkiyeBolme_Metodu(x_alt, x_ust, max_iter):
    iterasyon = 0

    while iterasyon < max_iter:
        x_kok= (x_alt + x_ust) / 2

        if f(x_kok) == 0:
            break
        elif f(x_kok)*f(x_alt) < 0:
            x_ust=x_kok
        else:
            x_alt=x_kok

        iterasyon +=1

    return (x_alt + x_ust) / 2


sonuc = IkiyeBolme_Metodu(x_alt,x_ust,max_iterasyon)

print("denklemin kökü: {}".format(sonuc))
