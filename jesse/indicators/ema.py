import numpy as np
import talib
import jesse.helpers as jh
from typing import Union


def ema(candles: np.ndarray, period=5, source_type="close", sequential=False) -> Union[float, np.ndarray]:
    """
    EMA - Exponential Moving Average

    :param candles: np.ndarray
    :param period: int - default: 5
    :param source_type: str - default: "close"
    :param sequential: bool - default=False

    :return: float | np.ndarray
    """
    if not sequential and len(candles) > 240:
        candles = candles[-240:]

    source = jh.get_candle_source(candles, source_type=source_type)
    res = talib.EMA(source, timeperiod=period)

    return res if sequential else res[-1]
