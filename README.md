📋 Public Message Board

A simple Flask-based web app where multiple users can post and read messages on a shared board.
Built as a beginner-friendly project to understand how web servers handle requests and responses.

----

🚀 Features

Post a message with your name.

View all messages from everyone in one place.

Refresh button to see the latest messages.

Works on any device connected to the same network.

Can be shared across the internet using tools like ngrok.

----

⚙️ Requirements

Python 3.x

Flask
---
Install Flask with:
pip install flask

----
📂 Project Structure

public-message-board/

│── app.py              # Main Flask app

│── requirements.txt    # List of dependencies

│── README.md           # Project description

----

▶️ How to Run

Clone this repository:

git clone https://github.com/<your-username>/public-message-board.git

cd public-message-board

---

Install dependencies:

pip install -r requirements.txt

---

Run the Flask server:

python app.py

---

Open in browser:

http://127.0.0.1:5000

---

(Optional) To access from another device on the same Wi-Fi:

Find your IP:

ipconfig    # Windows

ifconfig    # Linux/Mac

---

Open in browser:

http://<your-IP>:5000

---

(Optional) To share across the internet:

ngrok http 5000

---

🛡️ Future Improvements

Auto-refresh messages every few seconds.

Store messages in a database (SQLite).

Add user authentication.

Improve UI with Bootstrap.


















