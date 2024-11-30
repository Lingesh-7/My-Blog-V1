from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response=requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    datas=response.json()
    print(datas)
    return render_template("index.html",d=datas)

@app.route('/post/<int:bid>')
def post(bid):
    print(bid)
    response=requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    data=response.json()
    print(data)
    # if bid==data[0]['id']:
    #     print(data[0]['title'])
    #     print(data[0]['body'])
    return render_template("post.html",ds=data,b=bid)


if __name__ == "__main__":
    app.run(debug=True)
