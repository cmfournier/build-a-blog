from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:password@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(1600))

    def __init__(self, title, body):
        self.title = title
        self.body = body

@app.route('/blog', methods =['POST','GET'])
def index():
    if request.method == 'POST':
        title_name = request.form['blog_title']
        blog_post = request.form['blog_post']

        new_post = Blog(title_name, blog_post)
        db.session.add(new_post)
        db.session.commit()

    blog_posts = Blog.query.filter_by(id="4").all()
    return render_template('blog.html', title="Build A Blog", blog_posts=blog_posts)
        

if __name__ == '__main__':
    app.run()