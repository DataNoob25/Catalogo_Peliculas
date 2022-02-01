paradas=[200,375,550,750]
d,m,n,=950,400,len(paradas)

def Viaje(d,m,n,paradas):
 distancia=d
 nafta_kilometros=m
 Nparadas=n
 c1=[]
 c2=0 






 paradas.append(d)
 c1.append(paradas[0]-0)
 for i in range(len(paradas)-1):
  c1.append(paradas[i+1]-paradas[i])
 for i in range(len(paradas)-1):
     if nafta_kilometros>d:
         return 0
     if c1[i]>nafta_kilometros:
         return -1
     nafta_kilometros=nafta_kilometros-c1[i]
     if nafta_kilometros<c1[i+1]:
         c2+=1
         nafta_kilometros=m
 return c2
print(Viaje(d,m,n,paradas))