# Seuils stockage Aitif - V5.9
# Un seul endroit pour les seuils, pour ne pas les dupliquer.
# Si le marche ou le stockage change, on change seulement ici.
SEUILS = {
    "Riz": {"t_min": 15, "t_max": 25, "h_max": 80},
    "Cafe": {"t_min": 15, "t_max": 25, "h_max": 70},
    "Miel": {"t_min": 0, "t_max": 25, "h_max": 70},
}
def seuil_pour(produit):
    return SEUILS.get(produit, {"t_min": 15, "t_max": 25, "h_max": 80})
