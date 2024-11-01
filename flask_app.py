from flask import*
app=Flask(__name__)

@app.route('/')
def home():
    return "<Dit is huiswerk 11 flask> Hello world!<hopelijk krijg ik de tekst goed te zien>"

if __name__ =='__main__':
    app.run(port=5000,debug=True)