def berechne_brutto(netto_preis: float, mwst_satz: float = 19.0) -> float:
    """Berechnet den Bruttopreis."""
    if netto_preis < 0:
        raise ValueError("Der Nettopreis kann nicht negativ sein.")
    return round(netto_preis * (1 + mwst_satz / 100), 2)