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

        id = max(post['id'] for post in blogposts) + 1
        new_post = {'id': id, 'author':author, 'title': title, 'content': content}
        blogposts.append(new_post)

        with open('data_structure.json', 'w') as all_data:
            json.dump(blogposts, all_data)

        return redirect(url_for('index'))

    else:
        return render_template('add.html', title='new post')


@app.route('/delete/<int:post_id>')
def delete(post_id):
    with open('data_structure.json', 'r') as all_data:
        blogposts = json.load(all_data)

    for index, post in enumerate(blogposts):
        if post['id'] == post_id:
            del blogposts[index]

    with open('data_structure.json', 'w') as all_data:
        json.dump(blogposts, all_data)

    return render_template('delete.html', post_id=post_id)

@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    if request.method == 'POST':
        new_author= request.form.get('author')
        new_title = request.form.get('title')
        new_content = request.form.get('content')
        with open('data_structure.json', 'r') as all_data:
            blogposts = json.load(all_data)

        for post in blogposts:
            if post['id'] == post_id:
                post['title'] = new_title
                post['content'] = new_content
                post['author'] = new_author

        with open('data_structure.json', 'w') as all_data:
            json.dump(blogposts, all_data)

        return redirect(url_for('index'))

    with open('data_structure.json', 'r') as all_data:
        blogposts = json.load(all_data)
    for post in blogposts:
        if post['id'] == post_id:
            orig_title = post['title']
            orig_author = post['author']
            orig_content = post['content']

    return render_template('update.html', title='update post', post_id=post_id, orig_title=orig_title, orig_author=orig_author, orig_content=orig_content)




if __name__ == "__main__":
    app.run(debug=True)
