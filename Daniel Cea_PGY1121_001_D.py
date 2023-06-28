import os
os.system("cls")

encomiendas=[]
nombre=[]
def grabar_encomienda():
    nombre = input("ingrese el nombre del destinatario: ")
    direccion = input("ingrese la direccion de a entrega: ")
    descripcion = input("ingrese una descripcion de la encomienda: ")

    encomienda = {'nombre':nombre,'direccion':direccion,'descripcion':descripcion}

encomiendas.append(encomiendas)
print("Encomienda grabada con exito")

def buscar_encomienda():
    nombre = input("ingrese el nombre del destinatario a buscar: ")

for encomienda in encomiendas:
    if encomiendas['Nombre'] == (nombre):
        print("Encomienda encontrada: ")
        print(f"nombre:{encomiendas['Nombre']}")
        print(f"Direccion:{encomiendas['Direccion']}")
        print(f"Descripcion:{encomiendas['Descripcion']} ")
        
    
    print("Encomienda no encontrada.")

def listar_encomiendas():
    if not encomiendas:
        print("No hay encomiendas regisradas. ")
        return                                                              

print("lista de encomiendas:")
for encomienda in encomiendas:
    print(f"Nombre:{encomienda['Nombre']}")
    print(f"Direccion:{encomienda['Direccion']}")
    print(f"Descricpcion:{encomienda['Descripcion']}")
    print("--------------------------")

    def menu():
        while True:
            print("Menu de encomiendas")
            print("1. Grabar encomienda")
            print("2. Buscar encomienda")
            print("3. Listar encomienda")
            print("4. Salir")

opcion = input("Seleccione una opcion: ")
if opcion == '1':
    grabar_encomienda()
elif opcion == '2':
    buscar_encomienda()
elif opcion == '3':
    listar_encomiendas()
elif opcion == '4':
    print(" Hasta luego ")
    
else:
    print("Opcion invalida, intente nuevamente.")
    menu()









