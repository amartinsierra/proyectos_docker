Se trata de crear una aplicación que al iniciarse pregunte al usuario si quiere añadir datos de una persona o mostrar lista de personas almacenadas. Si elige la primera, se le solicita el nombre, email y edad y se guardará la persona en una base de datos interna y ahí acabará la aplicación, si elige la segunda se mostrará los datos de todas las personas que haya almacenado en el pasado.
Se desarrollarán  dos versiones de la aplicación, una en Java y otra en python usando un gestor de base de datos lo más simple posible(SQLite).
Después, habrá que desplegar esas aplicaciones en contenedores docker (una imagen por aplicación). Usaremos una imagen linux simple (en realidad dos) y montar sobre cada una base de ellas el software necesario para la ejecución de las aplicaciones, incluida la base de datos (la más ligera posible). 


Imagen:
>docker build -t imgpersonas .

Contenedor:
>docker run --name personas -v datos:/datos imgpersonas