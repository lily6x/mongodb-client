
import json
from lily.mongodb.DataBaseSupport import MongodbUtil
from bson.objectid import ObjectId

class SqlResolver(object):
    SELECT = "select"
    FROM = "from"
    WHERE = "where"


    @staticmethod
    def resolv(sql):
        print("Sql resolv")
        commend = None

        si = sql.find("select")
        if si >= 0 :
            commend = SqlResolver.resolvSelect(sql)

        # print(MongoCommend.toJson(commend))
        return commend

    @staticmethod
    def executeCommend(commend):
        print("commend execute")
        result = MongodbUtil.getDocuments("imapi",commend.collection,**commend.find)
        print(result)
        return result


    @staticmethod
    def __resolvFind(wlist,result):
        if type(wlist).__name__ == "list":
            le = len(wlist)
            if le < 3:
                return result
            va = wlist[2]
            vai = va.find("'")
            if vai < 0:
                va = int(va)
            else :
                if "ObjectId" in va:
                    v2 = ObjectId(va[10:len(va)-2])
                    va = ObjectId(v2)
                else :
                    va = va[1:len(va) - 1]
            result[wlist[0]] = va
            nlist = wlist[4:]
            return SqlResolver.__resolvFind(nlist, result)




    @staticmethod
    def resolvSelect(sql):
        print(sql)
        commend = MongoCommend()
        commend.sql = sql
        commend.type = 2
        print(commend)
        find = {}
        # fi = sql.index("from")
        # print(fi)
        # print(sql[fi:fi+4])
        sqlList = sql.split()
        lfi = sqlList.index("from")
        print(sqlList)
        print(sqlList.index("from"))
        print(sqlList[lfi+1])

        if "where" in sqlList :
            lwi = sqlList.index("where")
            wlist = sqlList[lwi + 1:]
            print(wlist)
            r = {}
            wl = SqlResolver.__resolvFind(wlist, r)
            print(wl)
            commend.find = wl

        commend.collection = sqlList[lfi+1]
        return commend




class MongoCommend(object):

    def __init__(self):
        print("commend init")
        self.sql = ""
        self.type = 3
        self.find = {}
        self.set = {}
        self.collection = ""

    @staticmethod
    def __obj_2_json(obj):
        return {
            "sql": obj.sql,
            "type": obj.type,
            "find": obj.find,
            "set": obj.set,
            "collection": obj.collection
        }
    @staticmethod
    def toJson(obj):
        return json.dumps(obj,default=MongoCommend.__obj_2_json)