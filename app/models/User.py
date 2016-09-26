
from system.core.model import Model
import re

class User(Model):
	def __init__(self):
		super(User, self).__init__()

	def all_users(self):
		return self.db.query_db("SELECT * FROM users")

	def get_user_by_id(self, user_id):
		query = "SELECT * FROM users WHERE id = :user_id"
		data = { 'id': user_id }
		user_id = self.db.query_db(query, data)

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


	def friends_process (self, info):
		password = info['password']
		email = info['email']
		query = "SELECT * FROM users WHERE email = :email LIMIT 1"
		data = {'email': info['email'] }
		user = self.db.get_one(query, data)

		if user:
			if self.bcrypt.check_password_hash(user.password, password):
				return user
		return False

	# def add_friends(self, user):
	# 	# Build the query first and then the data that goes in the query
	# 	query = "INSERT INTO user (alias) VALUES (:alias)"
	# 	data = { 'alias': user['alias']
	# 	}
	# 	return self.db.query_db(query, data)

	def delete_user(self, user_id):   
		query = "DELETE FROM users WHERE id = :user_id LIMIT 1"
		data = {'user_id' : user_id}
		self.db.query_db(query, data)


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