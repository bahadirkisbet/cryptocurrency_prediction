from binance.client import Client

def get_data_for_currency(_symbol,_interval,_start="01/01/2010",_end="now UTC"):
    '''
    return format
    arr[0] = start of time interval
    arr[1] = OPEN
    arr[2] = HIGH
    arr[3] = LOW
    arr[4] = CLOSE
    arr[5] = Volume
    arr[6] = end of the time interval
    arr[7] = Quote asset volume
    arr[8] = number of trades
    arr[9] = taker buy base asset volume
    arr[10] = taker buy quota asset volume
    arr[11] = Ignore
    '''
    cli = Client()
    data = cli.get_historical_klines(symbol=_symbol,interval=_interval,start_str=_start,end_str=_end)
    for i in range(len(data)):
        data[i] = [ float(data[i][j]) for j in range(12) ]
    return data

    
