# ASE Docker

Uma tentativa de montar um container simples de Sybase

## Construindo a imagem localmente para desenvolvimento

    git clone git@github.com:USERNAME/asedocker.git
    cd asedocker

Baixar o tar.gz do ASE e nomeá-lo ASE_Suite.linuxamd64.tgz e
colocar na raiz de `asedocker`, depois rodar:

    docker build -t ase .
    docker run --detach --hostname sybase ase

Descobrir o id e na sequência o IP:

    docker ps -a
    docker container inspect <ID>| grep -i IPAddress

Depois da imagem construída, da sua máquina, acessar o sybase:

    sudo apt install freetds-bin
    tsql -H <IP> -p 5000 -U sa -P Sybase123456789

Se quiser acessar o shell do container:

    docker exec -i -t <ID> /bin/bash

Limpando ambiente:

    docker stop <ID>
    docker rm <ID>

Criando uma banco de exemplo:

    tsql -H <ip> -p 5000 -U sa -P Sybase123456789 < database.sql

## Publicando no docker hub

Login:

    docker login

Pegar o <id> da máquina que irá subir em:  

    docker ps -a

Commit image:

    docker commit <id> uspdev/asedocker

Taggear:

    docker images
    docker tag <IMAGE ID> uspdev/asedocker:1.0.0

Push:

    docker push uspdev/asedocker


