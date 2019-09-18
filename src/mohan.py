from flask import Flask ,request,redirect
from flask_cors import CORS, cross_origin
from flask import jsonify
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/hello',methods = ['GET'])
@cross_origin()
def hello_world():
    if request.method == 'GET':
        y="Hello World"
        return jsonify(y)
#      return redirect(url_for('success',name = user))
   

if __name__ == '__main__':
    app.run()
#    app.run()
