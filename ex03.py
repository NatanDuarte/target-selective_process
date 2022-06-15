from json import load


def get_relevant_data(data: list) -> list:
    """Aplica um filtro para remover os dados 
    irrelevantes para calcular a média"""
    return list(
        filter(
            lambda daily_billing: daily_billing['valor'] > 0.0,
            data
        )
    )


def get_minimum_billing(data: list):
    if data is not None:
        min = data[0]
        for billing in data:
            if billing['valor'] <= min['valor']:
                min = billing
        return min


def get_maximum_billing(data: list):
    if data is not None:
        max = {'dia': 0, 'valor': 0}
        for billing in data:
            if billing['valor'] >= max['valor']:
                max = billing
        return max


def calculate_mensal_mean(data: list):
    total_of_elements = len(data)
    summation = 0
    for item in data:
        summation += item['valor']
    return summation / total_of_elements


def get_days_above_average(data, mean):
    days = 0
    for item in data:
        if item['valor'] > mean:
            days += 1
    return days


def main():
    DATA_FILE_PATH = './dados.json'

    with open(DATA_FILE_PATH, 'r') as file:
        data = load(file)

    relevant_data = get_relevant_data(data)

    minimum_billing = get_minimum_billing(relevant_data)
    maximum_billing = get_maximum_billing(relevant_data)

    mensal_mean = calculate_mensal_mean(relevant_data)
    days_above_average = get_days_above_average(relevant_data, mensal_mean)

    print(f'O menor valor de faturamento ocorreu no dia {minimum_billing["dia"]} \
no valor de R$ {minimum_billing["valor"]:.2f}.')
    print(f'O maior valor de faturamento ocorreu no dia {maximum_billing["dia"]} \
no valor de R$ {maximum_billing["valor"]:.2f}.')
    print(f'{days_above_average} dias superaram da média mensal (R$ {mensal_mean:.2f})')


main()
