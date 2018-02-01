# flask imports
from flask import Flask, Response, render_template, request, redirect, url_for, flash

# SQLAlchemy
from model import Base, Job, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# setup
app = Flask(__name__)
app.config["SECRET_KEY"]="malak"
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# flask-login imports
from flask_login import login_required, current_user
from login import login_manager, login_handler, logout_handler, sign_up_handler
login_manager.init_app(app)


# @login_required
@app.route('/home')
def home():
        Jobs_here = session.query(Job).all()
        return render_template('home.html',Jobs=Jobs_here)

# @login_required
@app.route('/about')
def about():
        return render_template('about.html')

@app.route('/show_job/<int:job_id>')
def show_job(job_id):
        Jobs_here = session.query(Job).filter_by(id=job_id).first()
        return render_template('about_job.html', job=Jobs_here)

@app.route('/apply/<int:job_id>')
def apply(job_id):
        Jobs_here = session.query(Job).filter_by(id=job_id).first()
        return render_template('apply.html', job=Jobs_here)

@app.route('/delete/<int:job_id>')
def delete(job_id):
        Jobs_here = session.query(Job).filter_by(id=job_id).first()
        session.delete(Jobs_here)
        session.commit()
        return redirect(url_for('home'))


# @login_required
@app.route('/add_job',methods=['GET','POST'])
def add_job():
    if request.method == 'GET':
        return render_template('add_job.html')
    else:  
        new_job_name      = request.form.get('job')
        new_about         = request.form.get('about')
        new_frequency     = request.form.get('frequency')
        new_date          = request.form.get('date')
        new_payment       = request.form.get('payment')
        new_picture       = request.form.get('picture')
        new_email         = current_user.email
        new_Job = Job(job=new_job_name,about= new_about,frequency=new_frequency,date=new_date,payment=new_payment,picture=new_picture,email=new_email)

        session.add(new_Job)
        session.commit()
        return redirect(url_for('home'))



############ LOGIN ############
@app.route('/sign_in', methods=['GET', 'POST'])
def login():
    return login_handler(request)



@app.route('/logout')
def logout():
	return logout_handler()


@app.route('/sign_up', methods=["GET", "POST"])
def sign_up():
	print (request.method)
	if request.method == 'GET':
		return render_template('sign_up.html')
	else:
		sign_up_handler(request)
		return redirect(url_for('home'))

if __name__=='__main__':
	app.run(debug=True)