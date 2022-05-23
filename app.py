from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import operator

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def index():
    region = request.args.get('region') if request.args.get('region') else "" # 取得地區 GET 參數
    region = '' if region == '不限地區' else region
    keyword = request.args.get('keyword') if request.args.get('keyword') else "" # 取得關鍵字 GET 參數

    with open("data.json", encoding='utf-8') as json_file:
        data = json.load(json_file)
    
    if ((region == '') and (keyword == '')): # 地區為空，關鍵字為空
    
        return jsonify(data)
    elif (keyword == ''): # 地區有值，關鍵字為空
        newData = []
        for i in data:
            if (i['region'] == region):
                newData.append(i)
        
        return jsonify(newData)
    elif (region and keyword): # 地區有值，關鍵字有值
        newData = []
        for i in data:
            if (region == i['region'] and keyword in i['name']):
                newData.append(i)
        
        return jsonify(newData)
    else: # 地區為空，關鍵字有值
        newData = []
        for i in data:
            if (keyword in i['name']):
                newData.append(i)
        
        return jsonify(newData)

@app.route("/hot", methods=['GET'])
def hot():
    with open("data.json", encoding='utf-8') as json_file:
        data = json.load(json_file)
    data.sort(key=operator.itemgetter('rank'), reverse=True) # 依照星等由高至低排序
    
    return jsonify(data)

if __name__ == '__main__':
    app.debug = True
    app.run()





