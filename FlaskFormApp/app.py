from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Replace with your email provider's SMTP server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'louie08111louie@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'bygy jgba jjah mbve'  # Replace with your email password
app.config['MAIL_DEFAULT_SENDER'] = 'louie08111louie@gmail.com'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    form_data = request.form
    # Create the email content
    subject = "New Form Submission"
    recipient = "louie08111louie@gmail.com"  # Replace with the recipient's email address
    body = f"""
    姓名: {form_data.get('name')}
    性別: {form_data.get('gender')}
    年齡: {form_data.get('age')}
    職業類型: {form_data.get('jobType')}
    聯繫電話: {form_data.get('phone')}
    聯繫電話: {form_data.get('time')}
    電子郵件: {form_data.get('email')}
    建案名稱: {form_data.get('buildingName')}
    建案地址: {form_data.get('buildingAddress')}
    屋況: {form_data.get('houseStatus')}
    戶型: {form_data.get('apartmentType')}
    樓層: {form_data.get('floor')}
    預計交屋日期: {form_data.get('completionDate')}
    預計入住時間: {form_data.get('contactPerson')}
    總預算: {form_data.get('budget')}
    權狀坪/室內坪數: {form_data.get('rooms')}
    現有格局: {form_data.get('layout')}
    人員數量: {form_data.get('family')}
    設計風格篇好: {form_data.get('preferences')}
    設計需求說明: {form_data.get('designRequirements')}
    如何知道京悅: {form_data.get('source')}
    
    """  # Include other form fields as needed

    # Send the email
    msg = Message(subject=subject, recipients=[recipient], body=body)
    mail.send(msg)

    print("Email sent successfully")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
