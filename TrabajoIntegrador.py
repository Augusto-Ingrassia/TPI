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
            poblacion = lista[1]
            superficie = lista[2]
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
            opcion = int(input("¿Como desea filtrar los paises?\n1) Por Continente\n2) Por Rango de Poblacion\n3)Por rango de superficie"))
            if opcion == 1:

            elif opcion == 2:

            elif opcion == 3:

            else:
                print("Error, ingrese una opcion valida")
        except:
            print("Error, ingrese un numero valido")

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