from flask import Flask, render_template #library to send html file

app = Flask(__name__) #new instance of flask class

@app.route("/") #route when part is empty - if route is empty, create index and send back
def index(): 
	return render_template("index.html")
if __name__ == "__main__": #condition: if part of main function
	app.run(debug=True) #runs flask

