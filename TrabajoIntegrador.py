#Clase paises (no se si esta bien armada)
class Pais:
    def __init__(self,nombre,poblacion,superficie,continente):
        self.nombre = nombre
        self.poblacion = poblacion
        self.superficie = superficie
        self.continente = continente

    #Esto muestra todos los paises cargados hasta el momento, despues se borra
    def mostrarPaises(self):
        print ()
        print(f"Nombre: {self.nombre}")
        print(f"Poblacion: {self.poblacion}")
        print(f"Superficie: {self.superficie}")
        print(f"Continente: {self.continente}")
        print()

#Funcion para abrir el archivo csv y crear la clase pais junto con sus atributos
def archivoCSV():
    listaPaises = []
    with open("Paises.csv","r") as paises:
        for linea in paises:
            lista = linea.strip().split(",")
            nombre = lista[0]
            poblacion = int(lista[1])
            superficie = int(lista[2])
            continente = lista[3]
            #Cargamos cada dato en una variable y esta la mandamos a la clase Pais para crear sus atributos
            pais = Pais(nombre,poblacion,superficie,continente)
            #Despues de creada la cargamos a la lista paises que sera retornada al main
            listaPaises.append(pais)
        return listaPaises

#Menu de Funciones 
def menu(paises):
    while True:
        try:
            opcion = int(input("Bienvenido, seleccione una de las siguiente opciones a realizar(ingrese el numero de la opcion)\n1) Mostrar Paises cargados\n2) Buscar un Pais\n3) Filtrar Paises\n"
            "4) Ordenar Paises\n5) Agregar pais\n6) Borrar pais\n7) Mostrar estadisticas\n8) Salir\n"))
            if opcion == 1:
                for pais in paises:
                    pais.mostrarPaises()
            elif opcion == 2:
                buscarPais(paises)
            elif opcion == 3:
                filtrarPaises(paises)
            elif opcion == 4:
                print("Completar funcion")
            elif opcion == 5:
                agregarPais(paises)
            elif opcion == 6:
                print("Completar funcion")
            elif opcion == 7:
                print("Completar funcion")
            elif opcion == 8:
                print("Hasta Luego")
                break
            else:
                print("Error opcion invalida, vuelva a intentar")
        except:
            print("Error, ingrese un numero con las opciones disponibles") 
    
#Funcion que busca coincidencia con un pais
def buscarPais(paises):
    while True:
        try:
            buscar = input("Ingrese el nombre del pais que desea buscar o s si no quiere continuar: ").lower().replace(" ","")
            if buscar == "s":
                break
            else:
                for pais in paises:
                    if pais.nombre == buscar:
                        print("Pais encntrado, estos son los datos: ")
                        pais.mostrarPaises()
                        #Consultar si terminar la funcion una vez haya encontrado el pais buscado o que vuelva al principio de la función (break o return)
                        return
                else:
                    print(f"No se ah encontrado ningun pais con el nombre {pais}")
        except:
            print("Opcion invalida, vuelva a intentar")

def filtrarPaises(paises):
    while True:
        try:
            opcion = int(input("¿Como desea filtrar los paises?\n1) Por Continente\n2) Por Rango de Poblacion\n3) Por rango de superficie\n4) Regresar al Menu\n"))
            if opcion == 1:
                filtrarPorContinente(paises)
            elif opcion == 2:
                rangoNumeros(paises,"poblacion")
            elif opcion == 3:
                rangoNumeros(paises,"superficie")
            elif opcion == 4:
                break
            else:
                print("Error, ingrese una opcion valida")
        except:
            print("Error, ingrese un numero valido")

#Funcion que se encarga de filtrar los paises con el mismo continente
def filtrarPorContinente(listaPaises):
    continentes = ["america","europa","asia","africa","oceania"]
    bandera = False
    while True:
        buscar = input("Ingrese el nombre del continente para filtrar, o si desea regresar ingrese s: ").lower().replace(" ","")
        if buscar == "s":
            return
        elif buscar in continentes:
            print(f"El continente {buscar} si existe, esta es la lista de los paises dentro de ese continente: ")
            for pais in listaPaises:
                if buscar == pais.continente:
                    pais.mostrarPaises()
                    bandera = True
            if bandera == False: print(f"No se encuentra ningun pais con el continente {buscar}")
            break
        else: 
            print(f"No existe un continente con el nombre {buscar}")

#Funcion que se encarga de corroborar que los numeros sean positivos y comprobar el menor y mayor de ellos
def rangoNumeros(listaPaises,dato): 
    print("Ingrese un primer numero")
    numeros1 = validarNumeros()
    while True:
        print("Ahora ingrese un numero mayor o menor al anterior")
        numeros2 = validarNumeros()
        if numeros1 == numeros2:
            print("Error, ambos numeros no pueden tener el mismo valor. Ingrese nuevamente el segundo numero")
        elif numeros1 > numeros2:
            filtrarPaisPorPoblacionOSuperficie(listaPaises,dato,numeros2,numeros1)
        else:
            filtrarPaisPorPoblacionOSuperficie(listaPaises,dato,numeros1,numeros2)
        break

#Funcion que filtra la informacion segun poblacion o superficie
def filtrarPaisPorPoblacionOSuperficie(listaPaises,dato,menor,mayor):
    bandera = False
    if dato == "poblacion":
        for pais in listaPaises:
            if menor <= pais.poblacion <= mayor:
                pais.mostrarPaises()
                bandera = True
    else:
        for pais in listaPaises:
            if menor <= pais.poblacion <= mayor:
                pais.mostrarPaises()
                bandera = True
    if bandera == False: print(f"No se encuentra ningun pais entre el rango {menor} y {mayor}")

#Funcion para agregar un pais nuevo
def agregarPais(listaPaises):
    #Validamos que el nombre del pais sean letras y no numeros o caracteres
    while True:
        nombre = input("Ingrese el nombre del pais que desea agregar\n").lower().replace(" ","")
        if not nombre.isalpha():
            print("Error, ingrese un nombre sin numeros o caracteres")
        else: 
            break
    #Llamamos a la funcion para la poblacion y la superficie
    print(f"Ingrese la poblacion del pais {nombre}")
    poblacion = validarNumeros()
    print(f"Ingrese la superficie del pais {nombre}")
    superficie = validarNumeros()
    #Verificamos que el continente sea correcto y que exista
    continentes = ["america","europa","asia","africa","oceania"]
    while True:
        continente = input("Ingrese el continente al que pertenece el pais\n").lower().replace(" ","")
        if continente.isalpha() and continente in continentes:
            break
        else:
            print(f"Error, el pais {nombre} contiene algun caracter/numero o no ingreso un continente existente")
    #Una vez todos los datos se hayan obtenido y no tengan fallos estos son cargados al archivo Paises.csv y se llama a la funcion archivoCSV para actualizar la lista
    with open("Paises.csv","a") as paises:
        paises.write("\n"+f"{nombre},{poblacion},{superficie},{continente}")
        pais = Pais(nombre,poblacion,superficie,continente)
        listaPaises.append(pais)
        
#Funcion que unicamente se encarga de validar que los numeros de la poblacion y superficie no sean negativos o nulos
def validarNumeros():
    while True:
            try:
                respuesta = int(input())
                if respuesta <= 0:
                    print("Error, no puede ingresar una numero negativo")
                    print("Ingrese nuevamente la informacion del pais")
                else:
                    return respuesta
            except:
                print("Error ingrese un numero")

#Main
if __name__ == "__main__":
    paises = archivoCSV()
    menu(paises)