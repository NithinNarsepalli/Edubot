from flask import Flask  #importing flask

app = Flask(__name__) 

@app.route('/') #route1 with the welcome message
def Home():
	return {
 "message": "Welcome to the IELTS Speaking Test Platform!"
}

@app.route('/info')  #route2 with the specified details
def information():
	return{
		"platform_name": "IELTS Speaking Test Platform",
 "version": "1.0",
 "developer_contact": "support@example.com"
}

if __name__ == '__main__':
	app.run(debug=True)