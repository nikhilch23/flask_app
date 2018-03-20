from flask import Flask, render_template

app= Flask('__main__')

@app.route('/')
def fun():
   return render_template('file.html')

app.run(port=5001)

