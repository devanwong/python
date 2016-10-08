from system.core.controller import *

class Users(Controller):
	def __init__(self, action):
		super(Users, self).__init__(action)
		self.load_model('User')
		self.db = self._app.db

	def index(self):
		if session.get('id'):
			return self.load_view('success.html')
		else:
			users = self.models['User'].all_users()
			return self.load_view('index.html', users=users)

	# def show(self, id):
	# 	user = self.models['User'].get_user_by_id(id)
	# 	return self.load_view('show.html', user=user)


	def register(self): 
		status = self.models['User'].register_user(request.form)
		if status['status']:
			session['name'] = request.form['name']
			session['id'] = status['user_id']
			flash('You have successfully registered!')
			return redirect('/friends')
		else:
			for message in status['errors']:
				flash(message, 'regis_errors')
			return redirect('/')

	def logout(self):
		session.clear() 
		flash('You are now logged out')
		return redirect('/')

#login
	def login(self):
		status = self.models['User'].login_process(request.form)
		if status:	
			session['id'] = status['id']
			session['name'] = status['name']
			return redirect('/friends')
		else:
			flash('Invalid Password')		
			return redirect('/')

	def success(self):
		friends = self.models['User'].friends_table(session['id'])
		non_friends = self.models['User'].nofriends_table(session['id'])
		return self.load_view('success.html', friends=friends, non_friends=non_friends)

	# def update(self, user_id):
	# 	return self.load_view('delete.html')
	def add (self, user_id):
		addfriend = self.models['User'].add_friends(session['id'],user_id)
		return redirect ('/friends')

	def remove(self, user_id):
		removefriend = self.models['User'].remove_friend(session['id'],user_id)
		return redirect ('/friends')

	def view(self, user_id):
		viewfriend = self.models['User'].view_friend(user_id)
		return self.load_view('profile.html', viewfriend=viewfriend)


	# def delete(self, id):
	# 	self.models['User'].delete_user(id)
	# 	session.clear()
	# 	flash('You have successfully deleted yourself!')
	# 	return redirect('/')