FROM fedora:32
RUN dnf install -y python-pip \
    && dnf clean all \
    && pip install fastapi uvicorn aiofiles SQLAlchemy psycopg2-binary
WORKDIR /srv
CMD ["uvicorn", "main:app", "--reload"]

# podman run --rm -v $PWD:/srv:z -p 8000:8000 --name fastapi -d fastapi

