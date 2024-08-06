# from google.oauth2.credentials import Credentials

# creds = Credentials.from_authorized_user_file('G:/CrevHim/Code/software/test/testall/credentials.json', scopes=['https://www.googleapis.com/auth/youtube.force-ssl'])


# # from googleapiclient.discovery import build

# # youtube = build('youtube', 'v3', credentials=creds)

# # video_id = 'BtqU9bAkCro'

# # response = youtube.videos().list(
# #     part='statistics',
# #     id=video_id
# # ).execute()

# # likes = int(response['items'][0]['statistics']['likeCount'])
# # comments = int(response['items'][0]['statistics']['commentCount'])
# # shares = int(response['items'][0]['statistics']['shareCount'])
# # views = int(response['items'][0]['statistics']['viewCount'])

# # engagement = (likes + comments + shares) / views

# # print('Engagement rate:', engagement)

# import requests

# set the TikTok API endpoint and parameters
# endpoint = "https://api.tiktok.com/api/user/detail"
# params = {
#     "unique_id": "cretivox",
#     "language": "en"
# }

# # send the API request and parse the response JSON
# response = requests.get(endpoint, params=params)
# data = response.json()

# # extract the engagement data from the response
# likes = data["userInfo"]["stats"]["diggCount"]
# comments = data["userInfo"]["stats"]["commentCount"]
# shares = data["userInfo"]["stats"]["shareCount"]
# followers = data["userInfo"]["stats"]["followerCount"]

# # calculate the engagement rate
# engagement_rate = ((likes + comments + shares) / followers) * 100

# print("Likes:", likes)
# print("Comments:", comments)
# print("Shares:", shares)
# print("Followers:", followers)
# print("Engagement Rate:", engagement_rate)



import instaloader

from flask import Flask, request, make_response, jsonify, Response, current_app
from werkzeug.utils import secure_filename
from flask_restful import Resource, Api 
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy 
import instaloader
from datetime import date
from sqlalchemy import JSON
import json

import requests
import sqlite3
from werkzeug.datastructures import FileStorage

import os
import pandas as pd 
import numpy as np
from datetime import date

bot = instaloader.Instaloader()

app = Flask(__name__)
api = Api(app)

with app.app_context():
    # within this block, current_app points to app.
    print(current_app.name)

CORS(app)


#setting database
filename = os.path.dirname(os.path.abspath(__file__))
database = 'sqlite:///' + os.path.join(filename, 'dbcomic.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = database 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()

# def set_my_array(self, array):
#         self.my_array = json.dumps(array)

# def get_my_array(self):
#     return json.loads(self.my_array)

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

class Ig(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.Text)
    name = db.Column(db.Text)
    mimetype = db.Column(db.Text)
    
class yt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.String(255))
    datayt = db.Column(JSON)
    
class talent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    datadate = db.Column(db.String(255))
    content = db.Column(db.String(255))
    shooting = db.Column(db.Text)
    rate = db.Column(db.Text)
    note = db.Column(db.Text)
    
    
    
db.create_all()

class igtry(Resource):
    def post(self):
        bot = instaloader.Instaloader()
        profileid = "cretivox"
        profile = instaloader.Profile.from_username(bot.context, profileid)
        url = profile.get_profile_pic_url()
        print(url)

        response = requests.get(url)
        pic = request.files['pic']
        pic2 = FileStorage(stream=response.content, filename='image.jpg', content_type=response.headers['Content-Type'])
        print(type(pic))
        print(type(pic2))
        mimetype = pic.mimetype
        # print(pic.read())
        # print(mimetype)
        con1 = Ig(
                  img = pic.read(),
                  name = 'image.jpg',
                  mimetype = mimetype
                  )
        mimetype = pic2.mimetype
        con2 = Ig(
                  img = response.content,
                  name = 'image.jpg',
                  mimetype = mimetype
                  )

        db.session.add(con1)
        db.session.add(con2)
    
        db.session.commit()
        return make_response({"msg" : "success"}, 200)
    
class GetImgInsta(Resource):
    def get(self, id):
        print(id)
        img = Ig.query.filter(Ig.id == id).first()
        # print(img.img)
        if not img:
           return jsonify({"msg":"bad request"}) 
        return Response(img.img, mimetype=img.mimetype) 

class yttry(Resource):
    def post(self):
        note = request.form.get('note')
        file = request.files['file']
        datayt = []
        
        
        df = pd.read_csv(file)
        total = df.iloc[0]
        print(df)
        
        for i in range(1,len(df.index)):
            x = df.iloc[i]
            jsyt = {
                "Content":x["Content"],
                "Video_title":x["Video title"],
                "Video_publish":x["Video title"],
                "Shares": x["Shares"],
                "Subscribers_lost": x["Subscribers lost"],
                "Subscribers_gain":x["Subscribers gained"],
                "Views":x["Views"],
                "Watch_time":x["Watch time (hours)"],
                "Subscribers":x["Subscribers"],
                "Impression":x["Impressions"],
                "impressions_click" : x["Impressions click-through rate (%)"]
            }
            datayt.append(jsyt)
            
        jstotal = [{
            "total_share" : total["Shares"],
            "total_sub_lost" : total["Subscribers lost"],
            "total_sub_gained" : total["Subscribers gained"],
            "total_views" : total["Views"],
            "total_watch_time" : total["Watch time (hours)"],
            "total_sub" : total["Subscribers"],
            "total_impressions" : total["Impressions"],
            "total_impressions_click" : total["Impressions click-through rate (%)"],
            "notes" : note,
            "data" : datayt
            
        }]
        

        # print(jstotal)
        con2 = yt(
                  note = note,
                  datayt = json.dumps(jstotal, cls=NpEncoder)
                  )

        db.session.add(con2)
    
        db.session.commit()
        return make_response({"msg" : "success"}, 200)

    def get(self):
        dataQuery = yt.query.all() 
        output = []
        for i in range(len(dataQuery)):
            x = {
                "id" : dataQuery[i].id,
                "data_yt" : json.loads(dataQuery[i].datayt)
            }
            output.append(x)
        
        return make_response(jsonify(output), 200)         
    
    def delete(self):
        db.session.query(yt).delete()
        db.session.commit()
        
        return jsonify({"msg":"Deleted"})    
      
class yttryto(Resource):
    def get(self, id):
        # print(data)
        
        data = yt.query.filter(yt.id == id).first()
        output = [{
            "id" : data.id,
            "data_yt" : json.loads(data.datayt)
        }
        ]
        return make_response(jsonify(output), 200)

class talentall(Resource):
    def post(self):
        name = request.form.get('name')
        d2 = date.today()
        content = request.form.get('content')
        shooting = request.form.get('shooting')
        rate = request.form.get('rate')
        note = request.form.get('note')
        
        con1 = talent(
            name = name,
            datadate = d2,
            content = content,
            shooting = shooting,
            rate = rate,
            note = note
        
        )
        
        db.session.add(con1)
    
        db.session.commit()
        return make_response({"msg" : "success"}, 200)

    def get(self):
        dataQuery = talent.query.all()
        output = []
        for i in range(len(dataQuery)):
            x = {
                "id" : dataQuery[i].id,
                "Name" : dataQuery[i].name,
                "Date" : dataQuery[i].datadate,
                "Content" : dataQuery[i].content,
                "Shooting_Experience" : dataQuery[i].shooting,
                "Rating_Bintang" : float(dataQuery[i].rate),
                "Notes" : dataQuery[i].note
            }
            output.append(x)
        
        return make_response(jsonify(output), 200) 
    
    def delete(self):
        db.session.query(talent).delete()
        db.session.commit()
        
        return jsonify({"msg":"Deleted"})  
    
class talentto(Resource):
    def get(self,id):  
        data = talent.query.filter(talent.id == id).first()
        output = [{
            "id" : data.id,
            "Name" : data.name,
            "Date" : data.datadate,
            "Content" : data.content,
            "Shooting_Experience" : data.shooting,
            "Rating_Bintang" : float(data.rate),
            "Notes" : data.note
        }
        ]
        return make_response(jsonify(output), 200)
    
    def put(self,id):
        pass
    
    def delete(self,id):
        own = talent.query.filter(talent.id == id).first()
        db.session.delete(own)
        db.session.commit()

        return make_response(jsonify({"msg" : "deleted"}), 200)
        

api.add_resource(talentall, "/talent", methods=["POST", "GET", "DELETE"])
api.add_resource(talentto, "/talent/<id>", methods=["GET", "DELETE"])

api.add_resource(yttry, "/yt", methods=["POST", "GET", "DELETE"])
api.add_resource(yttryto ,"/yt/<id>", methods=["GET"])    
    
api.add_resource(igtry, "/insta", methods=["POST"])
api.add_resource(GetImgInsta, "/insta/picture/<id>", methods=["GET"])

if __name__ == "__main__":
    app.run(debug=True,port=66, host="0.0.0.0")