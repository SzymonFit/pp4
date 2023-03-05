def netto(brutto, podatek):
    cena_netto = brutto / (1 + podatek)
    return cena_netto