#!/usr/bin/env python3
from flask import Flask, render_template
from tinydb import TinyDB
from pathlib import Path
import time

# Initialize Flask app
app = Flask(__name__, template_folder='templates')

# Connect to database (profiles.json)
DB_PATH = Path(__file__).resolve().parent.parent / "profiles.json"
DB = TinyDB(DB_PATH)

@app.route('/')
def index():
    # Load all classified records
    records = DB.all()
    records = sorted(records, key=lambda x: x.get('time', ''), reverse=True)
    for r in records:
        if 'time' in r:
            r['time_fmt'] = r['time']
        else:
            r['time_fmt'] = time.strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', items=records)

if __name__ == "__main__":
    print("🚀 Launching Blacklatch AI Threat Profiler Dashboard...")
    app.run(host="0.0.0.0", port=8090, debug=True)
