def processar_reservas():
    # Entrada dos quartos disponíveis
    quartos_disponiveis = set(map(int, input().split()))
    
    # Entrada das reservas solicitadas
    reservas_solicitadas = list(map(int, input().split()))

    # TODO: Crie o processamento das reservas:
    reservas_confirmadas = []
    reservas_recusadas = []
    
    for quarto_solicitado in reservas_solicitadas:

    # TODO: Verifique se cada reserva pode ser confirmada com base na disponibilidade dos quartos: 
    
        if quarto_solicitado in quartos_disponiveis:
            reservas_confirmadas.append(quarto_solicitado)
            quartos_disponiveis.remove(quarto_solicitado)
        else:
            reservas_recusadas.append(quarto_solicitado)

    # Saída dos resultados conforme especificação
    print("Reservas confirmadas:", " ".join(map(str, reservas_confirmadas)))
    print("Reservas recusadas:", " ".join(map(str, reservas_recusadas)))

# Chamada da função principal
processar_reservas()
