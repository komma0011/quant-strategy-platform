from data.loader import load_data
from strategy.strategy import check_signal


strategy_config = {
    'name': '이동평균 전략',
    'conditions': [
        {
            'indicator': 'moving_average',
            'period': 3,
            'operator': '>'
        },
        {
            'indicator': 'moving_average',
            'period': 4,
            'operator': '>'
        }
    ]
}


df = load_data()

result = check_signal(
    df,
    strategy_config
)

print(result)