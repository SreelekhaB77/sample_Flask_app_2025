from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <style>
                body {
                    background-color: #acf9b9;
                    color: black;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    font-family: Arial, sans-serif;
                    font-size: 2em;
                }
            </style>
        </head>
        <body>
            Welcome to my Flask App!
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
