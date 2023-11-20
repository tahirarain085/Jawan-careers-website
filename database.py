from sqlalchemy import create_engine,text


connection_string = "mysql+pymysql://e78mu9mp4geh687dh8s5:pscale_pw_GAXHDAq5ALPyzh8kZFIbgcCSI3sAguMvakwUPvyoZkw@aws.connect.psdb.cloud:3306/jawancareers?charset=utf8mb4"
engine = create_engine(connection_string, connect_args = {
    "ssl":{
        "ssl_ca": "/etc/ssl/cert.pem"
    }
})
def load_jobs_from_db():
     with engine.connect() as conn:
        results = conn.execute(text("SELECT * FROM Jobs"))

        jobs = []
        for row in results.all():
            jobs.append(row)
        return jobs
     