from flask import Flask


app = Flask(__name__, instance_relative_config=False)

from Controller.nav import main
app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)
