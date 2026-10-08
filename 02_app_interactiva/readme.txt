Creación imagen:
>docker build -t imginteractiva .

Creación de contenedor:

>docker run --name interactivo -it imginteractiva 

Etiquetado de imagen:
>docker tag imginteractiva ajms66/cursodocker:interactiva

Autenticación en docker hub:
>docker login -u usuario

Subida de imagen a docker hub:
>docker push ajms66/cursodocker:interactiva