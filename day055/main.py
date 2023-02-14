from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>'\
           '<p>This is my paragraph</p>'\
           '<img src="https://media3.giphy.com/media/UIpzEC5QTvuOQ/giphy.gif?cid=ecf05e470zck4m0ge5nkax17klx8gs8g17grf3l8q7fztwcg&rid=giphy.gif&ct=g" width=200>'



def make_bold(function):
    def bold():
        new_text = "<h1>" + function() + "</h1>"
        return new_text
    return bold

def make_emphasis(function):
    def emphasis():
        return "<em>" + function() + "</em>"
    return emphasis

def make_underlined(function):
    def underline():
        return "<u>" + function() + "</u>"
    return underline
    
    
@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, you are {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)