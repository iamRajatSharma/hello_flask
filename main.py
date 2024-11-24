from flask import Flask, request
app = Flask(__name__)

@app.route("/test", methods=["POST"])
def hello():
    print(request.query_string)
    return "I am post method"


if __name__=="__main__":
    app.run(debug=True)    

    
