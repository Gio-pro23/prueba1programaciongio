##ejercicio1

notas_mate=[]
notas_lengua=[]
notas_prog=[]

nota=input("ingresar notas de matematica (escribir listo en el caso que quieras terminar):")
while nota != "listo": ##osea mientras q nota ! lsito (osea q no sea igual a listo pq el ! es eso)
    nota = float(nota)   ##float para q sea decimal jjs
    if nota >=0 and nota <=10:
        notas_mate.append(nota)
    else:
        print("la nota tiene q estar entree 0 y 10")
    nota=input("ingresar notas de matematica (escribir listo en el caso que quieras terminar):")


nota=input("ingresar notas de lengua (escribir listo en el caso que quieras terminar):")
while nota != "listo":
    nota = float(nota)
    if nota >=0 and nota <=10:
        notas_lengua.append(nota)
    else:
        print("la nota tiene q estar entree 0 y 10")
    nota=input("ingresar notas de lengua (escribir listo en el caso que quieras terminar):")



nota=input("ingresar notas de programacion (escribir listo en el caso que quieras terminar):")
while nota != "listo":
    nota = float(nota)
    if nota >=0 and nota <=10:
        notas_prog.append(nota)
    else:
        print("la nota tiene q estar entree 0 y 10")
    nota = input("ingresar notas de programacion (escribir listo en el caso que quieras terminar):")


def calcular_promedio(lista,nombre):
   if len(lista) > 0: ##si tpodads las notas son mayores q 10 y menores que 0 
      suma=0 ##tiene q ser 0 asi va sumando cada nota segun yo pq siempre haciamos eso
      for i in lista:
        suma = suma + i

      promedio = suma / len(lista) ##la suma de cada una se divide por la cant de notas pq bueno el len ess lo q muestra lo q hay en la lista jsja   
      print(f"promedio de {nombre}:{promedio}")

      if promedio > 7:
           print("aprobado :)")
      else:
           print("desaprobado ;()")
   else:
        print("no hay notas")


###ahora para calcular td
calcular_promedio(notas_mate, "matematica:")
calcular_promedio(notas_lengua, "lengua")
calcular_promedio(notas_prog, "programacion:")

   
    