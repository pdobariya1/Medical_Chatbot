from flask import Flask, render_template, request

from src.QAgenerator import rag_qa_chain


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("chat.html")


@app.route("/get", methods=["GET", "POST"])
def chat():
    message = request.form["msg"]
    query = message
    print(query)
    response = rag_qa_chain.invoke({"input": query})
    print("Response :", response["answer"])
    return str(response["answer"])


if __name__ == "__main__":
    app.run(debug=True)