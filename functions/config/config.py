import os

current_dir = os.path.dirname(os.path.realpath(__file__))

SCOPES = ['https://www.googleapis.com/auth/analytics openid https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile']
R_URI = "http://localhost:5000/v1/connect/webhook/ga_integration"
SECRET = current_dir + "/secret.json"