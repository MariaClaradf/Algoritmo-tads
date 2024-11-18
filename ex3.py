# (Conversor de Temperatura) Receba uma temperatura em graus Celsius e converta para Fahrenheit usando a fórmula:
# F = C ∗ 1.8 + 32 (1)

print('Conversor de Temperatura!')

temp = float(input('Digite a temperatura que deseja em graus celsius: '))
fahrenheit = temp * 1.8 + 32

print(f'A temperatura {temp}°C é igual a {fahrenheit}°F')