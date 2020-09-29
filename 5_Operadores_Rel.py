'''
Operadores relacionales se usan para comparar dos valores
Los operadores relacionales tienen menor prioridad que los aritméticos

== igual
!= diferente
< mayor que
> menor que
<= menor o igual
>= mayor o igual
'''

n1 = 10
n2 = 20
n3 = 30

res = n1 < n2
print(n1 ,"es < que ", n2,": ", res)
res = n1 > n2
print(n1 ,"es > que ", n2,": ", res)
res = n1 <= n2
print(n1 ,"es <= que ", n2,": ", res)
res = n1 >= n2
print(n1 ,"es >= que ", n2,": ", res)
res = n1 == n2
print(n1 ,"es == que ", n2,": ",  res)
res = n1 != n2
print(n1 ,"es != que ", n2,": ", res)

res = n1 + n2 == n3 # primero se hace la suma y despues la comparación
print(res)