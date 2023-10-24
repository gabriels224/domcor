import pyrebase
import os
import firebase_admin
from firebase_admin import auth as firebase_auth
from firebase_admin import credentials
import pickle
import os
from flet import *
import datetime
from functools import partial

cred = credentials.Certificate('service_acont.json')
firebase_admin.initialize_app(cred)


firebaseConfig = {
    "apiKey": "AIzaSyC2nSudO3CBQR2pl8k1MRUacEGkfmXxn4E",
    "authDomain": "domcorts01.firebaseapp.com",
    "projectId": "domcorts01",
    "storageBucket": "domcorts01.appspot.com",
    "messagingSenderId": "548755608996",
    "appId": "1:548755608996:web:7119e4a586029de7099d31",
    "measurementId": "G-YRPLMZJ5NR",
    'databaseURL': "https://domcorts01-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


email = 'email@exemplo.com'
password = 'senha@1232'
name = "Seu nome"

def Criar_usuario(name, email, password):
    try:
        user = firebase_auth.create_user(
            email=email,
            password=password,
            display_name=name
        )
        return user.uid
    except:
        return None
    
def login_usuario(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return user['idToken']
    except:
        return None
    

def store_token(token):
    if os.path.exists('token.pickle'):
        os.remove('token.pickle')
    with open("token.pickle", 'wb') as f:
        pickle.dump(token, f)


def rekove_token(token):
    firebase_auth.revoke_refresh_tokens(token)
    if os.path.exists('token.pickle'):
        os.remove('token.pickle')