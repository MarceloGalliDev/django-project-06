FROM nginx:1.25.3-alpine

# removendo confuguração padrão da image do nginx
RUN rm /etc/nginx/conf.d/default.conf

# carregando arquivo de configuração e copiando para o destino
COPY ./default.conf /etc/nginx/conf.d/default.conf
