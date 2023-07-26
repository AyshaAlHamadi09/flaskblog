from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open('data_structure.json', 'r') as all_data:
        blogposts = json.load(all_data)
        return render_template('index.html', title='Flask Blog', blogposts=blogposts)


@app.route('/add', methods = ['GET', 'POST'])
def add():
    if request.method == 'POST':
        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')

        with open('data_structure.json', 'r') as all_data:
            blogposts = json.load(all_data)

        id = len(blogposts) + 1
        new_post = {'id': id, 'author':author, 'title': title, 'content': content}
        blogposts.append(new_post)

        with open('data_structure.json', 'w') as all_data:
            json.dump(blogposts, all_data)

        return redirect(url_for('index'))

    else:
        return render_template('add.html', title='new post')







if __name__ == "__main__":
    app.run(debug=True)
