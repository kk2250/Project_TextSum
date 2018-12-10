#!/usr/bin/env python3

from flask import Blueprint,render_template,request,session,redirect,url_for
import src.models.model as model
import sqlite3
import datetime as dt


controller = Blueprint('public',__name__)

@controller.route('/',methods=['GET','POST'])
def globall():
    if request.method == 'GET':
        tweets = model.fetchall_tweets()
        list_of_tweets = []
        for _ in tweets:
            q = [_[1],_[2],_[3]]
            list_of_tweets.insert(0, q)
        return render_template('unauthorized/global.html', list_of_tweets=list_of_tweets)

@controller.route('/login',methods=['GET','POST'])
def log_in():
    if request.method == 'GET':
        return render_template('unauthorized/login.html')