# Inicialização e Configuração do Docker

**Note:** Todos os comandos à seguir devem ser executados no terminal

## Postgres

- Configurando a imagem do postgres

```bash
docker run \
    --name postgres \
    -e POSTGRES_USER=dbadmin \
    -e POSTGRES_PASSWORD=123mudar \
    -e POSTGRES_DB=realdb \
    -p 5432:5432 \
    -d \
    postgres
```

- Ver as imagens instaladas na máquina
  docker ps -a

* Entrar no container postgres

```bash
docker exec -it postgres /bin/bash
```

- Após entrar no container postgres, roda o comando abaixo para iniciar a interface

```bash
docker run \
    --name adminer \
    -p 8080:8080 \
    --link postgres:postgres \
    -d \
    adminer
```

## MongoDB

- Configurando a imagem do MongoDB

```bash
docker run \
    --name mongodb \
    -p 27017:27017 \
    -e MONGO_INITDB_ROOT_USERNAME=dbadmin \
    -e MONGO_INITDB_ROOT_PASSWORD=123mudar \
    -d \
    mongo
```

- Configurando um Client para o MongoDB

```bash
docker run \
    --name mongoclient \
    -p 3000:3000 \
    --link mongodb:mongodb \
    -d \
    mongoclient/mongoclient
```

- Cria um usuário (admin) para acessar o mongo, também criar um banco de dados (realdb) e realiza o login no mesmo

```bash
docker exec -it mongodb \
  mongo --host localhost -u dbadmin -p 123mudar --authenticationDatabase admin \
  --eval "db.getSiblingDB('realdb').createUser({user: 'realuser', pwd: '123mudar', roles: [{role: 'readWrite', db: 'realdb'}]})"
```

---

## Outros comandos necessários do docker

- Para Ver todas as imagens que estão na máquina:

```bash
docker ps -a
```

- Para Iniciar uma imagem que está instalada na máquina:

```bash
docker start id_ou_nome_da_imagem
```

- Para Parar uma imagem que está instalada na máquina:

```bash
docker stop id_ou_nome_da_imagem
```

- Para Remover uma imagem da máquina:

```bash
docker rm id_ou_nome_da_imagem
```
