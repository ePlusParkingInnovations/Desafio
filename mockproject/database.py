import sqlite3

class DataBase(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.conn = sqlite3.connect('data.db')

	def UpdateData(self, data):
		c = self.conn.cursor()
		c.execute("UPDATE parking SET available = (?) WHERE place ='calle'",[(data), ])
		self.conn.commit()

	def CloseDB(self):
		self.conn.close()


	def GetParking(self):
		c = self.conn.cursor()
		c.execute("SELECT available  FROM parking")
		return (c.fetchall()[0][0])
