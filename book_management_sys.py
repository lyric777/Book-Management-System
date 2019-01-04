from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from flask_script import Manager, Shell


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField
from wtforms.validators import Required


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
manager = Manager(app)

app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)


class Admin(db.Model):
    __tablename__ = 'admin'
    admin_id = db.Column(db.String(6), primary_key=True)
    admin_name = db.Column(db.String(32))
    password = db.Column(db.String(24))
    right = db.Column(db.String(32))

    def __repr__(self):
        return '<Admin %r>' % self.admin_name


class Book(db.Model):
    __tablename__ = 'book'
    isbn = db.Column(db.String(13), primary_key=True)
    book_name = db.Column(db.String(64))
    author = db.Column(db.String(64))
    press = db.Column(db.String(32))
    class_name = db.Column(db.String(64))

    def __repr__(self):
        return '<Book %r>' % self.book_name


class Student(db.Model):
    __tablename__ = 'student'
    card_id = db.Column(db.String(8), primary_key=True)
    student_id = db.Column(db.String(9))
    student_name = db.Column(db.String(32))
    sex = db.Column(db.String(2))
    telephone = db.Column(db.String(11), nullable=True)
    enroll_date = db.Column(db.Date)
    valid_date = db.Column(db.Date)
    loss = db.Column(db.Boolean, default=False)  # 是否挂失
    debt = db.Column(db.Boolean, default=False)  # 是否欠费

    def __repr__(self):
        return '<Student %r>' % self.student_name


class Inventory(db.Model):
    __tablename__ = 'inventory'
    barcode = db.Column(db.String(6), primary_key=True)
    isbn = db.Column(db.String(13))
    storage_date = db.Column(db.Date)
    location = db.Column(db.String(32))
    withdraw = db.Column(db.Boolean, default=False)  # 是否注销
    status = db.Column(db.Boolean, default=True)  # 是否在馆
    admin = db.Column(db.ForeignKey('admin.admin_id'))  # 入库操作员

    def __repr__(self):
        return '<Inventory %r>' % self.barcode


class ReadBook(db.Model):
    __tablename__ = 'readbook'
    id = db.Column(db.Integer, primary_key=True)
    barcode = db.Column(db.ForeignKey('inventory.barcode'), index=True)
    card_id = db.Column(db.ForeignKey('student.card_id'), index=True)
    start_date = db.Column(db.Date)
    borrow_admin = db.Column(db.ForeignKey('admin.admin_id'))  # 借书操作员
    end_date = db.Column(db.Date, nullable=True)
    return_admin = db.Column(db.ForeignKey('admin.admin_id'))  # 还书操作员
    due_date = db.Column(db.Date)  # 应还日期

    def __repr__(self):
        return '<ReadBook %r>' % self.id


def make_shell_context():
    return dict(app=app, db=db, Admin=Admin, Book=Book)


manager.add_command("shell", Shell(make_context=make_shell_context))


@app.route('/', methods=['GET', 'POST'])
def login():
    form = Login()
    return render_template('login.html', form=form)


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/admin/<name>')
def user(name):
    return render_template('index.html', name=name)


@app.route('/search_book')
def search_book():
    name = None
    form = SearchBookForm()
    return render_template('search-book.html', name=name, form=form)


class Login(FlaskForm):
    account = StringField('账号', validators=[Required()])
    password = PasswordField('密码', validators=[Required()])
    submit = SubmitField('登录')


class SearchBookForm(FlaskForm):
    methods = [('title', '书名'), ('author', '作者'), ('class', '类别'), ('isbn', 'ISBN')]
    method = SelectField(choices=methods)
    content = StringField(validators=[Required()])
    submit = SubmitField('搜索')


if __name__ == '__main__':
    manager.run()
