#Clase paises (no se si esta bien armada)
class Pais:
    def __init__(self,nombre,poblacion,superficie,continente):
        self.nombre = nombre
        self.poblacion = poblacion
        self.superficie = superficie
        self.continente = continente

    #Esto solo esta de muestra, despues se borra
    def mostrar_info(self):
        print(f"País: {self.nombre}")
        print(f"  Capital: {self.superficie}")
        print(f"  Población: {self.poblacion}")
        print(f"  Continente: {self.continente}")
        print()

#Funcion para abrir el archico csv y crear la clase pais junto con sus atributos
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

def menu(paises):
    while True:
        try:
            opcion = int(input("Bienvenido, seleccione una de las siguiente opciones a realizar(ingrese el numero de la opcion)\n1) Buscar un Pais\n2) Filtrar Paises\n"
            "3) Ordenar Paises\n4) Agregar pais\n5) Borrar pais\n6) Mostrar estadisticas\n7) Salir\n"))
            if opcion == 1:

            elif opcion == 2:

            elif opcion == 3:

            elif opcion == 4:

            elif opcion == 5:

            elif opcion == 6:

            elif opcion == 7:
                print("Hasta Luego")
                break
            else:
                print("Error opcion invalida, vuelva a intentar")
        except:
            print("Error, ingrese un numero con las opciones disponibles") 
    

#Main, mostramos hasta ahora los paises para ver si fueron bien cargados
if __name__ == "__main__":
    paises = archivoCSV()
    for pais in paises:
        pais.mostrar_info()
    menu(paises)