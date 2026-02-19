import numpy as np
import matplotlib.pyplot as plt
from datetime import date, timedelta

def equation_of_time(day_of_year):
    """Equação do tempo em minutos (aproximação de Spencer)"""
    B = 2 * np.pi * (day_of_year - 1) / 365
    eot = 229.18 * (0.000075
                    + 0.001868 * np.cos(B)
                    - 0.032077 * np.sin(B)
                    - 0.014615 * np.cos(2*B)
                    - 0.04089  * np.sin(2*B))
    return eot  # em minutos

def solar_declination(day_of_year):
    """Declinação solar em graus"""
    B = 2 * np.pi * (day_of_year - 1) / 365
    dec = (180/np.pi) * (0.006918
                         - 0.399912 * np.cos(B)
                         + 0.070257 * np.sin(B)
                         - 0.006758 * np.cos(2*B)
                         + 0.000907 * np.sin(2*B)
                         - 0.002697 * np.cos(3*B)
                         + 0.00148  * np.sin(3*B))
    return dec

# Gerar dados para cada dia do ano
dias = np.arange(1, 366)
eot = equation_of_time(dias)      # minutos (desvio em X)
dec = solar_declination(dias)      # graus (posição em Y)

# Datas para rotular pontos especiais
meses = {
    "Jan 1": 1, "Fev": 32, "Mar": 60, "Abr": 91,
    "Mai": 121, "Jun": 152, "Jul": 182, "Ago": 213,
    "Set": 244, "Out": 274, "Nov": 305, "Dez": 335
}

# --- Plot ---
fig, ax = plt.subplots(figsize=(7, 9))

# Colorir por mês
scatter = ax.scatter(eot, dec, c=dias, cmap='hsv', s=8, zorder=3)
ax.plot(eot, dec, color='gray', linewidth=0.8, alpha=0.5)

# Marcadores de meses
for nome, dia in meses.items():
    x, y = equation_of_time(dia), solar_declination(dia)
    ax.plot(x, y, 'ko', ms=5, zorder=4)
    ax.annotate(nome, (x, y), textcoords="offset points",
                xytext=(6, 3), fontsize=8)

# Linhas de referência
ax.axhline(0, color='orange', lw=0.8, linestyle='--', label='Equinócio (dec=0)')
ax.axvline(0, color='blue',   lw=0.8, linestyle='--', label='EoT = 0')

ax.set_xlabel("Equação do Tempo (minutos)\n← Sol adiantado | Sol atrasado →", fontsize=11)
ax.set_ylabel("Declinação Solar (graus)", fontsize=11)
ax.set_title("Analema Solar", fontsize=15, fontweight='bold')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
plt.colorbar(scatter, ax=ax, label='Dia do ano')
plt.tight_layout()
plt.show()
