import pymongo


class MongDBClient:
    """
    Create a Mongoclient with given url and port. Give the database name. Default is 'mydatabase'.
    MongoDB does not create a database until it gets the content. It waits for creating a collection with least a single document
    """

    def __init__(self, url, port=None, dbname='mydatabase'):
        if port is not None:
            self.mongoClient = pymongo.MongoClient(f"mongodb://{url}:{port}")
        else:
            default_port = 27017
            self.mongoClient = pymongo.MongoClient(f"mongodb://{url}:{default_port}")
        self.database = self.mongoClient[dbname]
        print("Databases are ",self.mongoClient.list_database_names())

    def is_database_exists(self, dbname):
        dbnames = self.mongoClient.list_database_names()
        return dbname in dbnames

    def create_collection(self, collection_name):
        """
        Create a collection if it does not exists.
        MongoDB waits until a document is inserted before creating the actual collection
        """
        if self.database is not None:
            self.collection = self.database[collection_name]
        print(self.database.list_collection_names())

    def is_collection_exists(self, collection_name):
        if self.database is not None:
            collections = self.database.list_collection_names()
            return collection_name in collections
        return False

    def insert_single_document(self, dbname, collection, document:dict):
        self.database = self.mongoClient[dbname]
        self.collection = self.database[collection]
        insert_one = self.collection.insert_one(document)
        print(insert_one.inserted_id)

    def insert_multiple_document(self, dbname, collection, document_list:list):
        self.database = self.mongoClient[dbname]
        self.collection = self.database[collection]
        insert_many = self.collection.insert_many(document_list)
        for id in insert_many.inserted_ids:
            print(id, end=' ')
        print("document inserted")

    def find_data(self, dbname, collection,filter:dict= {}, projection:list=None):
        """
        Select document in a collection and return a cursor, pointing to that document

        :param dbname: name of the database where the collection is present
        :param collection: name of the collection where to find the document
        :param filter: document to include in thre result set
        :param projection: fields to be returned to the matching docuemnt
        :return:
        """
        self.database = self.mongoClient[dbname]
        self.collection = self.database[collection]
        if projection is not None:
            projection_dict = {}
            for key in projection:
                projection_dict[key] = 1
            for doc in self.collection.find(filter, projection_dict):
                print(doc)
        else:
            print(self.collection.count_documents(filter))
            for doc in self.collection.find(filter):
                print(doc)


    def sort_query(self, dbname, collection, field, direction:int):
        self.database = self.mongoClient[dbname]
        self.collection = self.database[collection]
        valid = {1, -1}
        if direction not in valid:
            raise ValueError("direction must be 1 or -1")
        document = self.collection.find().sort(field, direction)

    def delete_document(self, dbname, collection,query:dict):
        self.database = self.mongoClient[dbname]
        self.collection = self.database[collection]
        delete_result = self.collection.delete_many(query)
        print(delete_result.deleted_count, " documents deleted")

    def drop_collection(self, dbname, collection):
        self.database = self.mongoClient[dbname]
        self.collection = self.database[collection]
        self.collection.drop()

    def update_document(self, dbname, collection,query:dict, update:dict):
        self.database = self.mongoClient[dbname]
        self.collection = self.database[collection]
        update_result = self.collection.update_many(query, update)
        print(update_result.modified_count, "documents updated")