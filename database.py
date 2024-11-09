from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from sqlalchemy import text
DATABASE_URL = "sqlite:///library.db"

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)
session = Session()

if __name__ == "__main__":
    with engine.connect() as conn:
        try:
            query = "select * from books"
            result = conn.execute(text(query))
            print(result.all())
        except Exception as e:
            print(f"An error occurred: {e}")