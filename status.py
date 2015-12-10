from flask import Flask, render_template
import config
app = Flask(__name__)

@app.route("/")
def index():
	print(config.servers)
	return render_template("main.html", servers=config.servers)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000)  
