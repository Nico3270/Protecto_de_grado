def tipo_terreno(num):
    if num < 3:
        return "Terreno Plano"
    elif num < 6:
        return "Terreno Ondulado"
    elif num < 9:
        return "Terreno Montañoso"
    else:
        return "Terreno Escarpado"

print(tipo_terreno(7.5))