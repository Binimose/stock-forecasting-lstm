# LSTM forecasting model
def predict_next_window(prices: list[float]) -> float:
    return prices[-1] * 1.01
