from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        print(f"Captured credentials: {username}, {password}")  # Just simulating data capture

    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Fake Login Portal</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; padding: 50px; }
            .login-box { border: 1px solid #ccc; padding: 20px; width: 300px; margin: auto; }
        </style>
    </head>
    <body>
        <h2>Fake Login Portal</h2>
        <div class="login-box">
            <form method="POST">
                <input type="text" name="username" placeholder="Username" required><br><br>
                <input type="password" name="password" placeholder="Password" required><br><br>
                <button type="submit">Login</button>
            </form>
        </div>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run()
