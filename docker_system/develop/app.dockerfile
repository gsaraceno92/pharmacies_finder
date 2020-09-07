FROM python:3.8

ARG USER
ARG UID
# ARG UID
# Prevents Python from writing pyc files to disc 
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1


RUN apt-get update
RUN apt-get install -y vim libldap2-dev libsasl2-dev libssl-dev libapache2-mod-wsgi

ADD ./app /usr/src/app

# Install python modules
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt
RUN python --version

RUN groupadd -g $UID $USER
RUN useradd -u $UID -g $USER $USER -d /usr/src/app
RUN chown $USER:$USER /usr/src/app

WORKDIR /usr/src/app
USER $USER

ENTRYPOINT ["python3"]
CMD ["app.py"]

