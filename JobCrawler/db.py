import mysql.connector
from JobCrawler.read_config import read_config_file

class DB():
    def __init__(self):
        db_config = read_config_file('../config.ini', 'mysql')
        print(db_config)
        try:
           self.conn = mysql.connector.connect(
                                    user=db_config['user'],
                                    password=db_config['password'],
                                    db=db_config['database'],
                                    host=db_config['host'],
                                    port=db_config['port']
           )
        except mysql.connector.Error as err:
            print(err)

        self.create_jobadv_table()

    def create_jobadv_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS jobadv(
                id INT AUTO_INCREMENT PRIMARY KEY,
                post_date DATE NOT NULL,
                name VARCHAR(100) NOT NULL,
                skills TEXT,
            
                CONSTRAINT name_date UNIQUE (name, post_date)                    
            );
        """
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
                self.conn.commit()
        except:
            print('Problem with connecting db')


    def drop_jobadv_table(self):
        sql = "DROP TABLE IF EXISTS jobadv;"

        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            self.conn.commit()

    def insert_job(self, job_data):
        sql = """
            INSERT IGNORE INTO jobadv
            (post_date, name,  skills)
            values(%s, %s, %s) 
        """

        with self.conn.cursor(prepared=True) as cursor:
            cursor.execute(sql, tuple(job_data.values()))
            self.conn.commit()

    def insert_jobs(self, jobs_data:list):
        sql="""
            INSERT IGNORE INTO jobadv
            (post_date, name,  skills)
            values(%s, %s, %s) 
        """
        for a_job in jobs_data:
            self.insert_job(a_job)

        # with self.conn.cursor() as cursor:
        #     cursor.executemany(sql, jobs_data[0])
        #     self.conn.commit()

    def select_all_jobs(self):
        sql = "SELECT id, post_date, name, skills FROM jobadv"

        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()

        return result

    def get_info_in_db(self):
        sql = 'SELECT MAX(post_date) AS "Posted Date" FROM jobadv;'
        with self.conn. cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchone()

        if result:
            return result[0]
        else:
            raise ValueError('There is no data in table')


    def get_column_names(self):
        sql = "SELECT id, post_date, name, skills FROM jobadv LIMIT 1;"

        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchone()

        return cursor.column_names


if __name__ == '__main__':
    db = DB()
    db.get_info_in_db()
    db.insert_job({'name':'2',
                   'post_date' : 4500,
                   'skills': 'Python'
                   })
