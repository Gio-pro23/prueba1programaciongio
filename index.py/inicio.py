##ejercicio1

notas=[]
notas=input("ingresar notas(escribir listo para terminar):")
if notas=="listo":
    break


nota=float ##para q sea decimal,obvio

if nota >=0 and <=10:
    notas.append(nota)
else:
    print("la nota tiene q estar entree 0 y 10")
    if len(notas) >=0 ##si tpodads las notas son mayores q 10 y menores que 0 

    suma=0 ##tiene q ser 0 asi va sumando cada nota segun yo pq siempre haciamos eso
    for i in notas:
        suma=suma /len(notas) ##la suma de cada una se divide por la cant de notas pq bueno el len ess lo q muestra lo q hay en la lista jsja

    print("el promedio es:",suma)

    print("probando git hub, ndqv con la prueba")

