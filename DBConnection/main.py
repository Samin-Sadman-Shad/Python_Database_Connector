# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

from MySQLConnection import MySQLDb
from MongoDBConnection import MongDBClient
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # mysql = MySQLDb(host='localhost',port='3306',user='root ', password='password')
    # mysql.create_database('SCHOOL')
    # mysql.create_table(table='STUDENT', dbname='SCHOOL', id='INT AUTO_INCREMENT PRIMARY KEY', name='VARCHAR(50)',age='INT',studentID='INT')
    # # mysql.insert_data(table='STUDENT', column_data={'name':'shad', 'age':'19', 'studentId':'5'})
    # # mysql.get_data(table='STUDENT', column_list=['name', 'age'])
    # mysql.update_data(table='STUDENT', column_data={'name':'sam'}, condition="studentID=1")

    mongodb = MongDBClient(url='localhost', dbname='BookStore2')
    # mongodb.create_collection('Books')
    # mongodb.insert_multiple_document(dbname='BookStore2', collection='Books',
    #                                  document_list=[{ "Name": "Design Patterns", "Price": 54.93, "Category": "Computers", "Author": "Ralph Johnson" },
    #                                                 { "Name": "Clean Code", "Price": 43.15, "Category": "Computers","Author": "Robert C. Martin" },
    #                                                 { "Name": "Clean Code 2", "Price": 43.15, "Category": "Computers","Author": "Robert C. Martin" }])
    # mongodb.find_data(dbname='BookStore2', collection='Books',filter={'name':'Clean Code', "Price": 43.15, "Category": "Computers","Author": "Robert C. Martin"})
    # mongodb.find_data(dbname='BookStore2', collection='Books', filter={})
    mongodb.find_data(dbname='BookStore2', collection='Books', filter={'Name':'Clean Code'})
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
