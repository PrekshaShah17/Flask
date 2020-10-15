from flask import Flask, render_template, request
from forms import SignUpForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'itsasecret'


@app.route('/')
def home():
    return 'Hello World'


@app.route('/about')
def about():
    return 'The About Page'


@app.route('/blog')
def blog():
    posts = [{'title': 'Technology in 2020', 'author': 'Preksha'},
             {'title': 'Technology in 2050', 'author': 'Preksha'}]
    return render_template('blog.html', author="Preksha", sunny=False, posts=posts)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        return render_template('user.html', result=result)
    return render_template('signup.html', form=form)


@app.route('/blog/<string:blog_id>')
def blogpost(blog_id):
    return 'This is blog post number ' + blog_id


if __name__ == '__main__':
    app.run()
