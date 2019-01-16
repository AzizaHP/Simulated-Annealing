import math
import random

x1 = random.uniform(-10,10)
x2 = random.uniform(-10,10)

def fa(x1,x2):
    formula = (4 - 2.1 * x1 ** 2 + x1 ** 4 / 3) * x1 ** 2 + x1 * x2 + (-4 + 4 * x2 ** 2) * x2 ** 2
    return formula

SolusiSementara = fa(x1,x2)
T = 50000
i = 0
while ((i != 40000) and (T != 0)):
    x1sementara = random.uniform(-10,10)
    x2sementara = random.uniform(-10,10)
    SolusiBaru = fa(x1sementara,x2sementara)
    if (SolusiSementara > SolusiBaru):
        SolusiSementara = SolusiBaru
        x1 = x1sementara
        x2 = x2sementara
    elif (SolusiSementara <= SolusiBaru):
        deltaE = SolusiBaru - SolusiSementara
        saa = math.e **((-1*deltaE) / T)
        ran = random.random()
        if ( saa > ran):
            SolusiSementara = SolusiBaru
            x1 = x1sementara
            x2 = x2sementara
        # endif
        T = T*0.9
        i+=1
    print("Pada Iterasi ke ",i," didapat Nilai T : ",T," dengan solusi : ",SolusiSementara)
# endwhile
print("Nilai Minimum : ",SolusiSementara)