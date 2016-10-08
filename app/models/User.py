
from system.core.model import Model
import re

class User(Model):
	def __init__(self):
		super(User, self).__init__()

	# def all_users(self):
	# 	return self.db.query_db("SELECT * FROM users")

	# def get_user_by_id(self, user_id):
	# 	query = "SELECT * FROM users WHERE id = :user_id"
	# 	data = { 'id': user_id }
	# 	user_id = self.db.query_db(query, data)

	def register_user(self, info):

		EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
		errors = []

		if not info['name'] or not info['alias']:
			errors.append('Name cannot be blank')
		elif len(info['password'])<8:
			errors.append('Password must contain 8 characters!')
		elif not EMAIL_REGEX.match(info['email']):
			errors.append("Invalid Email Address!")
		elif not info['c_password'] == info['password']:
			errors.append("Password does not match!")

		query = "SELECT * FROM users WHERE email = :email"  
		data = { 'email': info['email']} 
		email = self.db.query_db(query, data)
		if email:
			errors.append('This email already exists')

		if errors:
			print errors
			return {'status': False, 'errors': errors}
		else:
			password = info['password']
			hashed_pw = self.bcrypt.generate_password_hash(password)
			query = "INSERT INTO users (name, alias, email, password, created_at, updated_at) VALUES (:name, :alias, :email, :password, NOW(), NOW())"
			data = {
			'name': info['name'], 
			'alias': info['alias'],
			'email': info['email'],
			'password': hashed_pw
			}
			user_id = self.db.query_db(query, data)
			print user_id
			return {'status': True, 'user_id': user_id}

# login
	def login_process (self, info):
		password = info['password']
		email = info['email']
		query = "SELECT users.id, users.name, users.email, users.password FROM users WHERE email = :email LIMIT 1"
		data = {'email': info['email'] }
		user = self.db.get_one(query, data)

		if user:
			if self.bcrypt.check_password_hash(user.password, password):
				return user
		return False

	def friends_table (self,user_id):
		query = """SELECT lists.id, lists.item, lists.user_id, users.name, lists.add_id, users2.name, lists.created_at FROM lists
		LEFT JOIN users ON lists.user_id = users.id
		LEFT JOIN users AS users2 ON lists.add_id = users2.id
		WHERE users.id = :user_id"""
		data = {
		'user_id': user_id
		}
		return self.db.query_db(query, data)

	def nofriends_table (self,user_id):
		query = """SELECT lists.id, lists.item, lists.user_id, users.name, lists.add_id, users2.name, lists.created_at FROM lists
		LEFT JOIN users ON lists.user_id = users.id
		LEFT JOIN users AS users2 ON lists.add_id = users2.id
		WHERE users.id != :user_id
				"""
		data = {'user_id': user_id}
		return self.db.query_db(query, data)

	def add_friends(self, user_id, add_id):
		# Build the query first and then the data that goes in the query
		data = { 'add_id' : add_id,
		'user_id': user_id

		}
		query = """INSERT INTO lists (item, user_id, add_id) VALUES (:item, :user_id, :add_id);"""
		self.db.query_db(query, data)
		# query = """INSERT INTO lists (user_id, add_id) VALUES (:add_id, :user_id);"""
		# self.db.query_db(query, data)


	def remove_friend(self, user_id, add_id): 
		data = { 'add_id' : add_id,
		'user_id': user_id
		} 
		query = """DELETE FROM items WHERE add_id =:add_id AND user_id = :user_id LIMIT 1;"""
		self.db.query_db(query, data) 
		query = """DELETE FROM items WHERE add_id = :add_id and user_id = :add_id LIMIT 1;"""
		self.db.query_db(query, data)
		# query = "DELETE FROM users WHERE id = :user_id LIMIT 1"
		# data = {'user_id' : user_id}

	def view_friend (self, user_id):
		query = """SELECT lists.item, lists.user_id, users.name from lists 
				LEFT JOIN  users on lists.user_id = users.id
				WHERE lists.user_id = lists.user_id"""
		data = { 
			'lists.user_id' : user_id
			}
		return self.db.query_db(query, data)

	def create_list (self, item):
		query = """INSERT into lists (item, created_at) VALUES (:item, NOW());"""
		data = {
		'item' : item
		}
		return self.db.query_db(query, data)
		

"""
	def get_users(self):
		query = "SELECT * from users"
		return self.db.query_db(query)

	def get_user(self):
		query = "SELECT * from users where id = :id"
		data = {'id': 1}
		return self.db.get_one(query, data)

	def add_message(self):
		sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
		data = {'message': 'awesome bro', 'users_id': 1}
		self.db.query_db(sql, data)
		return True
	
	def grab_messages(self):
		query = "SELECT * from messages where users_id = :user_id"
		data = {'user_id':1}
		return self.db.query_db(query, data)

	"""