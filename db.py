from sqlalchemy import create_engine,text

db_connection_string ="mysql+mysqlconnector://root:ilovepakistan@localhost:3306/jawancareers"

engine = create_engine(db_connection_string)


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text('SELECT * FROM jobs'))
        rows = result.fetchall()
        jobs = [dict(zip(result.keys(), row)) for row in rows]
        return jobs

        
            