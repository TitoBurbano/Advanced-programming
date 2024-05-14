from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class PostgresConnection:
    def __init__(self, user: str, password: str, host: str, port: int, database_name: str):
        self.engine = create_engine(
            f"postgresql://{user}:{password}@{host}:{port}/{database_name}"
        )
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()


if __name__ == "__main__":
    
    user = "new_user"
    password = "password"
    host = "localhost"
    port = 5432  
    database_name = "mydatabase"

    
    postgres_conn = PostgresConnection(user, password, host, port, database_name)

    
    session = postgres_conn.get_session()

