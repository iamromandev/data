# base image
ARG PYTHON_VERSION=3.11.0

FROM python:${PYTHON_VERSION} as base

ENV PYTHONFAULTHANDLER=on
ENV PYTHONUNBUFFERED=on
ENV PYTHONHASHSEED=random

# install required packages
#RUN apt-get update
#RUN apt-get install -y curl
#RUN apt-get update  \
#    && apt-get install --no-install-recommends -y  \
#    curl  \
#    build-essential

# builder image
FROM base as builder

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PIP_NO_CACHE_DIR=1
ENV PIP_DEFAULT_TIMEOUT=100
ENV POETRY_HOME="/opt/poetry"
ENV POETRY_VERSION=1.3.1
ENV POETRY_NO_INTERACTION=1
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV PYSETUP_PATH="/opt/pysetup"
ENV VENV_PATH="/opt/pysetup/.venv"
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"
#RUN pip install "poetry==$POETRY_VERSION"
RUN curl -sSL https://install.python-poetry.org | python3 -
#ENV PATH="/root/.poetry/bin:$PATH"
#RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
#RUN poetry config virtualenvs.create false
#RUN poetry install

WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./
RUN poetry install --no-dev
