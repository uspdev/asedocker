# ASE Docker
Uma tentativa de montar um container simples de Sybase

## Uso
<code bash>
# baixar o tar.gz do ASE e nomeá-lo ASE_Suite.linuxamd64.tgz
docker build -t ase .
docker run --detach --hostname sybase ase
# descobrir o IP via
docker container inspect <ID>
</code>
