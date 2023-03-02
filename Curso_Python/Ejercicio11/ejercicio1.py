import sqlite3

def main():
    conn = sqlite3.connect('Curso_Python/Ejercicio11/ej1.db')
    cursor = conn.cursor()
    
    cursor.execute('CREATE TABLE Alumnos(Id INT, Nombre TEXT, Apellido TEXT)')    
    
    cursor.execute('INSERT INTO Alumnos(Id, Nombre, Apellido) VALUES(1, "fran", "Vigna")')    
    cursor.execute('INSERT INTO Alumnos(Id, Nombre, Apellido) VALUES(2, "ivi", "barrios")')    
    cursor.execute('INSERT INTO Alumnos(Id, Nombre, Apellido) VALUES(3, "nahuel", "villa")')    
    cursor.execute('INSERT INTO Alumnos(Id, Nombre, Apellido) VALUES(4, "juan", "perez")')    
    cursor.execute('INSERT INTO Alumnos(Id, Nombre, Apellido) VALUES(5, "juanito", "gil")')    
    cursor.execute('INSERT INTO Alumnos(Id, Nombre, Apellido) VALUES(6, "santu", "roldan")')    
    cursor.execute('INSERT INTO Alumnos(Id, Nombre, Apellido) VALUES(7, "julian", "alvarez")')    
    cursor.execute('INSERT INTO Alumnos(Id, Nombre, Apellido) VALUES(8, "messi", "messi")')    


    conn.commit()
    cursor.execute('SELECT * FROM Alumnos WHERE Nombre = "fran" ')    
    
    rows = cursor.fetchall()
    
    print(rows)

    
    
    
    cursor
    cursor.close()
    conn.close()




if __name__ == '__main__':
    main()