from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Return HTML content with large text
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hello World</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #282c34;
                font-family: Arial, sans-serif;
                color: white;
                text-align: center;
            }
            h1 {
                font-size: 4rem;
                margin: 0;
            }
            p {
                font-size: 1.5rem;
                margin-top: 1rem;
            }
        </style>
    </head>
    <body>
        <div>
            <h1>Hello!! ATS Company</h1>
            <p>Welcome to 2025 🎉</p>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
