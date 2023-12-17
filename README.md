# command for generate secret key
    python -c "import secrets; print(secrets.token_urlsafe(38))" 

# command for docker
    verificar as configurações do yml:
        docker compose -f local.yml config

    exportando plataforma de uso no docker:
        export DOCKER_DEFAULT_PLATAFORM=linux/arm64
    
    subindo arquivo yml para criar imagem docker:
        docker compose -f local.yml up --build -d --remove-orphans