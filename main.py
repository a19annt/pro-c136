from flask import Flask, request, jsonify
from data import data
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/')
def index():
    return jsonify({
        'data':data,
        'message':'succes'
    })

@app.route('/planet')
def planet():
    name = request.args.get('name')
    planet_data = next(item for item in data if item['name'] == name)
    return jsonify({
        'data':planet_data,
        'message':'succes'
    })
    

if(__name__ == '__main__'):
    app.run(debug = True)