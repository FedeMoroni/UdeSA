import numpy as np

def f(x):
    return np.log(x-1) + np.cos(x - 1)

def f_prime(x):
    return 1/(x-1) - np.sin(x - 1)

def newton_raphson(p1, tol=10**-5, max_iter=1000):
    p = p1
    for i in range(max_iter):
        f_p = f(p)
        f_prime_p = f_prime(p)
        
        if f_prime_p == 0:  # Evitar división por cero
            print("Derivada es cero. No se puede continuar.")
            return None
        
        p_next = p - f_p / f_prime_p

        if abs(p_next - p) < tol:
            print(f"Convergencia alcanzada en {i+1} iteraciones.")
            return p_next
        p = p_next
    print("Número máximo de iteraciones alcanzado sin convergencia.")
    return p 


p1 = 1.5
raiz = newton_raphson(p1)
print(f"La raíz aproximada es: {raiz}") 