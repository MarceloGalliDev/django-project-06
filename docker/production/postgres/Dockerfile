FROM postgres:15-bullseye

# fazendo copia de backup do banco de dados
COPY ./docker/production/postgres/maintenance /usr/production/bin/maintenance

# obtendo privilegios
RUN chmod +x /usr/production/bin/maintenance/*

# movendo arquivo de backup
RUN mv /usr/production/bin/maintenance/* /usr/production/bin \
    && rmdir /usr/production/bin/maintenance