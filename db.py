import sqlite3
import datetime

def login(username, password):

	conn = sqlite3.connect('db.sqlite')
	cur = conn.cursor()
	cur.execute('CREATE TABLE IF NOT EXISTS users (username VARCHAR, password VARCHAR)')
	cur.execute("SELECT username, password FROM users WHERE username = ?", (username,))
	data = cur.fetchall()

	if len(data) == 0:
		print(f'There is no user {username}, please register.')
	else:
		if data[0][1] != password:
			return 'wp'
		else:
			print('Looks good')
			return True

	conn.commit()
	conn.close()


def register(username, password):

	conn = sqlite3.connect('db.sqlite')
	cur = conn.cursor()
	cur.execute('CREATE TABLE IF NOT EXISTS users (username VARCHAR, password VARCHAR)')
	cur.execute("SELECT 1 FROM users WHERE username = ?", (username,))
	data = cur.fetchall()

	if len(data) > 0:
		print('User exists already, please log in.')

	else:
		cur.execute('INSERT INTO users (username, password) values (?, ?)', (username, password))
		conn.commit()
		conn.close()
		return True


def post(username, content=''):
	conn = sqlite3.connect('db.sqlite')
	cur = conn.cursor()
	cur.execute('CREATE TABLE IF NOT EXISTS posts (username VARCHAR, dt TEXT, content TEXT)')
	cur.execute('INSERT INTO posts (username, dt, content) values (?, ?, ?)', (username, datetime.datetime.now(), content))
	conn.commit()
	conn.close()


def load_feed():
	conn = sqlite3.connect('db.sqlite')
	cur = conn.cursor()
	cur.execute('CREATE TABLE IF NOT EXISTS posts (username VARCHAR, dt TEXT, content TEXT)')
	cur.execute("SELECT username, dt, content FROM posts WHERE 1=1")
	data = cur.fetchall()
	conn.close()
	print(data)
	return data