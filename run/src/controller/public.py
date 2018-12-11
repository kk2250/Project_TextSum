#!/usr/bin/env python3

from flask import Blueprint,render_template,request,session,redirect,url_for


controller = Blueprint('public',__name__)

@controller.route('/',methods=['GET','POST'])
def frontpage():
    if request.method == 'GET':
        return render_template('templates/homepage.html', message=message)
    elif request.method == 'POST':
        text = request.form['summarize']
        
        return render_template('templates/homepage.html', message=message)
