from flask import jsonify, request
from flask.views import MethodView
from .models import User, Post, db

# User Views (Class-Based)
class UserAPI(MethodView):
    def get(self):
        users = User.query.all()
        users_list = [{"id": user.id, "username": user.username, "email": user.email} for user in users]
        return jsonify(users_list), 200

    def post(self):
        data = request.get_json()
        new_user = User(username=data['username'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created"}), 201

# Post Views (Class-Based)
class PostAPI(MethodView):
    def get(self):
        posts = Post.query.all()
        posts_list = [{"id": post.id, "title": post.title, "content": post.content, "user_id": post.user_id} for post in posts]
        return jsonify(posts_list), 200

    def post(self):
        data = request.get_json()
        new_post = Post(title=data['title'], content=data['content'], user_id=data['user_id'])
        db.session.add(new_post)
        db.session.commit()
        return jsonify({"message": "Post created"}), 201
