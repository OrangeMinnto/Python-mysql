import lib.core.base as db
import lib.core.function as function
import lib.parse.SqlToCode as SqlToCode
import json

if __name__ == '__main__':

	while True:
		sql = input("sql > ")
		print("")
		SqlToCode.parseSql(sql)
		print("")
	#db.create_db("test") #数据库创建
	#db.select_db("test1")
	#db.create_table("bbb",{"id":"int","name":"string"}) #创建表
	#db.select_db("test1")
	#db.insert_into_table("bbb",[{"id":6,"name":"bb"},{"id":7,"name":"bb"}])
	#db.insert_into_table("bbb",{"id":2,"name":"aa"})
	#db.insert_into_table("bbb",{"id":1,"name":"ccc"})
	#db.delete_from_table("bbb",{"id":["=",1]})
	#db.update_from_table("bbb",{"name":"test11"},{"id":["<=",2]})
	#db.select_from_table("bbb",["*"],{"id":[">=",1]})
	#db.update_from_table("bbb",)
	#function.console_print(["id","name"],[{"id":3,"name":"bb"},{"id":3,"name":"bb"},{"id":3,"name":"bb"}])
	#db.desc_from_table("bbb")
	#db.show_databases()
	#db.show_tables()
	'''
	or and 查询
	table_info = function.get_table_info("data/diego/users.json")
	data = function.get_all_data_from_table("data/diego/users.json")
	function.data_where(json.loads(table_info),data,[{"and": {"id":["=",1]}},{"or":{"id":[">",4]}},{"or":{"id":["<=",2]}}])
	'''
	