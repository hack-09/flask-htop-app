
# 🖥️ Flask `/htop` System Monitor 🚀  
[![Flask](https://img.shields.io/badge/Flask-2.0+-blue)](https://flask.palletsprojects.com/)  
[![Python](https://img.shields.io/badge/Python-3.8+-brightgreen)](https://www.python.org/)  
[![GitHub](https://img.shields.io/badge/GitHub-Repository-darkblue)](https://github.com/YOUR-USERNAME/flask-htop-app)

A simple Flask application that provides system information using an `/htop` endpoint.

---

## 📌 Features  
- **Displays Your Name** 🏷️  
- **Shows System Username** 👤  
- **Displays Server Time (IST)** ⏳  
- **Fetches & Shows `top` Command Output** 📊  
- **Hosted on GitHub Codespaces with Public Access** 🌍  

---

## 🎯 **Live Demo**
🔗 **Hosted URL:** [Click Here](https://flask-htop-app.onrender.com/htop)  

---

## 🚀 **Project Setup**

### 🔧 Prerequisites  
Ensure you have **Python 3.8+** installed.  

### 🛠️ Installation Steps
1. **Clone the Repository**  
   ```sh
   git clone https://github.com/hack-09/flask-htop-app.git
   cd flask-htop-app
   ```

2. **Create a Virtual Environment (Optional but Recommended)**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```

3. **Install Dependencies**
   ```sh
   pip install flask
   ```

4. **Run the Flask App**
   ```sh
   python app.py
   ```

5. **Access the App in Browser**
   ```
   http://127.0.0.1:5000/htop
   ```

---

## 📂 Project Structure
```
/flask-htop-app
│── app.py         # Main Flask application
│── README.md      # Project documentation
```

---

## 🖥️ API Endpoint Details
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/htop`  | GET    | Returns system details including username, time (IST), and `top` command output |

---

## 📸 Sample Output
**Example Web Page Rendered by `/htop` Endpoint:**

![image](https://github.com/user-attachments/assets/bcbd3f9a-49c4-46a8-bd56-5031ea807a78)

```yaml
Name: Priyanshu Kumar
Username: codespace
Server Time (IST): 2025-02-22 08:14:18 IST
top - 08:14:18 up  1:00,  0 users,  load average: 0.15, 0.25, 0.22
Tasks:  25 total,   1 running,  24 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
MiB Mem :   7929.6 total,    310.4 free,   1927.2 used,   5691.9 buff/cache
MiB Swap:      0.0 total,      0.0 free,      0.0 used.   5622.8 avail Mem 

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
      1 codespa+  20   0    1136    128    128 S   0.0   0.0   0:00.09 docker-+
      7 codespa+  20   0    2616   1408   1408 S   0.0   0.0   0:00.74 sh
    153 root      20   0   12196   3480   2560 S   0.0   0.0   0:00.00 sshd


```

---

## 📢 Deployment
This application is deployed using GitHub Codespaces with a public port for external access.

**Steps to Keep It Running:**
1. Start the Codespace
2. Set Port to Public in GitHub Codespaces
3. Run `python app.py`
4. Use the Public Link for Testing

---

## 🤝 Contributing
Want to improve this project? Feel free to contribute!

1. **Fork the Repository**
2. **Create a Feature Branch**
3. **Make Your Changes**
4. **Submit a Pull Request**

---

## 📝 Author
👤 **Priyanshu Kumar**  
📧 **priyanshukumar9780@gmail.com.com**  
🌍 **GitHub**

---

## 🏆 Show Some Love
If you like this project, give it a ⭐ on GitHub!

