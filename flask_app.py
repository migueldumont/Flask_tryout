from flask import*
app=Flask(__name__)

@app.route('/')
def home():
    return "<p> Hello, dit is huiswerk 11 over flask </p>"

if __name__ =='__main__':
    app.run(port=5000,debug=True)