from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField
from wtforms.validators import DataRequired


class Login(FlaskForm):
    account = StringField(u'账号', validators=[DataRequired()])
    password = PasswordField(u'密码', validators=[DataRequired()])
    submit = SubmitField(u'登录')


class SearchBookForm(FlaskForm):
    methods = [('title', '书名'), ('author', '作者'), ('class', '类别'), ('isbn', 'ISBN')]
    method = SelectField(choices=methods)
    content = StringField(validators=[DataRequired()])
    submit = SubmitField('搜索')
