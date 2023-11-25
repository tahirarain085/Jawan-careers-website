from sqlalchemy import create_engine,text

db_connection_string ="mysql+mysqlconnector://root:ilovepakistan@localhost:3306/jawancareers"

engine = create_engine(db_connection_string)


def load_jobs_from_db():
    with engine.connect() as conn:
        results = conn.execute(text('SELECT * FROM jobs'))
        


        rows = results.fetchall()
        jobs = [dict(zip(results.keys(), row)) for row in rows]
        return jobs

        
            