def berechne_brutto(netto_preis: float, mwst_satz: float = 19.0) -> float:
    """Berechnet den Bruttopreis basierend auf Netto-Preis und MwSt-Satz.
    
    Verhindert negative Werte, um Berechnungsfehler zu vermeiden.
    """
    if netto_preis < 0:
        raise ValueError("Der Nettopreis kann nicht negativ sein.")
        
    if mwst_satz < 0:
        raise ValueError("Der MwSt-Satz kann nicht negativ sein.")
        
    brutto = netto_preis * (1 + mwst_satz / 100)
    return round(brutto, 2)


def extrahiere_mwst(brutto_preis: float, mwst_satz: float = 19.0) -> float:
    """Berechnet den enthaltenen MwSt-Betrag aus einem Bruttopreis."""
    if brutto_preis < 0 or mwst_satz < 0:
        raise ValueError("Werte koennen nicht negativ sein.")
        
    netto = brutto_preis / (1 + mwst_satz / 100)
    mwst_betrag = brutto_preis - netto
    return round(mwst_betrag, 2)