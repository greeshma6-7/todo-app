from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    date = request.args.get("date", "No date provided")
    return f"""
    Hi Waseem<br>
    Hi Greeshma<br>
    Hi Davana<br><br>
    Today's date: {date}
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
