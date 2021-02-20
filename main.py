from flask import Flask, render_template, request, redirect
from sentiment_analysis import analyze

app = Flask(__name__)
    
@app.route("/", methods=['GET', 'POST'])
def index():
  if request.method == "POST":
    req = request.form
    text = req.get('text')

    if text:
      analysis = analyze(text)
      return render_template('index.html', analysis=analysis, text=text)
      
    else:
      feedback = "Text to Analyze cannot be empty. Please fill it out."
      return render_template('index.html', feedback=feedback)

  return render_template('index.html')