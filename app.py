from flask import Flask, render_template, request, jsonify, send_file
from scanner import run_scan
import pandas as pd
import io

app = Flask(__name__)

scan_history = []
last_results = []


@app.route("/")
def home():
    return render_template("index.html", history=scan_history)


@app.route("/scan", methods=["POST"])
def scan():
    global last_results

    data = request.get_json()
    url = data.get("url")

    results = run_scan(url)
    last_results = results

    high = medium = low = 0

    for r in results:
        if r["severity"] == "High":
            high += 1
        elif r["severity"] == "Medium":
            medium += 1
        else:
            low += 1

    scan_history.append({
        "url": url,
        "high": high,
        "medium": medium,
        "low": low
    })

    return jsonify({
        "results": results,
        "high": high,
        "medium": medium,
        "low": low
    })


@app.route("/export_csv")
def export_csv():
    global last_results

    if not last_results:
        return "No data available"

    df = pd.DataFrame(last_results)

    buffer = io.StringIO()
    df.to_csv(buffer, index=False)
    buffer.seek(0)

    return send_file(
        io.BytesIO(buffer.getvalue().encode()),
        mimetype="text/csv",
        as_attachment=True,
        download_name="scan_report.csv"
    )


if __name__ == "__main__":
    app.run(debug=True)
