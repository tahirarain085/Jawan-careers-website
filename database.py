from sqlalchemy import create_engine,text


connection_string = "mysql+pymysql://root:ilovepakistan@localhost:3306/jawancareers"
engine = create_engine(connection_string, connect_args = {
    "ssl":{
        "ssl_ca": "/etc/ssl/cert.pem"
    }
}
)
def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text('SELECT * FROM jobs'))
        rows = result.fetchall()
        jobs = [dict(zip(result.keys(), row)) for row in rows]
        return jobs


# def load_jobs_from_db():
#     with engine.connect() as conn:
#         results = conn.execute(text("SELECT * FROM jobs"))

#         jobs = {}
#         for row in results.all():
#             jobs.update(row)
            
#         return jobs
     