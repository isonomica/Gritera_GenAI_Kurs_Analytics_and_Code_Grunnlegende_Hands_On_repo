import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

W, H = 24, 14
fig, ax = plt.subplots(figsize=(W, H))
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.axis('off')
fig.patch.set_facecolor('#F0F2F5')

BLUE   = '#3A7BD5'
GREEN  = '#27AE60'
ORANGE = '#E67E22'
GRAY   = '#7F8C8D'
RED    = '#C0392B'
TEAL   = '#16A085'
PURPLE = '#8E44AD'
DARK   = '#2C3E50'
LGRAY  = '#BDC3C7'

def box(ax, x, y, w, h, label, sublabel='', color=BLUE, text_color='white', fs=10):
    r = mpatches.FancyBboxPatch((x - w/2, y - h/2), w, h,
        boxstyle="round,pad=0.1", facecolor=color,
        edgecolor='white', linewidth=2, zorder=3)
    ax.add_patch(r)
    dy = 0.12 if sublabel else 0
    ax.text(x, y + dy, label, ha='center', va='center',
            fontsize=fs, color=text_color, fontweight='bold', zorder=4)
    if sublabel:
        ax.text(x, y - 0.18, sublabel, ha='center', va='center',
                fontsize=8, color=text_color, alpha=0.9, zorder=4)

def arr(ax, x1, y1, x2, y2):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color='#555', lw=1.4), zorder=2)

# ── LAG 0: rot ────────────────────────────────────────────────────────────────
box(ax, 12, 13.2, 3.8, 0.7, 'kurs-dataplattform', 'dbt + DuckDB', color=DARK, fs=13)

# ── LAG 1: hovednoder ─────────────────────────────────────────────────────────
#   seeds x=2.5   models x=12   konfig x=21.5
box(ax,  2.5, 11.5, 2.6, 0.6, 'seeds/',   'rawdata (CSV)',          color=ORANGE, fs=11)
box(ax, 12.0, 11.5, 6.0, 0.6, 'models/',  'SQL-transformasjoner',   color=BLUE,   fs=11)
box(ax, 21.5, 11.5, 2.6, 0.6, 'konfig',   'yml / toml',             color=GRAY,   fs=11)
for x in [2.5, 12.0, 21.5]:
    arr(ax, 12, 12.85, x, 11.8)

# ── LAG 2: seeds ──────────────────────────────────────────────────────────────
seeds = [
    ('raw_customers.csv',    '15 kunder',           GREEN),
    ('raw_products.csv',     '12 produkter',         GREEN),
    ('raw_orders.csv',       '20 ordrer',            GREEN),
    ('raw_order_items.csv',  '42 ordrelinjer',       GREEN),
    ('raw_complaints.csv',   '11 klager',            GREEN),
    ('northwind/',           '11 CSV (deaktivert)',  GRAY),
]
for i, (name, sub, c) in enumerate(seeds):
    y = 10.4 - i * 1.0
    box(ax, 2.5, y, 2.6, 0.65, name, sub, color=c, fs=9)
    arr(ax, 2.5, 11.2, 2.5, y + 0.33)

# ── LAG 2: konfig ─────────────────────────────────────────────────────────────
cfgs = ['dbt_project.yml', 'profiles.yml', 'pyproject.toml', 'README.md']
for i, name in enumerate(cfgs):
    y = 10.4 - i * 1.0
    box(ax, 21.5, y, 2.6, 0.65, name, color=LGRAY, text_color=DARK, fs=9)
    arr(ax, 21.5, 11.2, 21.5, y + 0.33)

# ── LAG 2: models-undermapper ─────────────────────────────────────────────────
#   staging x=6.5   exercises x=9.5   intermediate x=12.5   marts x=15.5   sources x=18.5
sub = [
    ( 6.5, 'staging/',      '3 modeller (klar)', TEAL),
    ( 9.5, 'exercises/',    'kursovelse',         RED),
    (12.5, 'intermediate/', 'tom',                GRAY),
    (15.5, 'marts/',        'tom',                GRAY),
    (18.5, 'sources.yml',   'kildedefinisjon',    PURPLE),
]
for x, lbl, sl, c in sub:
    box(ax, x, 10.2, 2.6, 0.65, lbl, sl, color=c, fs=10)
    arr(ax, 12.0, 11.2, x, 10.52)

# ── LAG 3: staging-modeller ───────────────────────────────────────────────────
stg = [
    ('stg_customers', '.sql + .yml'),
    ('stg_orders',    '.sql + .yml'),
    ('stg_products',  '.sql + .yml  (ny)'),
]
for i, (name, sl) in enumerate(stg):
    y = 8.9 - i * 1.0
    box(ax, 6.5, y, 2.6, 0.65, name, sl, color=TEAL, fs=9)
    arr(ax, 6.5, 9.87, 6.5, y + 0.33)

# ── LAG 3: exercises ──────────────────────────────────────────────────────────
box(ax, 9.5, 8.9, 2.6, 0.65, 'buggy_model.sql', '3 bevisste feil', color=RED, fs=9)
arr(ax, 9.5, 9.87, 9.5, 9.23)

plt.tight_layout(pad=0.3)
plt.savefig('docs/repo_oversikt.png', dpi=150, bbox_inches='tight', facecolor='#F0F2F5')
print("Lagret: docs/repo_oversikt.png")
