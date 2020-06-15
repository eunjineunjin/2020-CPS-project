from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
	#return "Hello World!"
	#return "<html><body><h1>Hello World</h1></body></html>"
	return render_template('hello.html')

if __name__ == "__main__":
	app.run(debug= True)