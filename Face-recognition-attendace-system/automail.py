import os
import yagmail
from twilio.rest import Client
import webbrowser
import requests
def send_mail(receiver_mail,reveiver_whatsapp_number):
    receiver = "add receiver mail"  # receiver email address
    body = "Attendence File"  # email body
    filename = "Attendance"+os.sep+"Attendance_2019-08-29_13-09-07.csv"  # attach the file
    filename = [os.path.join("Attendance", f) for f in os.listdir("Attendance")]
    #print(filename)
    print("You have entered your mail:"+receiver_mail)
    print("You have entered your whatsapp number:"+reveiver_whatsapp_number)
    file=filename[-1]
    #print(file)
    os.startfile(file)
    # mail information
    yag = yagmail.SMTP("use your mail", "use your mail password")

    # sent the mail
    yag.send(
        to=receiver,
        subject="Attendance Report",  # email subject
        contents=body,  # email body
        attachments=file,  # file attached
    )
    account_sid = 'twilio id' 
    auth_token = 'twilio token' 
    client = Client(account_sid, auth_token) 
    message = client.messages.create( 
                                  from_='whatsapp:twilio whatsapp number with country code',  
                                  body=f"Your Attendance will be accepted, please check your mail",      
                                  to='whatsapp:+91whatsappnumber'
                              )
