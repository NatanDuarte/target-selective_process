data = [
    {'state': 'SP', 'value': 67836.43},
    {'state': 'RJ', 'value': 36678.66},
    {'state': 'MG', 'value': 29229.88},
    {'state': 'ES', 'value': 27165.48},
    {'state': 'Outros', 'value': 19849.53},
]


def get_total_billing(data):
    summation = 0
    for billing in data:
        summation += billing['value']
    return summation


def get_data_percentual(data):
    total = get_total_billing(data)
    for index, billing in enumerate(data):
        data[index]['percentual'] = billing['value'] / total * 100
    return data


data = get_data_percentual(data)

for item in data:
    print(f'{item["state"]} - {item["percentual"]:.2f} %')
