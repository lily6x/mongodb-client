#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pymongo import MongoClient
import math


settings = {
    "ip": '47.107.234.237',  # ip
    "port": 28018,  # 端口
    "db_name": "mydb",  # 数据库名字
    "set_name": "test_set"  # 集合名字
}


class MongodbUtil(object):
    @staticmethod
    def shwDatabases():
        conn = MongoClient(settings['ip'], settings['port'])
        database = {}
        ls = conn.list_database_names()
        for d in ls:
            db = conn[d]
            cs = db.list_collection_names()
            database[d] = cs
        return database

    # * 不定长 数组 参数形式
    # ** 不定长 Key value 形式参数
    @staticmethod
    def getDocuments(database,collection,currPage=1,pageSize=20,**vardict):
        conn = MongoClient(settings['ip'], settings['port'])
        db = conn[database]
        coll = db[collection]
        cou = coll.count_documents(vardict)
        page = MongodbUtil.getPage(pageSize,currPage,cou)
        dcs = coll.find(vardict).limit(page["limit"]).skip(page["skip"])
        result = {}
        data = []
        for r in dcs:
            # print(result["_id"])
            data.append(r)
        result["count"] = cou
        result["total"]=page["pageCount"]
        result["data"]=data
        return result

    @staticmethod
    def getPage(pageSize,currPage,count):
        page = {}
        page["pageSize"]=pageSize
        page["currPage"]=currPage
        page["count"]=count
        page["pageCount"]=math.ceil(count/pageSize)
        page["limit"] = pageSize
        page["skip"]=pageSize*(currPage-1)
        return page

