COMANDOS
    - BASH
        - para listar os usuarios do sistema
        * apartir do usuario com id 1000, são utilizaveis
        /# cat /etc/passwd

        - para verificar qual usuario esta sendo utilizado
        whoimi

        - para verificar de qual usuario pertence os arquivos do path
        ls -la

        - alterando o dono do arquivo
        * verifica o uso do SUDO em caso de não ser o root
        chown {de usuario}:{para usuario} {nomearquivo.extensão}

        - executando o minimo no linux para manter o container rodando
        tail -f /dev/null

        - verificar todos processos rodando no momento
        ps aux
    

    - DOCKER
        - listando container
        docker ps

        - executando comandos dentro do container
        * para abrir um terminal do container incluimos o -it
        docker exec {nome do container} {comandos}
        docker exec -t {nome do container} bash

        - para iniciar o conteiner com usuario root
        docker compose exec -u root app bash

        - sempre atualizar os pacotes
        apt update

        - script shell para verificar o arquivo .env
        * crie um arquivo .env-example
        if [ ! -f ".env" ]; then
            cp .env-example .env
        fi

        - mesclar configs .yaml
        docker compose -f {arquivo1.yaml} {arquivo2.yaml}

        - em criação de volumes é possível incluirmos um :cache para agilizar a criação
        .:home/node/app:cached

        - criamos um container apartir de uma imagem base, como por exemplo uma que ja possui python com pip
        - para baixar imagem do docker hub
        docker pull {nome da tag}

        - nomeando a imagem criada
        docker build -t {nome da imagem}:{nome da tag} {diretorio}

        - para criar container
        * o uso do -t é para referenciar o terminal, será utilizando em background
        * o uso do -P é para mapear a porta do EXPOSE do docker file para minha aplicação
        docker run -d -P {nome da imagem}:{tag}

        - verificando logs do container
        * se incluido o -f ele ficará aberto em tempo real para visualização
        docker logs {nome do container}

1. Select a version compatible with application
    """
    FROM {language}:{version (docker hub)}
    """

2. Choose a work path
* selecionar de preferencia a mesma pasta do seu sistema para conter as mesmas permissoes
    """
    WORKDIR {path}
    """

3. Specify the user
* importante selecionar o usuario para que possuam as mesmas permissões para editar os arquivos
    """
    USER {username}
    """