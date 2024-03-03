from flask import Flask, request, jsonify
from service import BlogService  # Adjusted import to reflect the new BlogService
from models import Schema
import json

app = Flask(__name__)

@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = "*"
    response.headers['Access-Control-Allow-Headers'] =  "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods'] =  "POST, GET, PUT, DELETE, OPTIONS"
    return response

@app.route("/")
def hello():
    return "Hello and Welcome to the Blog!"

# Blog posts endpoints
@app.route("/posts", methods=["GET"])
def list_posts():
    posts = BlogService().list_posts()
    # Convert the Row objects to dictionaries
    posts_list = [dict(post) for post in posts]
    return jsonify(posts_list)

@app.route("/posts", methods=["POST"])
def create_post():
    data = request.get_json()
    title = data['title']
    content = data['content']
    return jsonify(BlogService().create_post(title, content))    

@app.route("/posts/<int:post_id>", methods=["PUT"])
def update_post(post_id):
    # Assuming BlogService has a method to update a post
    return jsonify(BlogService().update_post(post_id, request.get_json()))

@app.route("/posts/<int:post_id>", methods=["DELETE"])
def delete_post(post_id):
    # Assuming BlogService has a method to delete a post
    return jsonify(BlogService().delete_post(post_id))

@app.route("/posts/<int:post_id>/comments", methods=["GET"])
def list_comments_for_post(post_id):
    comments = BlogService().list_comments(post_id)
    # Convert the Row objects to dictionaries
    comments_list = [dict(comment) for comment in comments]
    return jsonify(comments_list)

@app.route("/posts/<int:post_id>/comments", methods=["POST"])
def add_comment_to_post(post_id):
    # Assuming BlogService has a method to add a comment to a post
    data = request.get_json()
    data["post_id"] = post_id  # Ensure the comment is associated with the right post
    return jsonify(BlogService().add_comment(data))

if __name__ == "__main__":
    Schema()  # Initialize the database schema
    app.run(debug=True, host='127.0.0.1', port=5000)

