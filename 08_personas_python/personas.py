import sqlite3

DB = "/datos/personas.db"


def crear_tabla():
    conexion = sqlite3.connect(DB)

    conexion.execute("""
        CREATE TABLE IF NOT EXISTS personas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL,
            edad INTEGER NOT NULL
        )
    """)

    conexion.commit()
    conexion.close()


def anadir_persona():
    nombre = input("Nombre: ")
    email = input("Email: ")
    edad = int(input("Edad: "))

    conexion = sqlite3.connect(DB)

    conexion.execute(
        """
        INSERT INTO personas (nombre, email, edad)
        VALUES (?, ?, ?)
        """,
        (nombre, email, edad)
    )

    conexion.commit()
    conexion.close()

    print("Persona almacenada correctamente.")


def mostrar_personas():
    conexion = sqlite3.connect(DB)

    cursor = conexion.execute(
        "SELECT id, nombre, email, edad FROM personas"
    )

    personas = cursor.fetchall()

    conexion.close()

    print()
    print("PERSONAS ALMACENADAS")
    print("--------------------")

    if not personas:
        print("No hay personas almacenadas.")
        return

    for persona in personas:
        id_persona, nombre, email, edad = persona

        print(
            f"{id_persona} - {nombre} - {email} - {edad} años"
        )


def main():
    crear_tabla()

    print("1. Añadir persona")
    print("2. Mostrar personas")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        anadir_persona()
    elif opcion == "2":
        mostrar_personas()
    else:
        print("Opción no válida")


if __name__ == "__main__":
    main()

