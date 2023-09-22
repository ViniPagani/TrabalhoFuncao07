def composta(f, g, x):
    return f(g(x))

f_input = input("Digite a função f(x) (use 'x' como variável): ")
g_input = input("Digite a função g(x) (use 'x' como variável): ")
x = float(input("Digite o valor de x: "))

def f(x):
    return eval(f_input)

def g(x):
    return eval(g_input)

resultado = composta(f, g, x)
print(f"O resultado de f(g({x})) é: {resultado}")
