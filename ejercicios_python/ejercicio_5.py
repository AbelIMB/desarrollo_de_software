peliculas=[]
pelicula = {}

def cargar_peliculas(peliculas):
    nombre = input("Ingrese nombre de pelicula: ")
    anio = input("Ingrese año de estreno: ")

    pelicula = {"anio":anio, "nombre": nombre}
    peliculas.append(pelicula)

def mostrar_peliculas(peliculas):
    print("Resultado: ")
    peliculas.sort(key=lambda pelicula: pelicula["anio"])
    for pelicula in peliculas: 
        print(f"{pelicula['nombre']}")

if __name__ == '__main__':
    import sys

tamanio = 0
while 6 > tamanio:
    cargar_peliculas(peliculas)
    tamanio = len(peliculas)

mostrar_peliculas(peliculas)
    
'''
Ingrese nombre de pelicula: Batman inicia
Ingrese año de estreno: 2008
Resultado: 
[“300”, “Avatar”, “Batman Inicia”, “Iron Man”, “Tropic Thunder”]
{2005: “Batman Inicia”, 2006: “300”, 2008: “Tropic Thunder”, “Iron Man”}
'''