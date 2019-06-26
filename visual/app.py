# -*- coding: utf-8 -*- 
import json
from flask import Flask, request, render_template, Response,jsonify
app = Flask(__name__)
from result import sample




@app.route('/' ,methods = ['POST','GET'])
def input():

   if request.method == 'POST':
      keyword = request.form["get_name"]
      result = list(filter(lambda x: keyword in x['name'] , sample))
      # []
      print(result)
      return render_template("index.html", result = result)
   else:
      return render_template('index.html')

@app.route('/autocomplete/', methods=['POST','GET'])
def autocomplete():

   results = list(map(lambda x: x['name'], sample))
   # ["한신포차", "한신포차 (종로관철점)", "한신포차 (논현본점)", "경성포차", "백억포차"]
   return jsonify(matching_results=results)




if __name__ == '__main__':

    app.run(host='0.0.0.0')












    #
