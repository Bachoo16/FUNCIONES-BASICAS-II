# CUENTA REGRESIVA 
def regresiva(num):
    arreglo=[]
    for i in range (num, 0, -1):
        arreglo.append(i)
    return arreglo
print (regresiva(5)) 

#IMPRIMIR Y DEVOLVER 
def print_and_devolver(list):
    print(list[0])
    return list[1]
print(print_and_devolver([1,2]))

#PRIMERO MAS LONGITUD 
def primer_plus_length(list):
    return list[0] + len[list]
print(primer_plus_length([1,2,3,4,5]))


#VALORES MAYORES QUE EL SEGUNDO 
def valores_mayor_que_el_segundo(list):
    if len(list) < 2:
     return False
    output = []
    for i in range(0, len(list)):
      if list [i] > list [1]:
        output.append[i](list[i])
    print(len(output))
    return output    
print(valores_mayor_que_el_segundo([5,2,3,2,1,4]))
print(valores_mayor_que_el_segundo([3]))

#ESTA LONGITUD, ESE VALOR 
def longitud_valor(size,value):
    output = []
    for i in range(0, size):
        output.append(value)
    return output

print(longitud_valor(4,7))
print(longitud_valor(6,2))
