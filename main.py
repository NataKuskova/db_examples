import MySQLdb
import MySQLdb.cursors


def get_connection():
    connection = MySQLdb.connect(user='root',
                                 passwd='123',
                                 db='base_example',
                                 cursorclass=MySQLdb.cursors.DictCursor)
    return connection


def insert_books(values):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO Books (title, ISBN) VALUES (%s, %s)", values)


def select(**kwargs):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "SELECT * FROM Books"
    sql_where = ''
    if kwargs:
        sql += " Where "
        for name in kwargs.items():
            if not sql_where:
                sql_where = name[0] + "=" + str(name[1])
            else:
                sql_where += " and " + name[0] + "=" + str(name[1])
        sql += sql_where
    cursor.execute(sql)
    return cursor.fetchall()


# insert_books([
#     ('Book1', 'qwe-123'),
#     ('Book2', 'qwe-1212'),
# ])


print(select(title=1, ISBN=2))
