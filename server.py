from flask import Flask, request, jsonify
import util

def create_app():

 app = Flask(__name__)

 @app.route('/get_symptom_names', methods=['GET'])
 def get_symptom_names():
     response = jsonify({
         'symptom': util.get_data_columns()
     })
     response.headers.add('Access-Control-Allow-Origin', '*')

     return response

 @app.route('/get_diseases_names', methods=['GET'])
 def get_diseases_names():
     response = jsonify({
         'diseases': util.get_diseases_names()
     })
     response.headers.add('Access-Control-Allow-Origin', '*')

     return response

 @app.route('/predict_disease', methods = ['GET','POST'])
 def predict_disease():


     S1 = request.form['S1']
     S2 = request.form['S2']
     S3 = request.form['S3']
     S4 = request.form['S4']
     S5 = request.form['S5']
     S6 = request.form['S6']

     response = jsonify({
         'predict_disease': util.predict_disease(S1,S2,S3,S4,S5,S6)
     })
     response.headers.add('Access-Control-Allow-Origin', '*')

     return response

 @app.route('/description', methods = ['GET'])
 def description():
     response = jsonify({
         'Description of the disease': util.description()
     })
     response.headers.add('Access-Control-Allow-Origin', '*')

     return response

 @app.route('/precaution', methods = ['GET'])
 def precaution():
     response = jsonify({
         'Precaution of the disease': util.precaution()
     })
     response.headers.add('Access-Control-Allow-Origin', '*')

     return response
 return app
#if __name__ == "__main__":
#   util.load_saved_artifacts()
#   app.run()
