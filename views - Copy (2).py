from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('feedback_form.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    age = request.form.get('age')
    status = request.form.get('status')
    ladokite = request.form.get('ladokite')
    spending = request.form.get('spending')
    feedback = request.form.get('feedback')

    # Send email
    send_email(age, status, ladokite, spending, feedback)

    return "Feedback submitted successfully!"

def send_email(age, status, ladokite, spending, feedback):
    # Your Gmail credentials
    email_address = "carnivalcampus@gmail.com"
    email_password = "The flash1"
    recipient_email = "samuelolusegun181@gmail.com"

    # Email content
    subject = "New Campus Carnival Feedback"
    message = f"Age: {age}\nStatus: {status}\nLadokite: {ladokite}\nSpending: {spending}\nFeedback: {feedback}"

    # Create and send email
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(email_address, email_password)
        server.sendmail(email_address, recipient_email, msg.as_string())

if __name__ == '__main__':
    app.run(debug=True)
