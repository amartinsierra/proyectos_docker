Imagen:
>docker build -t migitea .
contenedor:
>docker run -d --name contgitea -p 3010:3000 -e GITEA__security__INSTALL_LOCK=true -v gitea-data:/data migitea