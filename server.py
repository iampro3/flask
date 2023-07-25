from flask import Flask
import random

app = Flask(__name__)

topics = [
    {'id':1, 'title': 'html', 'body':'html is ...'},
    {'id':2, 'title': 'css', 'body':'css is ...'},
    {'id':3, 'title': 'javascript', 'body':'javascript is ...'}
]

def template(contents, content):
     return f'''
     <!doctype html>
    <html>
        <body>
            <h1><a href="/>WEB</a></h1>
            <ol>
                {contents}
            </ol>
                {contents}
                <ul>
                <li><a href="/create/">create</a></li>
                </ul>
        </body> 
    </html>
    '''

def getContents():
    liTags =''
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">(topic["title"])</a></li>'        
        return liTags
    
@app.route('/')
def index():
    
    return template(getContents(), '<h1>welcome</h2>Hello, Web')
    # return 'random: <strong>'+str(random.random())+'</strong>'
    # return '''<!doctype html>
    # <html>
    #     <body>
    #         <h1><a href="/>WEB</a></h1>
    #         <ol>
    #             {liTags}
    #         </ol>
    #         <h2>Welcome</h2>
    #         Hello, Web
    #     </body> 
    # </html>
    # '''


@app.route('/read/<ind:id>/')
def read(id):
    # print(id)
    title=''
    body=''
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            body=topic['body']
            break
    return template(getContents(), f'<h2>{title}</h2>{body}')
    # return 'Read '+id

@app.route('/create/')
def create():
    content ='''
    <p><input type="text" name = "title" placeholder="title"></p>
    <p><textarea name="body" placeholder="body"></textarea></p>
'''
    return template(getContents(), content)

app.run(debug=True)