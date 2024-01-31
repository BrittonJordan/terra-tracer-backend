import sqlalchemy as sa
from sqlalchemy.dialects.mysql import insert

def build_engine(username: str, password: str, host: str, port: int, database: str):
    return sa.create_engine(f"postgresql://{username}:{password}@{host}:{port}/{database}")

def load_location_visits_from_file(engine, file_path):
    # load json file from file_path

    print("test")
