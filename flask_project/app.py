# entry point
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

posts = {
    0 : { # The '0' here is postid, this is a unique identifier for each post
          'title': 'Hello World !',
          'content': 'This is my first blog post!'
    }
}

# defining url of our application
@app.route('/') # forward slash is here for our homepage, this decorator here will act on this function
# this is for route homepage
def home():
    return render_template('home.html', posts = posts)
    # this function here is going to run when the user visits this route

@app.route('/post/<int:post_id>') #/post/0
def post(post_id):
    post=posts.get(post_id)
    # return f"Post {post['title']}, content:\n\n{post['content']}."
    if not post:
        return render_template('404.html', message = f'A post with id {post_id} was not found.')
    return render_template('post.html', post = post)

@app.route('/post/form')
def form():
    return render_template('create.html')

# 127.0.0.1:5000/post/create?title=blablabla&content=something_else
@app.route('/post/create', methods = ['GET','POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title') # this helps form to send data as a hidden payload
        content = request.form.get('content')
        post_id = len(posts)
        posts[post_id] = {'id':post_id,'title':title, 'content':content}

        return redirect(url_for('post', post_id = post_id))
    return render_template('create.html')
    # url_for : takes a function name and returns a URL (an address that we want).
    # In this case, it takes post function name, that is defined up there and it is going to give us URL : '/post/<int:post_id>'
    # redirect is wrapping this url_for and what it does is it sends a response back to the browser telling the browser
    # that it should actually not load this page, it should go and load '/post/create' this page instead.


if __name__ == '__main__':
    app.run(debug=True) # this will starrt running our app
