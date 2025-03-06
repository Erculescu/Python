import numpy as np

def functie_obiectiv(cost,valoare,x,costmax):
    cost_x=np.dot(x,cost)
    valoare_x=np.dot(x,valoare)
    return cost_x<=costmax,valoare_x

def calculeaza_vecini(cost,valoare,x,costmax):
    vecini_x=np.zeros(0,int)
    valoare_vecini_x=np.zeros(0,float)
    n=cost.size
    for i in range(n):
        y=x.copy()
        y[i]=not x[i]
        gasit_y,valoare_y=functie_obiectiv(cost,valoare,y,costmax)
        if gasit_y:
            vecini_x=np.append(vecini_x,y)
            valoare_vecini_x=np.append(valoare_vecini_x,valoare_y)
    dim=len(vecini_x)
    vecini_x=vecini_x.reshape(round(dim/n),n)
    return vecini_x,valoare_vecini_x


def hillclimb(fc,fv,iteratii,costmax):
    cost=np.genfromtxt(fc)
    valoare=np.genfromtxt(fv)
    n=cost.size
    cea_mai_buna_iteratie=np.zeros([iteratii,n],int)
    cea_mai_buna_valoare=np.zeros(iteratii,float)

    for i in range(iteratii):
        gasit=False
        while gasit==False:
            x=np.random.randint(0,2,n)
            gasit,val=functie_obiectiv(cost,valoare,x,costmax)
        local=False
        while not local:
            vecini_x,valoare_vecini_x=calculeaza_vecini(cost,valoare,x,costmax)
            dim=vecini_x.size
            if dim==0:
                local=True
            else:
                j=np.argmax(valoare_vecini_x)
                val_max_vecini=valoare_vecini_x[j]
                if val_max_vecini>val:
                    x=vecini_x[j]
                    val=val_max_vecini
                else:
                    local=True
        cea_mai_buna_valoare[i]=val
        cea_mai_buna_iteratie[i]=x
    poz=np.argmax(cea_mai_buna_valoare)
    val_max=cea_mai_buna_valoare[poz]
    cel_mai_bun_individ=cea_mai_buna_iteratie[poz]
    print("Cea mai buna valoare: ",val_max)
    print("Cel mai bun individ: ",cel_mai_bun_individ)
    print("Gasit in iteratia: ",poz)



if __name__=='__main__':
    hillclimb("cost.txt","valoare.txt",100,50)