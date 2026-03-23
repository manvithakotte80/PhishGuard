from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import re

app = Flask(__name__)

# In-memory history and stats
history = []
stats = {"Safe": 0, "Phishing": 0}

# Phishing detection function
def check_phishing(url):
    phishing_keywords = ["login", "verify", "bank", "secure", "update", "password"]
    for word in phishing_keywords:
        if re.search(word, url, re.IGNORECASE):
            return "Phishing"
    return "Safe"

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    url = ""
    if request.method == "POST":
        url = request.form.get("url")
        result = check_phishing(url)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Save to history
        history.append({"url": url, "result": result, "time": timestamp})
        stats[result] += 1
    return render_template("index.html", history=history, stats=stats, result=result, url=url)

# Route to clear history
@app.route("/clear")
def clear_history():
    history.clear()
    stats["Safe"] = 0
    stats["Phishing"] = 0
    return redirect(url_for("home"))

def main():
    app.run(debug=True, port=5000)

if __name__ == "__main__":
    main()