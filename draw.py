from dataCollector import get_data_for_currency
import finplot as fplt
import pandas as pd

data = get_data_for_currency("BTCUSDT", "1h", "30 days ago UTC", "now UTC")
df = pd.DataFrame(data, columns='time open high low close volume end quote amount trades takerbase takerquote'.split())
fplt.candlestick_ochl(df[['time', 'open', 'close', 'high', 'low']])
fplt.show()

