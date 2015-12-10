from flask import Flask, render_template, Response
import config
import json
app = Flask(__name__)

@app.route("/")
def index():
	print(config.servers)
	return render_template("main.html", servers=config.servers)

@app.route("/stats/<servername>")
def server_stats(servername):
	stats = json.dumps([{'name': 'uptime', 'value': '2 days'}])
	return json_response(stats)

def json_response(response_val):
	return Response(response=response_val, status=200, mimetype="application/json")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000)  
