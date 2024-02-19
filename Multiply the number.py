"""
8 kyu

A Jack le gusta mucho su número cinco: el truco aquí es que tienes que multiplicar cada número por 5 elevado al número de dígitos de cada número, así, por ejemplo:

multiply(3) == 15 # 3 * 5¹
multiply(10) == 250 # 10 * 5²
multiply(200) == 25000 # 200 * 5³
multiply(0) == 0 # 0 * 5¹
multiply(-3) == -15 # -3 * 5¹

"""

number = 200
print(number*pow(5,len(str(number))))

