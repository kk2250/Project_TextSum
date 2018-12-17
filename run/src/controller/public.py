#!/usr/bin/env python3

from flask import Blueprint,render_template,request,session,redirect,url_for,Flask,send_file
from gensim.summarization.summarizer import summarize
from werkzeug import secure_filename
import os
# from model import model

controller = Blueprint('public',__name__,static_folder='static',static_url_path='/static')

@controller.route('/',methods=['GET','POST'])
def frontpage():
    if request.method == 'GET':
        return render_template('homepage.html')
    elif request.method == 'POST':
        if request.form['paragraph_text']:
            text = request.form['paragraph_text']
            with open('run/src/static/ori_text.txt','w+') as f:
                f.write(text)
            try:
                summ1 = summarize(text)
                with open('run/src/static/textfile1.txt','w+') as f:
                    f.write(summ1)
                return redirect('/result')
            except ValueError:
                return render_template('homepage.html')
        elif request.files['fileselect']:
            text_file = request.files['fileselect']
            filename = secure_filename(text_file.filename)
            text_file.save(os.path.join("run/src/static/ori_text.txt"))
            with open('run/src/static/ori_text.txt','r') as f:
                content = f.read()
            summ2 = summarize(content)
            with open('run/src/static/textfile1.txt','w+') as f:
                f.write(summ2)
            return redirect('/result')
        else:
            return render_template('homepage.html')

@controller.route('/result',methods=['GET','POST'])
def results():
    if request.method == 'GET':
        with open('run/src/static/textfile1.txt','r') as f:
            summ = f.read()
        return render_template('printpage.html', message=summ)
    elif request.method == 'POST':
        with open('run/src/static/textfile1.txt','r') as ff:
            content = ff.read()
        summ1 = summarize(content)
        with open('run/src/static/textfile1.txt','w+') as fff:
            fff.write(summ1)
        return render_template('printpage.html', message=summ1)

@controller.route('/download')
def download():
    return send_file('/Users/kkim2250/Desktop/Project_TextSum/run/src/static/textfile1.txt', as_attachment=True, attachment_filename="textfile1.txt")