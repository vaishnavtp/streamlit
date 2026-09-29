import mysql.connector


class BookListCreateRetrieveUpdateDelete:

    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="mysql@9746",
            database="library_db"
        )

        self.cursor = self.connection.cursor()

    # CREATE
    def create(self, title, author, price, pages, language):

        query = """
        INSERT INTO book (title, author, price, pages, language)
        VALUES (%s, %s, %s, %s, %s)
        """

        data = (title, author, price, pages, language)

        self.cursor.execute(query, data)
        self.connection.commit()

        print("Inserted Data Successfully")


    # RETRIEVE ONE RECORD
    def retrieve(self, id):

        query = "SELECT * FROM book WHERE id=%s"

        data = (id,)

        self.cursor.execute(query, data)

        record = self.cursor.fetchone()

        if record:
            return record
        else:
            print("No record found")


    # LIST ALL RECORDS
    def list(self):

        query = "SELECT * FROM book"

        self.cursor.execute(query)

        records = self.cursor.fetchall()

        return records


    # UPDATE
    def update(self, id, title, author, price, pages, language):

        query = """
        UPDATE book
        SET title=%s,
            author=%s,
            price=%s,
            pages=%s,
            language=%s
        WHERE id=%s
        """

        data = (title, author, price, pages, language, id)

        self.cursor.execute(query, data)
        self.connection.commit()

        print("Updated Data Successfully")


    # DELETE
    def delete(self, id):

        query = "DELETE FROM book WHERE id=%s"

        data = (id,)

        self.cursor.execute(query, data)
        self.connection.commit()

        print("Deleted Data Successfully")