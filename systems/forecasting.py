import pandas as pd

from systems.stage import SystemStage
# from systems.trading_rules import TradingRule

class Rules(SystemStage):
    """
        Construct the forecasting stage
    """

    def __init__(self, trading_rules):
        super().__init__()
        self._trading_rules = None
        self._passed_trading_rules = trading_rules

    def name(self):
        return "rules"
    
    @property
    def passed_trading_rules(self):
        return self._passed_trading_rules

    def __repr__(self):
        trading_rules = self.trading_rules()
        rule_name = ", ".join(trading_rules.keys())
        return "Rules object with rules " + rule_name
    
    @output()
    def get_raw_forecast(self, instrument_code, rule_variation_name):
        """
            Gets the forecast for the trading rule
        """

        system = self.parent

        self.log.msg(
            "Calculating raw forecast %s for %s"
            % (instrument_code, rule_variation_name),
            instrument_code=instrument_code,
            rule_variation_name=rule_variation_name,
        ) 

        trading_rule_dict = self.trading_rules()
        trading_rule = trading_rule_dict[rule_variation_name]

        result = trading_rule.call(system, instrument_code)
        result = pd.Series(result)

        return result

    # def trading_rules(self)

    # def _get_trading_rules_from_passed_rules(self)

    # def _get_rules_from_parent_or_raise_errors(self)

def process_trading_rules(passed_rules):
    """
        Process all the trading rules passed and return a dict of TradingRule objects
    """
    pass
