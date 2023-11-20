from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

# Parâmetros da distribuição normal (média e desvio padrão)
media = 170
desvio_padrao = 5

# Gere valores ao longo do eixo x
x = np.linspace(150 , 190 , 1000)

# Calcule a FDP para cada valor de x
pdf_values = norm.pdf(x, loc=media, scale=desvio_padrao)

# Plot da FDP
plt.plot(x, pdf_values, label='FDP da distribuição normal')
plt.title('Função de Densidade de Probabilidade (FDP) de uma Distribuição Normal Padrão')
plt.xlabel('Valores de x')
plt.ylabel('FDP(x)')
plt.legend()
plt.show()



from scipy.stats import norm

def calcula_probabilidade_acumulativa(x, media, desvio_padrao):
    # Calcula a probabilidade acumulativa para o valor x
    probabilidade_acumulativa = norm.cdf(x, loc=media, scale=desvio_padrao)
    return probabilidade_acumulativa

media = 170
desvio_padrao = 5
valor_x = 165

prob_acumulativa = 1 - calcula_probabilidade_acumulativa(valor_x, media, desvio_padrao)
print(f"A probabilidade para x={valor_x} é: {prob_acumulativa * 100:.2f}%")

quantidade_alunos = 10000
alunos_acima = quantidade_alunos * prob_acumulativa

print(f"A quantidade estimada de alunos acima de 165 cm é: {int(alunos_acima)}")



