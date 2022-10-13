from operator import imod
from flask import Flask, render_template , request
import json 
import urllib.request


app = Flask('__name__')


 

@app.route('/')
def index():
    source = urllib.request.urlopen("https://api.github.com/search/repositories?q=created:>2021-08-13&sort=stars&order=desc").read()
    list_of_data = json.loads(source)

    return render_template('index.html',list_of_data=list_of_data)
    
if __name__ == '__main__':
    app.run()