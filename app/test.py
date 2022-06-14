import json
import uuid
import pytest
import sqlalchemy as sa
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .address.database import Base
from . import main
from address.v1 import get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


@sa.event.listens_for(engine, "connect")
def do_connect(dbapi_connection, connection_record):
    dbapi_connection.isolation_level = None


@pytest.fixture()
def session():
    connection = engine.connect()
    session = TestingSessionLocal(bind=connection)

    yield session
    session.close()
    connection.close()


@pytest.fixture()
def client(session):
    def override_get_db():
        yield session

    main.app.dependency_overrides[get_db] = override_get_db
    yield TestClient(main.app)
    del main.app.dependency_overrides[get_db]

def add_addres(client):
    payload = {
        "line1": str(uuid.uuid4()),
        "latitude": str(uuid.uuid4()),
        "longitude": str(uuid.uuid4())
    }

    response = client.post(
        "/addres/add",
        json=payload,
    )
    response = json.loads(response.text)
    assert response.get("data") != None
