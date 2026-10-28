from flask import Flask, render_template

app = Flask(__name__)

OPERATIONS = [
    {
        "name": "Load Dataset",
        "icon": "⬇",
        "desc": "Upload CSV, Excel, or JSON files for analysis.",
    },
    {
        "name": "Preview Data",
        "icon": "📊",
        "desc": "Inspect rows, columns, and sample records quickly.",
    },
    {
        "name": "Clean Data",
        "icon": "🧹",
        "desc": "Remove nulls, duplicates, and formatting issues.",
    },
    {
        "name": "Handle Missing",
        "icon": "🩹",
        "desc": "Fill or drop missing values using smart rules.",
    },
    {
        "name": "Detect Outliers",
        "icon": "⚠",
        "desc": "Highlight anomalies with statistical detection.",
    },
    {
        "name": "Encode Fields",
        "icon": "🔤",
        "desc": "Convert categories to machine-learning ready values.",
    },
    {
        "name": "Scale Features",
        "icon": "📏",
        "desc": "Normalize and standardize numerical variables.",
    },
    {
        "name": "Visualize Trends",
        "icon": "📈",
        "desc": "Generate charts for patterns and distributions.",
    },
    {
        "name": "Summary Report",
        "icon": "📝",
        "desc": "Build an overview with insights and recommendations.",
    },
    {
        "name": "Export Result",
        "icon": "🚀",
        "desc": "Download cleaned data or a final report package.",
    },
]


@app.route("/")
def index():
    return render_template("index.html", operations=OPERATIONS)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
