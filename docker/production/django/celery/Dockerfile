ARG PYTHON_VERSION=3.11.7-bullseye

FROM python:${PYTHON_VERSION} as python

FROM python as python-build-stage
ARG BUILD_ENVIRONMENT=production

# o uso do RUN é para executar comandos dentro do container
# o uso do -y é para evitar a pergunta se deseja instalar, ele ja da YES direto
RUN apt-get update && apt-get install --no-install-recommends -y \
   build-essential \
   libpq-dev 

# o uso do COPY é usado como copia do dado local para o container
COPY ./requirements .

RUN pip wheel --wheel-dir /usr/src/app/wheels \
   -r ${BUILD_ENVIRONMENT}.txt


FROM python as python-run-stage

ARG BUILD_ENVIRONMENT=production
ARG APP_HOME=/app

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

ENV BUILD_ENV ${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

# here creates a new system group for django
RUN addgroup --system django && \
    adduser --system --ingroup django django && \
    mkdir -p ${APP_HOME}/staticfiles && \
    chown django:django ${APP_HOME}/staticfiles
    chmod 775 ${APP_HOME}/staticfiles

RUN apt-get update && apt-get install --no-install-recommends -y \
    libpq-dev \
    gettext \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*


COPY --from=python-build-stage /usr/src/app/wheels /wheels/

RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
   && rm -rf /wheels/

# aqui copiamos o script entrypoint depois executamos com chmod para permissoes
COPY ./docker/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY ./docker/local/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./docker/local/django/celery/flower/start /start-flower
RUN sed -i 's/\r$//g' /start-flower
RUN chmod +x /start-flower

COPY . ${APP_HOME}

ENTRYPOINT ["/entrypoint"]

# lembrando que o uso desse arquivo sempre segue do topo para o bot, \ 
# por isso a necessidade de verificar as permissoes antes de rodar
