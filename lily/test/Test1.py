from lily.mongodb import DataBaseSupport
from pymongo import MongoClient
from lily.mongodb.SqlResolver import SqlResolver
import math

settings = {
    "ip": '47.107.234.237',  # ip
    "port": 28018,  # 端口
    "db_name": "mydb",  # 数据库名字
    "set_name": "test_set"  # 集合名字
}

def mains():
    print("mains")
    sql()

def sql():
    print("sql")
    sql = "select * from user nickname = 'Lily'"
    commend = SqlResolver.resolv(sql)
    SqlResolver.executeCommend(commend)
    # s = sql.find("select")
    # print(s)


def showdbs():
    conn = MongoClient(settings['ip'], settings['port'])
    db = conn["imapi"]
    coll = db["user"]
    # cou = coll.find().count()
    cou = coll.count_documents({})
    print(cou)
    # d = DataBaseSupport.MongodbUtil.getDocuments()
    # print(d)
    # print("hello world")


if __name__ == "__main__":
    mains()
