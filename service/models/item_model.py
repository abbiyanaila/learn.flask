from service.common import connector

class ItemModel:
    def __init__(self, name, self):
        self.name = name
        self.price = price

    def json(self):
        return {'name': self.name 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        connection = connector.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE name=?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': {'name': row[0], 'price': row[1]}}

    @classmethod
    def insert(cls, item):
        connection = connector.get_connection()
        cursor = connection.cursor()

        query = "INSERT INTO {table} VALUES(?, ?)".format(table=cls.TABLE_NAME)
        cursor.execute(query, (item['name'], item['price']))

    @classmethod
    def update(cls, item):
        connection = connector.get_connection()
        cursor = connection.cursor()

        query = "UPDATE {table} SET price=? WHERE name=?".format(table=cls.TABLE_NAME)
        cursor.execute(query, (item['price'], item['name']))