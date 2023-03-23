ARG python=python:3.9.13-slim-buster

# build stage
FROM ${python} as build
# setup
WORKDIR /
# python environment
COPY venv/requirements.txt requirements.txt
RUN python -m venv venv
ENV PATH=/venv/bin:$PATH
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# final stage
FROM ${python} as final
# setup
WORKDIR /
# python environment
COPY --from=build /venv /venv
ENV PATH=/venv/bin:$PATH
# copy src and mount test_data
COPY config/. config
COPY src/. src
VOLUME ["/test_data"]
EXPOSE 8001
# run
CMD ["python3", "src/app/main_run_api.py"]
