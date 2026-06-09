import pymysql

class BoardDAO:

    def __init__(self):
        self.host = "localhost"
        self.user = "board_user"
        self.password = "board1234"
        self.database = "board_db"

    def get_connection(self):
        return pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            charset="utf8mb4"
        )
    
    def select_all(self):
        conn = self.get_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        sql = """
        SELECT *
        FROM board
        ORDER BY id DESC
        """

        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        conn.close()

        return result
    
    def insert_board(self, title, content, writer, password):
        conn = self.get_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO board (title, content, writer, password) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (title, content, writer, password))
        conn.commit()
        cursor.close()
        conn.close()

    def select_one(self, board_id):
        conn = self.get_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        update_sql = "UPDATE board SET views = views + 1 WHERE id = %s"
        cursor.execute(update_sql, (board_id,))
        conn.commit()

        sql = "SELECT * FROM board WHERE id = %s"
        cursor.execute(sql, (board_id,))
        result = cursor.fetchone() 
        cursor.close()
        conn.close()
        return result    
    
    def delete_board(self, board_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        sql = "DELETE FROM board WHERE id = %s"
        cursor.execute(sql, (board_id,))
        conn.commit()  
        cursor.close()
        conn.close()
