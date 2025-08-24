from flask import Flask, request, render_template_string

app = Flask(__name__)

messages = []  # store messages in memory

HTML = """
<h1>📋 Public Board</h1>
<form method="POST">
  Name: <input name="name"><br>
  Message: <input name="msg"><br>
  <button type="submit">Send</button>
</form>

<!-- Refresh button just reloads the page -->
<form method="GET">
  <button type="submit">🔄 Refresh</button>
</form>

<hr>
{% for m in messages %}
  <p><b>{{m[0]}}</b>: {{m[1]}}</p>
{% endfor %}
"""

@app.route("/", methods=["GET", "POST"])
def board():
    if request.method == "POST":
        name = request.form.get("name", "Anon")
        msg = request.form.get("msg", "")
        if msg:
            messages.append((name, msg))
    return render_template_string(HTML, messages=messages)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
