import sympy as sp
import numpy as np


def parse_function(formula):
    x = sp.Symbol('x')

    try:
        expr = sp.sympify(formula)
    except Exception:
        raise ValueError("فرمول قابل تشخیص نیست")

    return expr, x


def build_functions(expr, x):

    f = sp.lambdify(x, expr, "numpy")

    df_expr = sp.diff(expr, x)

    df = sp.lambdify(x, df_expr, "numpy")

    return f, df, df_expr


def newton_method(f, df, x0, tol, max_iter):

    iterations = []

    xn = x0

    for i in range(max_iter):

        fx = f(xn)
        dfx = df(xn)

        if abs(dfx) < 1e-12:
            raise ValueError("مشتق صفر شده است")

        xn1 = xn - fx/dfx

        error = abs(xn1 - xn)

        iterations.append({
            "iter": i+1,
            "x": float(xn),
            "f(x)": float(fx),
            "error": float(error)
        })

        if error < tol:
            return xn1, iterations

        xn = xn1

    return xn, iterations
