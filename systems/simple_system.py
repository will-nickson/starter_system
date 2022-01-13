# import data 

# import Rule
# import System
# import ForecastCombine
# import ForecastScaleCap
# import PositionSizing
# import Portfolios
# import Account
# import RawData


def simple_system(data=None, config=None, log_level="on"):
    """
        The most simple trading system possible
    """

    my_system = System(
        [
            Account(),
            Portfolios(),
            PositionSizing(),
            ForecastCombine(),
            ForecastScaleCap(),
            Rules(),
            RawData()
        ],
        data,
        config
    )

    my_system.set_logging_level(log_level)

    return my_system
