from flask import Flask

app = Flask(__name__, instance_relative_config=False)

if __name__ == '__main__':
    app.run(debug=True)