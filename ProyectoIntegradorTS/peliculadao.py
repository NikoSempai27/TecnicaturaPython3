import psycopg2
from dominio.pelicula import Pelicula

class PeliculaDAO:
    def __init__(self):
        self.conexion = None

    def conectar(self):
        try:
            self.conexion = psycopg2.connect(
                host='127.0.0.1',
                database='pelicat',
                user='postgres',
                password='postgres'
                )
            print('Conexión exitosa a la base de datos')
        except Exception as e:
            print(f'Ocurrio un error al conectar a la base de datos: {e}')


    def desconectar(self):
        if self.conexion:
            self.conexion.close()
            print('Desconexión exitosa de la base de datos')

    def obtener_pelicula(self, pelicula_id):
        try:
            with self.conexion:
                with self.conexion.cursor() as cursor:
                    cursor.execute("SELECT * FROM peliculas WHERE pelicula_id = %s", (pelicula_id,))
                    pelicula = cursor.fetchone()
                    if pelicula:
                        retorno = Pelicula(*pelicula)
                        retorno.pelicula_id = pelicula_id
                        return retorno
        except Exception as e:
            print(f'Ocurrio un error al obtener la película:{e}')

    def insertar_pelicula(self, pelicula):
        try:
            with self.conexion:
                with self.conexion.cursor() as cursor:
                    query = """
                        INSERT INTO peliculas (titulo, director, anio, medio, comentario, clasificacion_id, categoria_id)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """
                    cursor.execute(query, (
                        pelicula.titulo,
                        pelicula.director,
                        pelicula.anio,
                        pelicula.medio,
                        pelicula.comentario,
                        pelicula.clasificacion_id,
                        pelicula.categoria_id
                    ))
            print('Película insertada correctamente')
        except Exception as e:
            print(f'Ocurrio un error al insertar la película: {e}')

    def ver_peliculas(self):
        try:
            with self.conexion:
                with self.conexion.cursor() as cursor:
                    query = "SELECT * FROM peliculas"
                    cursor.execute(query)
                    peliculas = cursor.fetchall()
            print("Peliculas:")
            for pelicula in peliculas:
                print(pelicula)
        except Exception as e:
            print("Ocurrio un error al obtener las películas:", e)

    def eliminar_pelicula(self, pelicula_id):
        try:
            with self.conexion:
                with self.conexion.cursor() as cursor:
                    query = "DELETE FROM peliculas WHERE pelicula_id = %s"
                    cursor.execute(query, (pelicula_id,))
            print("Película eliminada correctamente")
        except Exception as e:
            print("Ocurrio un error al eliminar la película:", e)

    def modificar_pelicula(self, pelicula):
        try:
            with self.conexion:
                with self.conexion.cursor() as cursor:
                    query = """
                        UPDATE peliculas
                        SET titulo = %s, director = %s, anio = %s, medio = %s, comentario = %s, clasificacion_id = %s, categoria_id = %s
                        WHERE pelicula_id = %s
                    """
                    cursor.execute(query, (
                        pelicula.titulo,
                        pelicula.director,
                        pelicula.anio,
                        pelicula.medio,
                        pelicula.comentario,
                        pelicula.clasificacion_id,
                        pelicula.categoria_id,
                        pelicula.pelicula_id
                    ))
            print("Película modificada correctamente")
        except Exception as e:
            print(f'Ocurrio un error al modificar la película: {e}')
