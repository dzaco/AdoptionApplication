from flask import Blueprint , render_template, request
main = Blueprint('main' , __name__)



@main.route('/')
def index():
    return render_template('index.html')

@main.route('/adopt', methods = ['POST'])
def adopt():
    data = request.form
    print(data)
    return render_template('adopt.html', data=data)

@main.route('/test')
def test():
    return render_template('test.html')