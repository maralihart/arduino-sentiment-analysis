from flask import Flask, render_template, request, redirect

app = Flask(__name__)
    
@app.route("/", methods=['GET', 'POST'])
def index():
  if request.method == "POST":
    req = request.form
    return redirect(request.url)

  return render_template('index.html')