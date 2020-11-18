import requests
import psycopg2

def ingest(nbLigne,  _dbname, _username, _pw, _host = 'localhost'):

    with requests.get("http://127.0.0.1:5000/large_request/" + str(nbLigne), stream = True) as r:
        # print(r.text)
        """ connection to the target db """
        conn = psycopg2.connect(
            host = _host,
            dbname = _dbname,
            user = _username, 
            password = _pw
        )
        cur = conn.cursor()
        sql = "INSERT INTO transactions (txid, uid, amount) VALUES (%s, %s, %s)"

        """ get db and insert to the db"""
        buffer = ""
        for chunk in r.iter_content(chunk_size = 1):
            if chunk.endswith(b'\n'):
                s = eval(buffer)
                print(s)
                cur.execute(sql, (s[0], s[1], s[2]))
                conn.commit()
                buffer = ""
            else:
                buffer += chunk.decode()


if __name__ == "__main__":
    ingest(1000000, "stream_trans", "postgres", "docker", "192.168.1.23")