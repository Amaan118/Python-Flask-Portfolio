from flask import Flask, render_template, url_for, request, flash, redirect, send_file
import json
import smtplib


with open('config.json') as f:
    login_info = json.load(f)['login']

app = Flask(__name__)
app.secret_key = login_info['secret_key']
app.config['SESSION_TYPE'] = login_info['session']

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/project', methods=['GET', 'POST'])
def project():
    return render_template('project.html')

@app.route('/proj_det')
def details():
    return render_template('details.html')
    
@app.route('/academic')
def academic():
    return render_template('academic.html')

@app.route('/ssc')
def ssc():
    return render_template('ssc.html')

@app.route('/hsc')
def hsc():
    return render_template('hsc.html')

@app.route('/ug')
def ug():
    return render_template('ug.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/resume')
def resume():
    return send_file('static/download/resume.pdf')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method=='POST':
        try:
            name = request.form['name']
            email = request.form['email']
            phone = request.form['contact']
            descript = request.form['desc']
            
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(login_info['email'], login_info['password'])
            body = f'''
            Portfolio Response by {name},
            {descript} 
            From : {email}
            Contact Number : {phone}'''

            server.sendmail(email, [login_info['email']], body)

            flash('Thank You for the Message. I will reach out to you soon !', 'success')
        except:
            flash('Failed to Send Email. You can try after some time.', 'danger')
            
        return redirect('/contact')
    return render_template('contact.html')

    
if __name__=='__main__':
    app.run(debug=False)