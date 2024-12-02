from flask import Flask

# Maak een Flask-applicatie
app = Flask(__name__)

# Stel een route in
@app.route('/')
def home():
    return "Welkom op mijn website!"

if __name__ == '__main__':
    app.run(debug=True)