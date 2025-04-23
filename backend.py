from flask import Flask, render_template, send_from_directory, jsonify
import os

app = Flask(__name__)
REPORT_DIR = '/Users/souravg/Documents/sample/reports/'

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/reports/<filename>')
def get_report(filename):
    return send_from_directory(REPORT_DIR, filename)

@app.route('/api/reports')
def list_reports():
    try:
        files = os.listdir(REPORT_DIR)
        html_files = [f for f in files if f.endswith('.html')]
        reports = [{
            "filename": f,
            "label": f.replace('-', ' ').replace('_', ' ').replace('.html', '').capitalize()
        } for f in html_files]
        return jsonify(reports)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
