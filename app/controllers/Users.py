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

	def show(self, id):
		user = self.models['User'].get_user_by_id(id)
		return self.load_view('show.html', user=user)


	def register(self): 
		status = self.models['User'].register_user(request.form)
		if status['status']:
			session['name'] = request.form['name']
			session['id'] = status['user_id']
			flash('You have successfully registered!')
			return self.load_view('success.html')
		else:
			for message in status['errors']:
				flash(message, 'regis_errors')
			return redirect('/')

	def logout(self):
		session.clear() 
		flash('You are now logged out')
		return redirect('/')

	def friends(self):
		status = self.models['User'].friends_process(request.form)
		if status:	
			session['id'] = status['id']
			session['name'] = status['name']
			return self.load_view('success.html', name=session['name'])
		else:
			flash('Invalid Password')		
			return redirect('/')

	# def update(self, user_id):
	# 	return self.load_view('delete.html')

	def destroy(self, id):
		return self.load_view('delete.html', id=id)

	def delete(self, id):
		self.models['User'].delete_user(id)
		session.clear()
		flash('You have successfully deleted yourself!')
		return redirect('/')