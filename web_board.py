from flask import Flask, request, jsonify

app = Flask(__name__)
posts = []

@app.route('/post', methods=['POST'])
def create_post():
    post = request.json
    posts.append(post)
    return jsonify({"message": "Post created"})

@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

if __name__ == '__main__':
    app.run(debug=True)
