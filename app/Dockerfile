FROM python:3-onbuild

ARG USER=app
ARG UID=1001
ARG GID=1001

RUN useradd ${USER} \
   && usermod -u $UID ${USER} \
   && groupmod -g $GID ${USER} \
   && mkdir -p /app \
   && chown -R ${USER}:${USER} /app
USER ${USER}

WORKDIR /app

COPY --chown=$USER:$USER . .


EXPOSE 8000

CMD ["python", "./main.py"]