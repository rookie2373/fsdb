import tree_ddl as schema
import tree_dml as db

db_name = 'local/family_tree.db'

schema.create_db(db_name)
db.create_dummies(db_name)
db.verify_dummies(db_name)

conn, cursor = schema.connect_db(db_name)

db.add_person(conn=conn, cursor=cursor, first_name="your_name", last_name="family_name", gender="M", birth_date="01/01/1980", death_date='',place_of_birth="Oslo")

db.add_relation_type(conn=conn, cursor=cursor, type_name="nullvoid")

db.add_relationship(conn=conn, cursor=cursor, from_id=1, to_id=1000, type_id=1000)