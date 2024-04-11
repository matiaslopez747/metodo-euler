import sympy as sp
import numpy as np

def metodo_euler(ecuacion_str,x0,y0,h,xf):
    x = sp.symbols('x')
    y = sp.symbols('y')
    ecuacion = sp.lambdify([x,y], sp.sympify(ecuacion_str), 'numpy')
    pasos=round((xf-x0)/h)
    yn=y0
    xn=x0
    for i in range(pasos+1):
        yn1=yn+h*ecuacion(xn,yn)
        print(f"para x={xn} y un valor de y={yn} el valor de yn+1={yn1}")
        xn=round(xn,1)+round(h,1)
        yn=yn1
        
#ejemplo de como ingresar el ejercicio 1
#metodo_euler("2*x*y",1,1,0.1,15)

#ejemplo de como ingresar el ejercicio 2
#metodo_euler("15-3*y",0,0,0.1,1)       

metodo_euler(input("ingrese la funcion en forma y'=f(x,y): "),float(input("ingrese el valor inicial de x: ")),float(input("ingrese el valor inicial de y: ")),float(input("ingrese el valor del incremento: ")),float(input("ingrese el hasta que valor quiere evaluar: ")))