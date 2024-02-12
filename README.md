# command for generate secret key
    python -c "import secrets; print(secrets.token_urlsafe(38))" 

# command for docker
    verificar as configurações do yml:
        docker compose -f local.yml config

    exportando plataforma de uso no docker:
        export DOCKER_DEFAULT_PLATAFORM=linux/arm64
    
    subindo arquivo yml para criar imagem docker:
        docker compose -f local.yml up --build -d --remove-orphans
    
    verificando logs
        docker compose -f local.yml logs {name docker}
    
    inspecionando volumes do docker
        docker volume inspect src_local_postgres_data

    desconectando docker
        docker compose -f local.yml down
    
    executando scripts .sh
        docker compose -f local.yml exec postgres backup

# Arquivo .sh
    Executamos scripts com usando shebang, e incluimos os comandos para realizar os backups

# command postgres
    listando databases
    \list

    conectando db
    \connect

    listando tabelas do db
    \dt

    fechar db
    \q

# criando arquivo ssh
    ssh-keygen

# check de domain
    whatsmydns.net