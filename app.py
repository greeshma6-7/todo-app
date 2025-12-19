from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    manual_date = request.args.get("date", "No date provided")
    return f"""
    Hi Waseem<br>
    Hi Davana<br>
    Hi Greeshma<br><br>
    Today's date (manual): {manual_date}
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
