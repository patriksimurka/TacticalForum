import sqlite3
import datetime
import json

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
	cur.execute('CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY, username VARCHAR, dt TEXT, content TEXT, likes integer, liking TEXT)')
	cur.execute('INSERT INTO posts (username, dt, content, likes, liking) values (?, ?, ?, ?, ?)', (username, datetime.datetime.now(), content, 0, '{"usernames": []}'))
	conn.commit()
	conn.close()


def load_feed():
	conn = sqlite3.connect('db.sqlite')
	cur = conn.cursor()
	cur.execute('CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY, username VARCHAR, dt TEXT, content TEXT, likes integer, liking TEXT)')
	cur.execute("SELECT id, username, dt, content, likes, liking FROM posts WHERE 1=1")
	data = cur.fetchall()
	data = data[0]
	data = list(data)
	print(data)
	data[-1] = json.loads(data[-1])
	data = tuple(data)
	data = [data]
	conn.close()
	return data

def add_like(idcko, username):
	conn = sqlite3.connect('db.sqlite')
	cur = conn.cursor()
	cur.execute("SELECT liking FROM posts WHERE id=?", (idcko))
	arr = cur.fetchall()[0][0]
	liking = json.loads(arr)
		
	if username not in liking['usernames']:
		cur.execute('UPDATE posts SET likes = likes + 1 WHERE id = ?', (idcko))
		liking['usernames'].append(username)
		cur.execute('UPDATE posts SET liking = ? WHERE id = ?', (json.dumps(liking), idcko))
		unlike = 'false'
	else:
		cur.execute('UPDATE posts SET likes = likes - 1 WHERE id = ?', (idcko))
		liking['usernames'].remove(username)
		cur.execute('UPDATE posts SET liking = ? WHERE id = ?', (json.dumps(liking), idcko))
		unlike = 'true'

	cur.execute("SELECT likes FROM posts WHERE id=?", (idcko))
	conn.commit()
	data = cur.fetchall()
	conn.close()
	return str(data[0][0]) +' '+ unlike
