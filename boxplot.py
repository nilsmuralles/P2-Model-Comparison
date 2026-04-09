import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

df = pd.read_csv("data/raw/Datos.csv")
df = df.drop(columns=["Sample code number", "Class"])

variables = df.columns.tolist()
labels = [
    "Clump\nThickness", "Cell\nSize", "Cell\nShape",
    "Marginal\nAdhesion", "Epithelial\nSize", "Bare\nNuclei",
    "Bland\nChromatin", "Normal\nNucleoli", "Mitoses"
]

fig, ax = plt.subplots(figsize=(13, 6))
fig.patch.set_facecolor("#FAFAFA")
ax.set_facecolor("#FAFAFA")

bp = ax.boxplot(
    [df[col].dropna() for col in variables],
    patch_artist=True,
    notch=False,
    vert=True,
    widths=0.55,
    flierprops=dict(marker='o', color='#D85A30', markerfacecolor='#D85A30',
                    markersize=4, linestyle='none', alpha=0.7),
    medianprops=dict(color='#3C3489', linewidth=2),
    boxprops=dict(facecolor='#CECBF6', color='#534AB7', linewidth=1.2),
    whiskerprops=dict(color='#534AB7', linewidth=1.2, linestyle='--'),
    capprops=dict(color='#534AB7', linewidth=1.5),
)

ax.set_xticks(range(1, len(labels) + 1))
ax.set_xticklabels(labels, fontsize=10, color='#444')
ax.set_yticks(range(1, 11))
ax.set_ylabel("Valor (escala ordinal 1–10)", fontsize=11, color='#555')
ax.set_ylim(0.5, 10.8)
ax.yaxis.grid(True, linestyle='--', alpha=0.5, color='#ccc')
ax.set_axisbelow(True)
for spine in ax.spines.values():
    spine.set_visible(False)

outlier_patch = mpatches.Patch(color='#D85A30', label='Valores atípicos (IQR)')
median_line = mpatches.Patch(color='#3C3489', label='Mediana')
ax.legend(handles=[outlier_patch, median_line], fontsize=10,
          loc='upper right', framealpha=0.7)

ax.set_title("Diagrama de caja y bigotes — Wisconsin Breast Cancer Dataset",
             fontsize=13, fontweight='bold', color='#2C2C2A', pad=14)

plt.tight_layout()
plt.savefig("boxplot_wisconsin.png", dpi=180,
            bbox_inches='tight', facecolor=fig.get_facecolor())
print("Guardado correctamente.")