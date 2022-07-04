import mysql.connector
from JobCrawler.read_config import read_config_file

class DB():
    def __init__(self):
        db_config = read_config_file('../config.ini', 'mysql')
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

        if not self.create_jobadv_table():
            print('Check DB, please')

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
                try:
                    cursor.execute(sql)
                    self.conn.commit()
                except:
                    print('Can not connect with db')
                    return False
        except:
            print('Problem with connecting db')


    def drop_jobadv_table(self):
        sql = "DROP TABLE IF EXISTS jobadv;"

        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
                self.conn.commit()
        except:
            print('Problem with dropping table in db')

    def insert_job(self, job_data):
        sql = """
            INSERT IGNORE INTO jobadv
            (post_date, name,  skills)
            values(%s, %s, %s) 
        """

        try:
            with self.conn.cursor(prepared=True) as cursor:
                cursor.execute(sql, tuple(job_data.values()))
                self.conn.commit()
        except:
            print('Problem with insertin in db')

    def insert_jobs(self, jobs_data:list):
        sql="""
            INSERT IGNORE INTO jobadv
            (post_date, name,  skills)
            values(%s, %s, %s) 
        """
        for a_job in jobs_data:
            self.insert_job(a_job)

    def select_all_jobs(self):
        sql = "SELECT id, post_date, name, skills FROM jobadv"

        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchall()
        except:
            print('Problem with inserting info in table')

        return result

    def get_info_in_db(self):
        sql = 'SELECT MAX(post_date) AS "Posted Date" FROM jobadv;'

        try:
            with self.conn. cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchone()
        except:
            print('Problem with reading from db')

        if result:
            return result[0]
        else:
            raise ValueError('There is no data in table')


    def get_column_names(self):
        sql = "SELECT id, post_date, name, skills FROM jobadv LIMIT 1;"

        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchone()
        except:
            print('Problem with reading column names')

        return cursor.column_names


if __name__ == '__main__':
    db = DB()
    db.get_info_in_db()
    db.insert_job({
                   'post_date' : '2022-07-01',
                    'name': '2',
                   'skills': 'Python'
                   })
