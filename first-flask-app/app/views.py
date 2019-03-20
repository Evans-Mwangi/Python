from flask import render_template, request, redirect, url_for

from app import app
 
blog = {'name': 'My awesome blog', 'posts' : {0:{'post_id':0, 'title': 'New Post pour moi', 'content':'Cest la poaste pour mon site', 'author': 'Evans Mwangi' }}
}
@app.route('/')
def home():
    return  render_template('home.jinja2', blog=blog)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = blog['posts'].get(post_id)
    if not post:
        return render_template('404.jinja2', message = f'A post with id {post_id} was not found')
    return render_template('post.jinja2', template_post=post)

@app.route('/post/create', methods = ['GET','POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        post_id =  len(blog['posts'])
        blog['posts'][post_id] = {'post_id':post_id, 'title': title, 'content': content}
        return redirect(url_for('post', post_id = post_id))
    return render_template('create.html')