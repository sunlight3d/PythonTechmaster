from pprint import pprint
from pymongo import MongoClient
from pymongo import ReturnDocument
from bson.objectid import ObjectId

class MongoDB:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['mongoDatabaseDemo']
        self.collection_student = self.db['students']

    def insert_one_student(self):
        self.collection_student.insert_one({
            "name": "Nguyen Van A",
            "age": 20,
            "email": "nguyenvana@gmail.com"
        })

    def insert_many_students(self):
        new_students = self.collection_student.insert_many(
            [
                {
                    "name": "Alex",
                    "age": 20,
                    "email": "alex@gmail.com"
                },
                {
                    "name": "Gracia",
                    "age": 22,
                    "email": "gracia@gmail.com"
                }
            ]
        )

    def find_all_students(self):
        all_students = self.collection_student.find({})
        print("Number of records = " + str(all_students.count()))
        for each_student in all_students:
            pprint(each_student)

    def delete_a_student(self):
        self.collection_student.delete_one({"name": "Alex"})

    def drop_a_collection(self):
        self.collection_student.drop()

if __name__ == "__main__":
    mongoDB = MongoDB()
    #mongoDB.insert_one_student()
    # mongoDB.insert_many_students()
    # mongoDB.find_all_students()
    # mongoDB.delete_a_student()
    mongoDB.drop_a_collection()
