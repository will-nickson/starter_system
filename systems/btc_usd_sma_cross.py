import pandas as pd
import plotly.graph_objects as go
import matplotlib as plt
import numpy as np

historical = pd.DataFrame(historical['result'])
historical.drop(['startTime'], axis = 1, inplace=True)
historical['time'] = pd.to_datetime(historical['time'], unit='ms')
historical.set_index('time', inplace=True)
historical['16_SMA'] = historical.close.rolling(16).mean()
historical['64_SMA'] = historical.close.rolling(64).mean()

print(historical.tail())

fig = go.Figure(data=[go.Candlestick(x = historical.index,
                                   open = historical['open'],
                                   high = historical['high'],
                                   low = historical['low'],
                                   close = historical['close'],
                                   ),
                    go.Scatter(x = historical.index, y=historical['16_SMA'], line=dict(color='purple', width=1)),
                    go.Scatter(x = historical.index, y=historical['64_SMA'], line=dict(color='blue', width=1))])


# fig.show()
