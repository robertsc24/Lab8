import sqlite3

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('blog.db')
        self.create_post_table()
        self.create_comment_table()

    def __del__(self):
        self.conn.commit()
        self.conn.close()

    def create_post_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "Post" (
          id INTEGER PRIMARY KEY,
          Title TEXT NOT NULL,
          Content TEXT NOT NULL,
          CreatedOn Date DEFAULT CURRENT_DATE
        );
        """
        self.conn.execute(query)

    def create_comment_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "Comment" (
          id INTEGER PRIMARY KEY,
          PostId INTEGER,
          Content TEXT NOT NULL,
          CreatedOn Date DEFAULT CURRENT_DATE,
          FOREIGN KEY(PostId) REFERENCES Post(id)
        );
        """
        self.conn.execute(query)


class PostModel:
    TABLENAME = "Post"

    def __init__(self):
        self.conn = sqlite3.connect('blog.db')
        self.conn.row_factory = sqlite3.Row

    def __del__(self):
        self.conn.commit()
        self.conn.close()

    def create_post(self, title, content):
        query = "INSERT INTO Post (Title, Content) VALUES (?, ?)"
        cur = self.conn.execute(query, (title, content))
        self.conn.commit()
        return cur.lastrowid

    def get_post(self, post_id):
        query = "SELECT * FROM Post WHERE id = ?"
        cur = self.conn.execute(query, (post_id,))
        post = cur.fetchone()
        return post

    def update_post(self, post_id, title, content):
        query = "UPDATE Post SET Title = ?, Content = ? WHERE id = ?"
        self.conn.execute(query, (title, content, post_id))
        self.conn.commit()

    def delete_post(self, post_id):
        query = "DELETE FROM Post WHERE id = ?"
        self.conn.execute(query, (post_id,))
        self.conn.commit()

    def list_posts(self):
        query = "SELECT * FROM Post"
        cur = self.conn.execute(query)
        posts = cur.fetchall()
        return posts



class CommentModel:
    TABLENAME = "Comment"

    def __init__(self):
        self.conn = sqlite3.connect('blog.db')
        self.conn.row_factory = sqlite3.Row

    def __del__(self):
        self.conn.commit()
        self.conn.close()

    def create_comment(self, post_id, content):
        query = "INSERT INTO Comment (PostId, Content) VALUES (?, ?)"
        cur = self.conn.execute(query, (post_id, content))
        self.conn.commit()
        return cur.lastrowid

    def get_comments_by_post(self, post_id):
        query = "SELECT * FROM Comment WHERE PostId = ?"
        cur = self.conn.execute(query, (post_id,))
        comments = cur.fetchall()
        return comments

    def update_comment(self, comment_id, content):
        query = "UPDATE Comment SET Content = ? WHERE id = ?"
        self.conn.execute(query, (content, comment_id))
        self.conn.commit()

    def delete_comment(self, comment_id):
        query = "DELETE FROM Comment WHERE id = ?"
        self.conn.execute(query, (comment_id,))
        self.conn.commit()
