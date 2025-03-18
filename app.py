#intial comment
from flask import Flask
import os
from datetime import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop_info():
    full_name = "Divya Nandini"
    username = os.getenv("USER") or os.getenv("USERNAME") or "unknown"
    ist_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')

    # Get top command output (first few lines)
    top_output = subprocess.getoutput("top -b -n 1 | head -5")

    return f"""
    <pre>
    Name: {full_name}
    Username: {username}
    Server Time (IST): {ist_time}
    
    Top Command Output:
    {top_output}
    </pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


