from django.shortcuts import redirect, render
from flask import Flask, request, jsonify, make_response, send_from_directory, send_file, render_template, url_for
import os
import flask
from flask_cors import CORS
import pandas as pd
import numpy as np


app = Flask(__name__)
CORS(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/generalUser')
def blog():
    return render_template('blog.html')

@app.route('/userResult')
def userResult():
    return render_template('result.html')


@app.route('/signup', methods = ['POST', 'GET'])
def signup():
    print("signup")

    name = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")
    data = request.data

    print(name)
    print(email)
    print(password)

    if email == "sarthak@slack.com":
        return flask.redirect("http://127.0.0.1:5000/devResult")

        
    return render_template('blog.html')
    #     return redirect(url_for('))
    

    # if _name and _email and _password:
    #     return redirect(url_for('home'))


@app.route('/signin', methods = ['POST', 'GET'])
def signin():
    print("signin")

    email = request.form.get("email")
    password = request.form.get("password")
    
    print(email)
    print(password)

    if email == "sarthak@slack.com":
        return flask.redirect("http://127.0.0.1:5000/devResult")

        
    return render_template('blog.html')
    #     return redirect(url_for('))
    

    # if _name and _email and _password:
    #     return redirect(url_for('home'))




@app.route('/loggedIn', methods = ['POST', 'GET'])
def loggedIn():
    _name = request.form.get("inputName")
    if(_name):
        if(_name == "sarthak@slack.com"):
            return render_template('resultDeveloper.html')
    return render_template('blog.html')


@app.route('/devResult')
def res():
    # result,continuation_token= reviews('com.Slack',lang='en',country='us',sort=Sort.MOST_RELEVANT, count=1000)
    df = pd.read_csv ('roxy\\app_reviews_slack.csv')

    count_1,count_2,count_3,count_4 = 0,0,0,0
    # count_1v2,count_2v2,count_3v2,count_4v2 = 0,0,0,0

    idx1,idx2,idx3,idx4 = 0,0,0,0

    reg_dict = {}
    reg_dictv2 = {}
    int_dict = {}
    int_dictv2 = {}
    app_dict = {}
    app_dictv2 = {}
    not_dict = {}
    not_dictv2 = {}


    for i in df['RegistrationIssues']:
        if i>0.7 and idx1<=8:
            my_formatter = "{0:.2f}"
            reg_dict[df['processed_review'][count_1]] = str(my_formatter.format(i*100))+"%"
            idx1+=1

        elif idx1>8 and i>0.7:
            my_formatter = "{0:.2f}"
            reg_dictv2[df['processed_review'][count_1]] = str(my_formatter.format(i*100))+"%"
            idx1+=1

        count_1+=1


        if idx1 ==16:
            break
    # count_2 = 0
    for i in df['Notification Issues']:
        if i>0.7 and idx2<=8:
            my_formatter = "{0:.2f}"
            not_dict[df['processed_review'][count_2]] = str(my_formatter.format(i*100))+"%"
            idx2+=1
        elif idx2>8 and i>0.7:
            my_formatter = "{0:.2f}"
            not_dictv2[df['processed_review'][count_2]] = str(my_formatter.format(i*100))+"%"
            idx2+=1

        count_2+=1
        if idx2 == 16:
            break

    # count_3 = 0
    for i in df['Slack Desktop/Mobile App Issues']:
        if i>0.7 and idx3<=8:
            
            my_formatter = "{0:.2f}"
            app_dict[df['processed_review'][count_3]] = str(my_formatter.format(i*100))+"%"
            idx3+=1

        elif idx3>8 and i>0.7:
            my_formatter = "{0:.2f}"
            app_dictv2[df['processed_review'][count_3]] = str(my_formatter.format(i*100))+"%"
            idx3+=1

        count_3+=1
        if idx3 == 16:
            break

    # count_4 = 0
    for i in df['Interface Issues']:
        if i>0.7 and idx4<=8:
            my_formatter = "{0:.2f}"
            int_dict[df['processed_review'][count_4]] = str(my_formatter.format(i*100))+"%"
            # print(int_dict[df['processed_review'][count_4]])
            idx4+=1
        elif idx4>8 and i>0.7:
            my_formatter = "{0:.2f}"
            int_dictv2[df['processed_review'][count_4]] = str(my_formatter.format(i*100))+"%"
            print(int_dictv2[df['processed_review'][count_4]])
            idx4+=1

        count_4+=1
        if idx4 == 16:
            break
            
    cols = []

    for i in df.columns:
        cols.append(i)

    cols.pop(0)
    cols.pop(0)

    cols.append("Audio Call Issues")

    cols[0] = "Registration Issues"

    patch_status = ['Pending','Fixed','Fixed','Pending','In-progress']

    dict_bug = {}

    for i in range(len(cols)):
        dict_bug[cols[i]]=patch_status[i]
    
    
    version_ = ['2018.11.07','2018.11.28','2017.01.16','2018.10.24','21.10.10.0']

    reviewRelated = ["""
    What’s New• Now, after you confirm your email, you’ll see a list of your workspaces, 
    and pick which ones you’d like to sign into. And then sign into them!• You can now 
    receive notifications while using the app, so If you're catching up on a channel and 
    you receive a DM you won't miss it (and if that doesn't sound like something you'd want, you'll find this in the notification settings menu)."""
    , """ What’s New• Need to pause notifications? Thinking of going on vacation for more than 24 hours? Good news. 
    You can pause them beyond a single day, or until a specific date or time.
     And we’ve also added two new presets to our existing list: “Until tomorrow” and “Until next week”. 
     A veritable panoply of new options for pausing notifications! Or, at the very least, "several"!""",
     """Slack 2.26.1 Release Notes:Highlights:• To match the desktop app, when you use @everyone or @channel, 
     we’ll now pop up a reminder of how many people you’ll be alerting (and how many time zones they might be in). 
     Because one small act of courtesy can save a whole lot of awkwardness later on.
     Full Release Notes:https://slack-files.com/T12KS1G65-F3PUXQ08N-528ebdc96b""",
     """What’s New• If your device is running Oreo or a more recent version of Android, 
     you'll now find your notifications sorted into categories, 
     giving you more control over how and when you see them.""",
     """What’s New, You can now record video and audio clips right within Slack. 
     Add some face time to your team updates, talk through feedback, or just say hello. 
     Want to sing your portion of the stand-up? Best check with your manager on that one.
     The channel list just got a little friendlier. 
     You’ll now see avatars next to your Direct Messages, and for those group conversations with lots of names, 
     we’ve given you a bit more space to see just who it is you’re talking to."""
     ]

    
    # return render_template('resultDeveloper.html')

    return render_template('new_results.html',reg_dict=reg_dict,int_dict=int_dict,not_dict=not_dict,app_dict=app_dict,
         reg_dictv2 = reg_dictv2, int_dictv2 = int_dictv2, app_dictv2 = app_dictv2,not_dictv2=not_dictv2,dict_bug=dict_bug)
# def result():
#     return render_template('resultDeveloper.html')





if __name__ == "__main__":
    app.run(debug=True)
