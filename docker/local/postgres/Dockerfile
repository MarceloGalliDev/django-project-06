FROM postgres:15-bullseye

# fazendo copia de backup do banco de dados
COPY ./docker/local/postgres/maintenance /usr/local/bin/maintenance

# obtendo privilegios
RUN chmod +x /usr/local/bin/maintenance/*

# movendo arquivo de backup
RUN mv /usr/local/bin/maintenance/* /usr/local/bin \
    && rmdir /usr/local/bin/maintenance