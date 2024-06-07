import numpy as np
import matplotlib.pyplot as plt

# constantes
c = 3e8  # velocidade da luz em m/s
frequencia = 309e6  # Frequência em Hz
lambda_ = c / frequencia  # comprimento de onda em metros

# função para calcular o fator de arranjo
def fator_arranjo(N, d, delta, theta):
    k = 2 * np.pi / lambda_
    n = np.arange(N)
    fator = np.abs(np.sum(np.exp(1j * (n * delta + k * d * n * np.cos(theta[:, np.newaxis]))), axis=1))
    return fator / N  # Normalização

# ângulos de observação
theta = np.linspace(0, 2 * np.pi, 360)
# valores de d e delta
ds = [lambda_/8, lambda_/2, lambda_]
deltas = [0, np.pi/2, 2*np.pi/3, np.pi]

# diagramas de radiação para cada valor de N
for N in [3, 5, 10]:
    # diagramas de radiação
    fig, axs = plt.subplots(1, len(ds), figsize=(18, 6), subplot_kw={'projection': 'polar'})
    fig.suptitle(f'Diagrama de Radiação para N={N}', fontsize=16, ha='center')

    for j, d in enumerate(ds):
        for delta in deltas:
            fator = fator_arranjo(N, d, delta, theta)
            axs[j].plot(theta, fator)

        axs[j].set_title(f'd={d/lambda_:.2f}λ', loc='center')

    # p/ dicionar legenda na extremidade direita da figura
    axs[-1].legend([f'{delta:.2f}' for delta in deltas], title='δ (rad)', loc='center left', bbox_to_anchor=(1, 0.5))

    plt.tight_layout(rect=[0, 0, 0.9, 0.95])
    plt.show()

print(f'Frequência: {frequencia / 1e6:.2f} MHz')
