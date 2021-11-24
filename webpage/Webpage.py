from logging import debug
from typing_extensions import Required
from flask import Flask,request,jsonify
from flask_restful import Api,Resource,reqparse
import pymysql.cursors
import json
import pickle
import time
import urllib3
http=urllib3.PoolManager()
localtime = time.asctime( time.localtime(time.time()) )
app=Flask(__name__)
api=Api(app)
mc=12664
class project(Resource):
    def put(self,value):
        
        return {'value':value}
    def get(self,value,kg):
        print("Success")
        if kg.startswith("val"):
            l=kg.split()
            print(l)
            db=pymysql.connect(
                host="0.tcp.ap.ngrok.io",
                user="root",
                passwd="",
                port=mc,
                database='FEX'
            )
            mycursor = db.cursor()
            sql='INSERT INTO new_table(cid,{}) VALUES (%s,%s)'.format(l[2])
            print(sql)
            mycursor.execute(sql,(l[1],value))
            db.commit()
            return {'value':value}
        elif kg=="id":
            db=pymysql.connect(
                host="0.tcp.ap.ngrok.io",
                user="root",
                passwd="",
                port=mc,
                database='FEX'
            )
            mycursor = db.cursor()
            sql="""SELECT idd,noc
            FROM signup;"""
            val=(value, 'y')
            mycursor.execute(sql)
            dev=mycursor.fetchall()
            print(dev[len(dev)-1])
            go=dev[len(dev)-1]
            g=go[1]
            print(g,type(g))
            g=g.split()
            print(g,type(g))
            pickle.dump(f"{go[0]}",open("sjm.pkl","wb"))
            mycursor = db.cursor()
            mycursor.execute("SHOW TABLES")
            for x in mycursor:
                print(x)
            
            for i in g:
                mycursor.execute(f"ALTER TABLE new_table ADD COLUMN {i} INT NOT NULL default 0")
            return "SUCCESSFUL"
                
        else:
            db=pymysql.connect(
                host="0.tcp.ap.ngrok.io",
                user="root",
                passwd="",
                port=mc,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor,
                database='FEX'
            )
            mycursor = db.cursor()
            TV=pickle.load(open("sjm.pkl","rb"))
            mycursor.execute(f"INSERT INTO {TV} {kg} VALUE({value}) ")                             
api.add_resource(project,"/<string:kg>/<string:value>")
if __name__=="__main__":
    app.run(debug=True)
    
