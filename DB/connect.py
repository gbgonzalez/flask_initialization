from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def database_connect(target: str = "flask_initalization"):

    engine = create_engine(
        f"mysql+pymysql://flaskUser:flaskPass@localhost:3306/{target}?charset=utf8mb4"
    )
    Session = sessionmaker(bind=engine, autoflush=False)

    return Session()

def database_engine(target: str = "flask_initalization"):

    engine = create_engine(
        f"mysql+pymysql://flaskUser:flaskPass@localhost:3306/{target}?charset=utf8mb4"
    )

    return engine