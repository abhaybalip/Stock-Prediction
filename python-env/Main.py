
from flask import *;

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('Index.html')

if(__name__=='__main__'):
    app.run(host='localhost',port=1000)
    