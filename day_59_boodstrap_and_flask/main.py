from flask import Flask, render_template, request
from collector_post import Post
import smtplib

app = Flask(__name__)

@app.route('/')
def init():
    post_r = Post(1)
    data = post_r.data()
    return render_template('index.html', data= data)

@app.route("/post/<num_id>")
def post(num_id):
    id = int(num_id)
    colle = Post(id)
    body = colle.collect_body()
    title = colle.collect_title()
    subtitle = colle.collect_subtitle()

    return render_template('post.html', title= title, body= body, subtitle= subtitle)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/form_entry', methods=['POST'])
def receive_data():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']
    send_email(name, email, phone, message)
    return "Your message was send successfully"

def send_email(name, email, phone, message):
    my_email = "samukakaroto123@gmail.com"
    password = "wplk zuyj gapn ntrs"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="samukakaroto123@gmail.com", msg=f"Subject:New Message\n\nNome: {name}\n Email: {email}\n Phone: {phone}\n Message: {message}")
        connection.close()

if __name__ == "__main__":
    app.run(debug=True)