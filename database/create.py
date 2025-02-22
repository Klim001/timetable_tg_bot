def create_session_db(Path):
    from sqlalchemy.engine import create_engine
    from sqlalchemy.orm import sessionmaker
    engine = create_engine(Path)
    Session_class = sessionmaker(bind=engine)
    return Session_class()