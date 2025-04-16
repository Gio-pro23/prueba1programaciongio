##ejercicio1

notas=[]

nota=input("ingresar notas de matematica (escribir listo en el caso que quieras terminar):")
while nota != "listo":
    nota = float(nota)   ##float para q sea decimal jjs
    if notas >=0 and <=10:
        notas.append(nota)
    else:
        print("la nota tiene q estar entree 0 y 10")


nota=input("ingresar notas de lengua (escribir listo en el caso que quieras terminar):")
while nota != "listo":
    nota = float(nota)
    if notas >=0 and <=10:
        notas.append(nota)
    else:
        print("la nota tiene q estar entree 0 y 10")



nota=input("ingresar notas de programacion (escribir listo en el caso que quieras terminar):")
while nota != "listo":
    nota = float(nota)
    if notas >=0 and <=10:
        notas.append(nota)
    else:
        print("la nota tiene q estar entree 0 y 10")



if len(notas) >=0 ##si tpodads las notas son mayores q 10 y menores que 0 
    suma=0 ##tiene q ser 0 asi va sumando cada nota segun yo pq siempre haciamos eso
    for i in notas:
        suma=suma + i
        promedio=suma /len(notas) ##la suma de cada una se divide por la cant de notas pq bueno el len ess lo q muestra lo q hay en la lista jsja   
        print("promedio:",promedio)

        if promedio > 7:
        print("aprobado :)")
        else:
        print("desaprobado ;()")
else print("no hay notas")
   
    