import sqlite3 as sql
from flask import session
from passlib.hash import sha256_crypt
import requests
import datetime
def insertUser(request):
    con = sql.connect("database.db")
    sqlQuery = "select username from user_details where (username ='" + request.form['username'] + "')"
    cur = con.cursor()
    cur.execute(sqlQuery)
    row = cur.fetchone()
    print row #check
    
    if not row:
        cur.execute("INSERT INTO user_details (username,password,name,dob,email,gender,isadmin,facebook) VALUES (?,?,?,?,?,?,?,?)", (request.form['username'], 
                   sha256_crypt.encrypt(request.form['password']),request.form['name'],request.form['dob'],request.form['email'],request.form['gender'],request.form['isAdmin'],request.form['facebook']))
        con.commit()
        print "added user successfully"
       
    con.close()
    return not row


def authenticate(request):
    con = sql.connect("database.db")
    sqlQuery = "select password from user_details where username = '%s'"%request.form['username']  
    cursor = con.cursor()
    cursor.execute(sqlQuery)
    row = cursor.fetchone()
    con.close()
    if row:
       return sha256_crypt.verify(request.form['password'], row[0])
    else:
       return False


def retrieveUsers(): 
	con = sql.connect("database.db")
        # Uncomment line below if you want output in dictionary format
	#con.row_factory = sql.Row
	cur = con.cursor()
	cur.execute("SELECT * FROM users;")
	rows = cur.fetchall()
	con.close()
	return rows
  
def retrievetweets(user=None): 
  try:
    with sql.connect("database.db") as con:
      con.row_factory = sql.Row
      cur = con.cursor()
      if user!=None:
        cur.execute("select * from tweet_detail ORDER BY Tweet_id")
        rows = cur.fetchall()
        users=[]
        for row in rows:
          if row['user_name']==user:
            users.append(row)
        return users
  except:
    print "Connection Error"
    return([],"connection Fault")

def retrieveParticular(Tweet_id): 
  try:
    with sql.connect("database.db") as con:
      con.row_factory = sql.Row
      cur = con.cursor()
      if Tweet_id!=None:
        cur.execute("select content, title from tweet_detail WHERE Tweet_id={x}".format(x=Tweet_id))

        rows = cur.fetchone()
        return (rows["content"], rows["title"])
  except:
    print "Connection Error"
    return([],"connection Fault")


def getAll():
  msg = "Records were fetched successfully"
  try:  
    with sql.connect("database.db") as con:
      con.row_factory = sql.Row
      cur = con.cursor()
      cur.execute("select * from tweet_detail WHERE published = 1 ORDER BY date DESC") 
      rows = cur.fetchall()
      user=[]
      for row in rows:
           user.append(row)
      return (user)
  except:
      print "connection failed"
      return ([], "connection failed")




def del_tweets(arg):
  try:
    with sql.connect("database.db") as con:
      cur=con.cursor()
      print "value of arg = " , arg
      queryString = "Delete from tweet_detail where Tweet_id='%s'"%arg
      cur.execute(queryString)
      return "success"
  except:
    return "Failure"


