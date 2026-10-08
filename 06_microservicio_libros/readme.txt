Imagen:
>docker build -t imglibros .
contenedor:
>docker run --name libros -e SERVER_DB=192.168.1.18 -e PASS_DB=root -p 9500:8500 imglibros