def check_signal(df, strategy_config):

    conditions = strategy_config['conditions']

    df['signal'] = True

    for condition in conditions:

        ma_period = condition['period']

        df['moving_average'] = df['price'].rolling(ma_period).mean()

        condition_result = df['price'] > df['moving_average']

        df['signal'] = df['signal'] & condition_result

    return df