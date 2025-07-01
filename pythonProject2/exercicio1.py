def grau_celsius_para_fahrenhit(celsius):
    f = (9 * celsius) / 5 + 32
    return f


celsius = float(input("digite uma temperatura em graus celsius"))
fahrenhit = grau_celsius_para_fahrenhit(celsius)

print(fahrenhit,"aqui esta a converção para fahrenhit")