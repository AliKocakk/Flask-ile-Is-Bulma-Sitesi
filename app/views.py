# views.py
from flask import Flask, render_template, request, redirect, url_for
from app import app,db
from app.models import About, Job, Expert, Application, mail
from flask_mail import Message, Mail





app.static_folder = 'static'
app.template_folder = 'templates'

@app.route('/')
def index():
    about_data = About.query.first()
    expert_data = Expert.query.limit(3).all()
    job_data = Job.query.limit(6).all()
    return render_template("index.html", about_data=about_data, experts=expert_data, jobs=job_data)

@app.route('/about')
def about():
    about_data = About.query.first()
    return render_template('about.html', about_data=about_data)

@app.route('/freelancer')
def freelancer():
    expert_data = Expert.query.all()
      
    return render_template('freelancer.html', experts=expert_data)

@app.route('/job')
def job():
    job_data = Job.query.all()  
    return render_template('job.html', jobs=job_data)  




@app.route('/apply/<int:job_id>', methods=['POST'])
def apply(job_id):
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        linkedin = request.form.get('linkedin')
        phone = request.form.get('phone')
        

        job = Job.query.get_or_404(job_id)
        application = Application(name=name, email=email, linkedin=linkedin, phone=phone, job=job)
        db.session.add(application)
        db.session.commit()

        

        return redirect(url_for('job'))




@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form.get('email')  

    
    message = Message('Hirevac Newsletter Subscription', recipients=[email])
    message.body = 'Thank you for subscribing to our newsletter!'
    mail.send(message)

    return redirect(url_for('index'))  



