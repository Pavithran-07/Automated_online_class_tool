import sqlite3
import datetime
import getpass 
import sys


class CRUD:
	def connection(self):
		try:
			conn = sqlite3.connect('test.db')
		except:
			print("Some error occurred...")
		return conn

	def userInsert(self,mail,password):
		self.conn = self.connection()
		sql = "INSERT INTO user values('{}','{}')".format(mail,password)
		self.conn.execute(sql)
		self.conn.commit()
		self.conn.close()

	def getuserCredentials(self):
		self.conn = self.connection()
		sql = "SELECT * from user"
		self.cursor = self.conn.execute(sql)
		for row in self.cursor:
			return row[0],row[1]


	def insert(self,fromtime,totime,link):
		conn = self.connection()
		sql = "INSERT INTO onlineclass values('{}','{}','{}')".format(fromtime[0],totime[0],link)
		conn.execute(sql)
		conn.commit()
		conn.close()

	def retdb(self):
		self.conn = self.connection()
		self.cursor = self.conn.execute("SELECT * FROM onlineclass")
		# self.conn.close()
		return self.cursor	

	def viewdb(self):
		self.conn = self.connection()
		self.cursor = self.conn.execute("SELECT * FROM onlineclass")
		for row in self.cursor:
			for i in range(len(row)):
				print(row[i])



class totalInput:

	def getInput(self):
		self.fromht = list(input("Enter the from time in HH:MM AM/PM eg: 09:48 AM: ").split(" "))
		self.toht =   list(input("Enter the to time in HH:MM AM/PM eg: 09:48 AM: ").split(" "))
		self.link = input("Enter the Class link: ")
		self.formatInput(self.fromht,self.toht,self.link)

	def amFormat(self,lst):
		temp = lst[0].split(":")
		temp[0] = str(int(temp[0]))
		lst[0] = temp[0]+ ":" + temp[1]
		return lst

	def pmFormat(self,lst):
		temp = lst[0].split(':')
		temp[0] = str(int(temp[0]) + 12)
		lst[0] = temp[0]+ ":" + temp[1]
		return lst

	def completeFormat(self,lst):
		temp = lst[0].split(":")
		temp[0] = str(int(temp[0]))
		lst[0] = str(temp[0])+ ":" + temp[1]
		return lst

	def formatInput(self,fromht,toht,link):
		if('AM' in fromht):
			fromht = self.amFormat(fromht)
		if('AM' in toht):
			toht = self.amFormat(toht)
		if('PM' in fromht):
				fromht = self.pmFormat(fromht)
		if('PM' in toht):
			toht = self.pmFormat(toht)

		fromht = self.completeFormat(fromht)
		toht = self.completeFormat(toht)

		crud = CRUD()
		crud.insert(fromht,toht,link)

		
