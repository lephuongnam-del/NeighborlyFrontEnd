import logging.config
import os
from flask import Flask, Blueprint, request, jsonify, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
import settings
import requests
import json
# from feedgen.feed import FeedGenerator
from flask import make_response
from urllib.parse import urljoin
from werkzeug.contrib.atom import AtomFeed

app = Flask(__name__)
Bootstrap(app)



# def get_abs_url(url):
#     """ Returns absolute url by joining post url with base url """
#     return urljoin(request.url_root, url)


# @app.route('/feeds/')
# def feeds():
    # feed = AtomFeed(title='All Advertisements feed',
    #                 feed_url=request.url, url=request.url_root)

    # response = requests.get(settings.API_URL + '/getAdvertisements')
    # posts = response.json()

    # for key, value in posts.items():
    #     print("key,value: " + key + ", " + value)

    #     feed.add(post.title,
    #              content_type='html',
    #              author= post.author_name,
    #              url=get_abs_url(post.url),
    #              updated=post.mod_date,
    #              published=post.created_date)

    # return feed.get_response()


# @app.route('/rss')
# def rss():
#     fg = FeedGenerator()
#     fg.title('Feed title')
#     fg.description('Feed Description')
#     fg.link(href='https://neighborly-client-v1.azurewebsites.net/')
    

#     response = requests.get(settings.API_URL + '/getAdvertisements')
#     ads = response.json()

#     for a in ads: 
#         fe = fg.add_entry()
#         fe.title(a.title)
#         fe.description(a.description)

#     response = make_response(fg.rss_str())
#     response.headers.set('Content-Type', 'application/rss+xml')
#     return response

@app.route('/')
def home():
    # response = requests.get(settings.API_URL + '/getAdvertisements')
    # response2 = requests.get(settings.API_URL + '/getPosts')
    # response = {}
    # response2 = {}

    posts = [ { "_id": "5ec34cb625f7e6b04907fbad", "title": "Food distribution", "city": "Hyattsville", "description": "Hi I think —not sure— there is a food distribution at going on now in our neighborhood community center?", "imgUrl": "https://www.bocaratontribune.com/wp-content/uploads/2020/04/IMG_0757-768x576.jpg", "publishedDate": "Sun May 17 2020 23:04:22 GMT-0400 (Eastern Daylight Time)" }, { "_id": "5ec34cb6a611ef690a38dc09", "title": "Need a haircut!", "city": "Riverdale Park", "description": "Can someone come to my yard and cut my hair?  I will wear a mask and also provide gloves an facemasks.  Contact Jessy at jessy@example.com", "imgUrl": "https://i.pinimg.com/564x/57/63/87/576387d0c55bb5a3e5dead09ac578fc5.jpg", "publishedDate": "Mon May 18 2020 20:04:22 GMT-0400 (Eastern Daylight Time)" }, { "_id": "5ec34cb6d1d76535514b91d9", "title": "aliquip veniam in eiusmod qui", "description": "Deserunt exercitation magna consequat nisi ullamco. Ullamco id ad proident non ullamco pariatur ad enim reprehenderit tempor aute cupidatat nostrud. Eiusmod cillum qui fugiat dolor. Commodo adipisicing est est commodo nisi eiusmod Lorem.\r\n", "imgUrl": "http://placehold.it/32x32", "publishedDate": "Mon May 18 2020 01:04:22 GMT-0400 (Eastern Daylight Time)" }, { "_id": "5ec34cb666a8e2c4f3c36cfd", "title": "sit culpa Lorem enim pariatur", "description": "Aliqua sunt aliqua laborum in ex Lorem. Culpa occaecat adipisicing proident nisi elit officia duis ullamco ea exercitation eu pariatur. Qui qui pariatur magna ullamco amet.\r\n", "imgUrl": "http://placehold.it/32x32", "publishedDate": "Wed May 21 2020 03:04:22 GMT-0400 (Eastern Daylight Time)" } ]
    ads = [ { "_id": "5ec34b22b5f7f6eac5f2ec3e", "title": "[testaccount111] Honda Tacoma pick up - low milage.", "description": "Manual transmission.  Great truck, clean title. Cash only.", "price": "$3,587.05", "city": "Poolsville" }, { "_id": "5ec34b22c800f5f824c21490", "title": "Lost cat reward if found.", "description": "My fat tabby disappeared last nite on 49th and Taylor.", "price": "0.00" }, { "_id": "5ec34b22f764357ce29a775e", "title": "Trailer", "description": "Ullamco nulla adipisicing esse occaecat ipsum deserunt. Est excepteur tempor eiusmod non. Eiusmod occaecat enim eiusmod nostrud mollit.\r\n", "price": "$1,703.56" }, { "_id": "5ec34b2265403b17d00ae864", "title": "Lawn mower", "description": "Sunt eiusmod occaecat deserunt magna Lorem cillum non consequat minim do.\r\n", "price": "$520.13" }, { "_id": "5ec34b228eac7b1667a21a9a", "title": "Dirt", "description": "Et ea officia occaecat minim adipisicing. Ut nostrud sunt mollit ex labore. Exercitation ut exercitation sint reprehenderit duis reprehenderit.\r\n", "price": "Free" } ]
    return render_template("index.html", ads=ads, posts=posts)
    


# @app.route('/ad/add', methods=['GET'])
# def add_ad_view():
#     return render_template("new_ad.html")


# @app.route('/ad/edit/<id>', methods=['GET'])
# def edit_ad_view(id):
#     response = requests.get(settings.API_URL + '/getAdvertisement?id=' + id)
#     ad = response.json()
#     return render_template("edit_ad.html", ad=ad)


# @app.route('/ad/delete/<id>', methods=['GET'])
# def delete_ad_view(id):
#     response = requests.get(settings.API_URL + '/getAdvertisement?id=' + id)
#     ad = response.json()
#     return render_template("delete_ad.html", ad=ad)

# @app.route('/ad/view/<id>', methods=['GET'])
# def view_ad_view(id):
#     response = requests.get(settings.API_URL + '/getAdvertisement?id=' + id)
#     ad = response.json()
#     return render_template("view_ad.html", ad=ad)

# @app.route('/ad/new', methods=['POST'])
# def add_ad_request():
#     # Get item from the POST body
#     req_data = {
#         'title': request.form['title'],
#         'city': request.form['city'],
#         'description': request.form['description'],
#         'email': request.form['email'],
#         'imgUrl': request.form['imgUrl'],
#         'price': request.form['price']
#     }
#     response = requests.post(settings.API_URL + '/createAdvertisement', json=json.dumps(req_data))
#     return redirect(url_for('home'))

# @app.route('/ad/update/<id>', methods=['POST'])
# def update_ad_request(id):
#     # Get item from the POST body
#     req_data = {
#         'title': request.form['title'],
#         'city': request.form['city'],
#         'description': request.form['description'],
#         'email': request.form['email'],
#         'imgUrl': request.form['imgUrl'],
#         'price': request.form['price']
#     }
#     response = requests.put(settings.API_URL + '/updateAdvertisement?id=' + id, json=json.dumps(req_data))
#     return redirect(url_for('home'))

# @app.route('/ad/delete/<id>', methods=['POST'])
# def delete_ad_request(id):
#     response = requests.delete(settings.API_URL + '/deleteAdvertisement?id=' + id)
#     if response.status_code == 200:
#         return redirect(url_for('home'))

# running app
def main():
    print(' ----->>>> Flask Python Application running in development server')
    app.run(host=settings.SERVER_HOST, port=settings.SERVER_PORT, debug=settings.FLASK_DEBUG)


if __name__ == '__main__':
    main()
