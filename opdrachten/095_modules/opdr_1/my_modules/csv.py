def lees_csv(bestandsnaam):
    with open(bestandsnaam, 'r') as f:
        regels = f.readlines()
        headers = regels[0].strip().split(',')
        data = []
        for regel in regels[1:]:
            waarden = regel.strip().split(',')
            persoon = dict(zip(headers, waarden))
            data.append(persoon)
    return data

def filter(lijst, veld, waarde):
    resultaat = []
    for persoon in lijst:
        if persoon[veld].lower().startswith(waarde.lower()):
            resultaat.append(persoon)
    return resultaat