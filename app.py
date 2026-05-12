from flask import Flask, render_template, request, jsonify
from solver.newton import parse_function, build_functions, newton_method

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/solve", methods=["POST"])
def solve():
    data = request.json

    formula = data["formula"]
    x0 = float(data["x0"])
    tol = float(data["tol"])
    max_iter = int(data["max_iter"])

    try:
        expr, x = parse_function(formula)
        f, df, df_expr = build_functions(expr, x)
        root, iterations = newton_method(f, df, x0, tol, max_iter)

        return jsonify({
            "status": "success",
            "root": root,
            "iterations": iterations
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
