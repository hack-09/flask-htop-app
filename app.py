from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Priyanshu Kumar"  # your name
    username = os.getenv("USER") or os.getenv("USERNAME")  # Get system username
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")
    
    # Get system process details using the `top` command
    top_output = subprocess.getoutput("top -b -n 1 | head -10")  

    return f"""
    <h1>Name: {name}</h1>
    <h2>Username: {username}</h2>
    <h2>Server Time (IST): {server_time}</h2>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
