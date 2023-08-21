from dominio.pelicula import Pelicula
from peliculadao import PeliculaDAO

def main():
    pelicula_dao = PeliculaDAO()
    pelicula_dao.conectar()

    while True:
        print("***** MENÚ *****")
        print("1. Ver todas las películas")
        print("2. Ingresar una nueva película")
        print("3. Modificar una película")
        print("4. Eliminar una película")
        print("5. Salir")
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            pelicula_dao.ver_peliculas()
        elif opcion == "2":
            titulo = input("Ingrese el título de la película: ")
            director = input("Ingrese el director de la película: ")
            anio = input("Ingrese el año de la película: ")
            medio = input("Ingrese el medio de la película: ")
            comentario = input("Ingrese un comentario a la película: ")
            clasificacion_id = input("Ingrese el ID de clasificación de la película: ")
            categoria_id = input("Ingrese el ID de categoría de la película: ")

            pelicula = Pelicula(titulo, director, anio, medio, comentario, clasificacion_id, categoria_id)
            pelicula_dao.insertar_pelicula(pelicula)
        elif opcion == "3":
            pelicula_id = input("Ingrese el ID de la película a modificar: ")
            pelicula = pelicula_dao.obtener_pelicula(pelicula_id)
            if pelicula:
                print("Datos de la película:")
                print(pelicula)
                titulo = input('Ingrese el nuevo título de la película (presione Enter para mantener el actual): ')
                director = input('Ingrese el nuevo director de la película (presione Enter para mantener el actual): ')
                anio = input('Ingrese el nuevo año de la película (presione Enter para mantener el actual): ')
                medio = input('Ingrese el nuevo medio de la película (presione Enter para mantener el actual): ')
                comentario = input('Ingrese el nuevo comentario de la película (presione Enter para mantener el actual): ')
                clasificacion_id = input('Ingrese el nuevo ID de clasificación de la película (presione Enter para mantener el actual): ')
                categoria_id = input('Ingrese el nuevo ID de categoría de la película (presione Enter para mantener el actual): ')

                if titulo:
                    pelicula.titulo = titulo
                if director:
                    pelicula.director = director
                if anio:
                    pelicula.anio = anio
                if medio:
                    pelicula.medio = medio
                if comentario:
                    pelicula.comentario = comentario
                if clasificacion_id:
                    pelicula.clasificacion_id = clasificacion_id
                if categoria_id:
                    pelicula.categoria_id = categoria_id

                pelicula_dao.modificar_pelicula(pelicula)
            else:
                print('No se encontró una película con el ID especificado.')
        elif opcion == "4":
            pelicula_id = input('Ingrese el ID de la película a eliminar: ')
            pelicula_dao.eliminar_pelicula(pelicula_id)
        elif opcion == "5":
            break
        else:
            print('Opción no válida. Por favor, ingrese un número de opción válido.')

    pelicula_dao.desconectar()

if __name__ == "__main__":
    main()
