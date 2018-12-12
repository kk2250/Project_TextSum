#!/usr/bin/env python3

from flask import Blueprint,render_template,request,session,redirect,url_for,Flask
# from model import model

controller = Blueprint('public',__name__)

@controller.route('/',methods=['GET','POST'])
def frontpage():
    if request.method == 'GET':
        return render_template('homepage.html')
    elif request.method == 'POST':
        text_file = request.file['upload']
        text = request.form['summ']
        if text_file:
            pass
            # model.sum(text_file)
            return render_template('templates/printpage.html', message=message)
        elif text:
            pass
            # model.sum(text)
            return render_template('templates/printpage.html', message=message)

@controller.route('/out',methods=['GET','POST'])
def printpage():
    if request.method == 'GET':
        return render_template('templates/printpage.html')
    elif request.method == 'POST':
        text_file = request.file['upload']
        text = request.form['summ']
        if text_file:
            pass
            # model.sum(text_file)
            return render_template('templates/printpage.html', message=message)
        elif text:
            pass
            # model.sum(text)
            return render_template('templates/printpage.html', message=message)