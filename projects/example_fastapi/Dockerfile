FROM python:3.12

ARG PACKAGE_NAME
ARG PACKAGE_VERSION="0.0.1"
ARG WHEEL_PATH_SUFFIX="-py3-none-any.whl"
ARG WHEEL_PATH="$PACKAGE_NAME-$PACKAGE_VERSION$WHEEL_PATH_SUFFIX"
ARG DEPS=requirements.txt

RUN python -m pip install --upgrade pip

WORKDIR /app

COPY ./$DEPS .
RUN pip install -r $DEPS

COPY ./dist/$WHEEL_PATH .
# This is adjusted to install third-party dependencies separately (the --no-deps) and install from requirements
RUN pip install --no-cache-dir --upgrade --no-deps $WHEEL_PATH

CMD ["uvicorn", "genmono.hello_api.core:app", "--host", "0.0.0.0", "--port", "8000"]
