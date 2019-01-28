import yagmail
import sendgrid
import os
from sendgrid.helpers.mail import *
from sendgrid.models import Email

#yag = yagmail.SMTP("coolemail@you.com","coolpassword")


with open("template_to_send.html") as f:
    email_template = f.read()

abc = [{'email': 'kavyeshs41@gmail.com', 'name': 'Kavyesh Shah', 'location': 'Surat', 'skill': 'Node.Js'},{'email': 'kavyeshs42@gmail.com', 'name': 'Kavyesh Shah', 'location': 'Rajkot', 'skill': 'Ubuntu'}]

template_data = [tuple(_.values()) for _ in abc]

# template_data = [
#     ("kavyeshs41@gmail.com","Kavyesh Shah","Pune"),
#     ("kavyeshs42@gmail.com","Chucky","Pune"),
# ]



# for to_email, name, location, skill_name in template_data:
#     txt = email_template.format(name=name, location=location)
#     contents = [txt]
#     yag.send(to_email, "Job Openings", contents)

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("test-email@scikey.ai")
subject = "Sending with SendGrid is Fun"

for to_email, name, location, skill_name in template_data:
    txt = email_template.format(name=name, location=location)
    contents = [txt]






