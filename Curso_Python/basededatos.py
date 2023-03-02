import getpass
import sqlite3

def main():
    crear_usuario(4, 'pepe', 'contraseña')
def main2():
    username = input('Nombre de usuario: ')
    password = getpass.getpass('Contraseña: ')
    
    if verifica_credenciales(username, password):
        print('Login correcto')
    else:
        print('Error al iniciar sesion')

def verifica_credenciales(username, password):
    conn = sqlite3.connect('Curso_Python/miaplicacion.db')
    cursor = conn.cursor()
    
    query = f'SELECT id FROM users WHERE username=\'{username}\' AND password=\'{password}\';'
    print('query a ejecutar', query)
    
    rows = cursor.execute(query)
    #fetchone devuelve 1 elemento
    data = rows.fetchone()
    
    cursor.close()
    conn.close()
    
    if data == None:
        return False    
    
    return True


def crear_usuario(identificador, usuario, clave):
    conn = sqlite3.connect('Curso_Python/miaplicacion.db', isolation_level=None)
    cursor = conn.cursor()
    
    query = f'INSERT INTO users(id, username, password) VALUES({identificador}, \'{usuario}\', \'{clave}\')'
    print('query a ejecutar', query)
    
    rows = cursor.execute(query)
    print(type(rows))
    
    #cuando se hace delete o insert se tiene que commiterar
    #conn.commit()
    
    cursor.close()
    conn.close()
    



if __name__ == '__main__':
    main()

