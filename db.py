from sqlalchemy import create_engine,text
from collections import OrderedDict

db_connection_string ="mysql+mysqlconnector://root:ilovepakistan@localhost:3306/jawancareers"

engine = create_engine(db_connection_string)



def load_jobs_from_db():
    with engine.connect() as conn:
        results = conn.execute(text("select * from jobs"))
        jobs = [dict(zip(results.keys(),job)) for job in results]
       
        
    return jobs

    
            