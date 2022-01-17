from binance.enums import *
from Config import *
from Execute_Trade import execute_trade
import json
from Helpers import *
import pandas as pd
from Update_State import update_state
import websocket

SYMBOL = "ADAUSDT"
SOCKET = "wss://fstream.binance.com/ws/adausdt@kline_5m"
loops = 0

change_leverage(SYMBOL, LEVERAGE)

data_5m = generate_initial_data(
    SYMBOL, INTERVALS_5M, 5)
data_30m = generate_initial_data(
    SYMBOL, INTERVALS_30M, 30)


def on_message(ws, message):
    global data_5m, data_30m, loops
    json_msg = json.loads(message)
    candle = json_msg['k']
    candle_closed = candle['x']
    close = float(candle['c'])

    if candle_closed:
        loops += 1

        data_5m.append({"Time": float(candle['t']), "Open": float(candle['o']), "High": float(
            candle['h']), "Low": float(candle['l']), "Close": float(candle['c']), "Volume": float(candle['v'])})
        df_5m = pd.DataFrame(data_5m)

        if loops % 6 == 0:
            data_30m.append(get_last_kline(SYMBOL))
        df_30m = pd.DataFrame(data_30m)

        update_state(SYMBOL)
        execute_trade(SYMBOL, df_5m, df_30m, close)

        if loops == 48:
            ws.close()


ws = websocket.WebSocketApp(
    SOCKET, on_message=on_message)

ws.run_forever(ping_interval=60)
