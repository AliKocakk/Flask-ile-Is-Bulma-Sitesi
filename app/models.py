from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin
from flask_mail import Mail

from app import app, db




app.config['MAIL_SERVER'] = 'smtp.office365.com'
app.config['MAIL_PORT'] = ***
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'alikocak****@hotmail.com'
app.config['MAIL_PASSWORD'] = '***'
app.config['MAIL_DEFAULT_SENDER'] = 'alikocak2035@hotmail.com'

mail = Mail(app)



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(255))
    is_admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class AdminUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)  
    #role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    #role = db.relationship('Role', backref=db.backref('users', lazy=True))


admin = Admin(app, name='Hirevac Admin and Editing Panel', template_mode='bootstrap4')

class UserAdmin(ModelView):
    column_list = ('username', 'email', 'is_admin')
    column_labels = {'username': 'Username', 'email': 'Email Address', 'is_admin': 'Admin'}
    column_filters = ('username', 'email', 'is_admin')

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin  




class AboutAdmin(ModelView):
    column_list = ('title', 'content', 'image_filename')
    column_labels = {'title': 'About Title', 'content': 'About Content', 'image_filename': 'Image Filename'}
    column_filters = ('title', 'content', 'image_filename')
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin
    
admin.add_view(UserAdmin(User, db.session))
#admin.add_view(RoleAdmin(Role, db.session))

#admin.add_view(PostAdmin(Post, db.session))






class About(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    image_filename = db.Column(db.String(255))

    def __repr__(self):
        return f"<About {self.title}>"
    
admin.add_view(AboutAdmin(About, db.session))




class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(100))
    salary_range = db.Column(db.String(50))
    image_filename = db.Column(db.String(255))


class JobAdmin(ModelView):
    column_list = ('title', 'location', 'salary_range', 'image_filename')
    column_labels = {'title': 'Job Title', 'location': 'Location', 'salary_range': 'Salary Range', 'image_filename': 'Image Filename'} 
    column_filters = ('title', 'location', 'salary_range', 'image_filename')
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

admin.add_view(JobAdmin(Job, db.session))



class Expert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    position = db.Column(db.String(255), nullable=False)
    jobs_done = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_filename = db.Column(db.String(255))
class ExpertAdmin(ModelView):
    column_list = ('name', 'position', 'jobs_done', 'rating')
    column_labels = {'name': 'Expert Name', 'position': 'Position', 'jobs_done': 'Jobs Done', 'rating': 'Rating'}
    column_filters = ('name', 'position', 'jobs_done', 'rating')
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

        
admin.add_view(ExpertAdmin(Expert, db.session))


    
    
class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    linkedin = db.Column(db.String(255))
    phone = db.Column(db.String(20))
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=True)
    job = db.relationship('Job', backref=db.backref('applications', lazy=True))

class ApplicationAdmin(ModelView):
    column_list = ('name', 'email', 'linkedin', 'phone', 'job')  
    form_columns = ('name', 'email', 'linkedin', 'phone', 'job')  
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin


admin.add_view(ApplicationAdmin(Application, db.session))





