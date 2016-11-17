#encoding=utf-8
from flask import Flask,render_template
from flask import make_response
from flask import redirect
from flask import abort
from flask import url_for
from flask_sqlalchemy import SQLAlchemy

#flask_script
from flask_script import Manager
from flask_script import Shell
#bootstrap
from  flask_bootstrap import Bootstrap

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)

#数据库
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:123456@localhost:3306/pythontest'
#这里登陆的是root用户，要填上自己的密码，MySQL的默认端口是3306，填上之前创建的数据库名text1
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
#设置这一项是每次请求结束后都会自动提交数据库中的变动
db = SQLAlchemy(app)#实例化

def make_shell_context():
	return dict(app=app, db=db, User=User, Role=Role)
manager.add_command("shell", Shell(make_context=make_shell_context))






'''
@app.route('/')
def index():
	return '<h1>Hello World!</h1>'
'''

'''
@app.route('/user/<name>')
def user(name):
	return '<h1>Hello, %s!</h1>' % name
'''


@app.route('/400')
def errorrout():
	return '<h1>Bad Request</h1>', 400	

@app.route('/response')
def response():
	response = make_response('<h1>This document carries a cookie!</h1>')
	response.set_cookie('answer', '42')
	return response
@app.route('/redirect')

#注意def定义的方法不能也叫作redirect
def redirect1():
	return redirect('http://www.baidu.com')

'''
@app.route('/user/<id>')
def get_user(id):
	user = load_user(id)
	if not user:
		abort(404)
		return '<h1>Hello, %s</h1>' % user.name
'''
#模板渲染
@app.route('/')
def index():
	return render_template('index.html')
@app.route('/user/<name>')
def user(name):
	'''
	mydict={'key':"key"}
	mylist=[1,2,999]
	myintvar=2
	'''
	#链接
	#打印 结果为 /
	print (url_for('index'))

	#打印结果为 http://localhost:5000/
	print (url_for('index', _external=True))

	#的返回结果是http://localhost:5000/user/john。
	print(url_for('user', name='john', _external=True)) 

	#静态文件
	print(url_for('static', filename='css/styles.css', _external=True))

	#return render_template('user.html',name=name,mydict=mydict,mylist=mylist,myintvar=myintvar)
	return render_template('user.html',name=name)

#模板继承
@app.route('/extends')
def extends():
	return render_template('extends.html')

#mysql数据库
# class Role(db.Model):
#     __tablename__ = 'roles' #定义表名
#     id = db.Column(db.Integer,primary_key=True)
#     #定义列对象
#     name = db.Column(db.String(64),unique=True)
#     user = db.relationship('User',backref='role',lazy='dynamic')#建立两表之间的关系，其中backref是定义反向关系，lazy是禁止自动执行查询（什么鬼？）

#     def __repr__(self):
#         return '<Role {}> '.format(self.name)

# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer,primary_key = True)
#     username = db.Column(db.String(64),unique=True,index=True)
#     role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

#     def __repr__(self):
#         return '<User {}>'.format(self.username)
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))


class Test(Base):
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(64))
    role_id = Column(Integer)









if __name__ == '__main__':
	#app.run(debug=True)
	#db.create_all()
	manager.run()
	
