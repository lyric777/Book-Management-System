from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField
from wtforms.validators import DataRequired, EqualTo


class Login(FlaskForm):
    account = StringField(u'账号', validators=[DataRequired()])
    password = PasswordField(u'密码', validators=[DataRequired()])
    submit = SubmitField(u'登录')


class SearchBookForm(FlaskForm):
    methods = [('title', '书名'), ('author', '作者'), ('class', '类别'), ('isbn', 'ISBN')]
    method = SelectField(choices=methods)
    content = StringField(validators=[DataRequired()])
    submit = SubmitField('搜索')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField(u'请输入原密码', validators=[DataRequired()])
    password = PasswordField(u'请输入新密码', validators=[DataRequired(), EqualTo('password2', message=u'两次密码必须一致！')])
    password2 = PasswordField(u'再次输入新密码', validators=[DataRequired()])
    submit = SubmitField(u'确认修改')
