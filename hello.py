from flask import Flask
from flask import jsonify
app = Flask(__name__)
empDB=[
 	{
 		'id':'101',
 		'name':'Test1',
 		'title':'Title1'
 	},
 	{
 		'id':'201',
 		'name':'Test2',
 		'title':'Title2'
 	}
 ]
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/empdb/employee',methods=['GET'])
def getAllEmp():
    return jsonify({'emps':empDB})


@app.route('/empdb/employee/<empId>',methods=['GET'])
def getEmp(empId):
    usr = [ emp for emp in empDB if (emp['id'] == empId) ] 
    return jsonify({'emp':usr})
    
@app.route('/empdb/employee/<empId>',methods=['PUT'])
def updateEmp(empId): 
    em = [ emp for emp in empDB if (emp['id'] == empId) ] 
    if 'name' in request.json : 
        em[0]['name'] = request.json['name'] 
    if 'title' in request.json:
        em[0]['title'] = request.json['title'] 
 return jsonify({'emp':em[0]})