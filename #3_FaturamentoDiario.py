def calcular_estatisticas(faturamento_diario):

    menor_valor = min(faturamento_diario)
    maior_valor = max(faturamento_diario)

    media_mensal = sum(faturamento_diario) / len(faturamento_diario)

    dias_acima_da_media = sum(1 for valor in faturamento_diario if valor > media_mensal)

    return menor_valor, maior_valor, dias_acima_da_media


faturamento_diario = [22174.1664, 24537.6698, 26139.6134, 0.0, 0.0, 26742.6612, 0.0, 42889.2258, 46251.174, 11191.4722,
                      0.0, 0.0, 3847.4823, 373.7838, 2659.7563, 48924.2448, 18419.2614, 0.0, 0.0, 35240.1826,
                      43829.1667, 18235.6852, 4355.0662, 13327.1025, 0.0, 0.0, 25681.8318, 1718.1221, 13220.495,
                      8414.61]

menor_valor, maior_valor, dias_acima_da_media = calcular_estatisticas(faturamento_diario)

print("Menor valor de faturamento diário:", menor_valor)
print("Maior valor de faturamento diário:", maior_valor)
print("Número de dias em que o faturamento diário foi superior à média mensal:", dias_acima_da_media)
