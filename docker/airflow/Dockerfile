# Base Image
FROM python:3.8-slim
LABEL maintainer="YuichiOtsuka"

# Arguments
ARG PYTHON_VERSION=3.8
ARG AIRFLOW_VERSION=2.4.0
ARG AIRFLOW_HOME=/opt/airflow

# Export
ENV AIRFLOW_HOME=${AIRFLOW_HOME}

# Install dependencies and tools
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    freetds-bin \
    krb5-user \
    ldap-utils \
    libffi-dev \
    libsasl2-dev \
    libsasl2-modules \
    libssl-dev \
    locales \
    lsb-release \
    sasl2-bin \
    sqlite3 \
    unixodbc \
    libczmq-dev \
    inetutils-telnet \
    bind9utils \
    freetds-dev \
    libkrb5-dev \
    libpq-dev \
    build-essential \
    default-libmysqlclient-dev \
    wget \
    curl \
    git \
    zip \
    unzip \
    gcc \
    apt-utils \
    rsync \
    procps \
    sed \
    netcat-openbsd \
    && apt-get clean

# Upgrade pip
# Create airflow user 
# Install apache airflow with subpackages
RUN pip install --upgrade "pip==20.2.4" && \
    useradd -ms /bin/bash -d ${AIRFLOW_HOME} airflow && \
    pip install apache-airflow==${AIRFLOW_VERSION} --constraint https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt

# Copy the airflow.cfg file (config)
#COPY ./config/airflow.cfg ${AIRFLOW_HOME}/airflow.cfg

# Set the owner of the files in AIRFLOW_HOME to the user airflow
RUN chown -R airflow: ${AIRFLOW_HOME}

# Copy the start-airflow.sh from host to container (at path AIRFLOW_HOME)
COPY ./start-airflow.sh ./start-airflow.sh

# Set the entrypoint.sh file to be executable
RUN chmod +x ./start-airflow.sh

# Set the username to use
USER airflow

# Create the folder dags inside $AIRFLOW_HOME
RUN mkdir -p ${AIRFLOW_HOME}/dags

# Expose ports (just to indicate that this container needs to map port)
EXPOSE 8080

# Execute start-airflow.sh
CMD [ "./start-airflow.sh" ]
