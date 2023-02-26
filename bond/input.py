import pandas as pd

from cashflower import Runplan, ModelPoint


runplan = Runplan(data=pd.DataFrame({
    "version": [1],
    "valuation_year": [2022],
    "valuation_month": [12],
}))


policy = ModelPoint(data=pd.DataFrame({"policy_id": [1]}))


assumption = dict()
# assumption["mortality"] = pd.read_csv("")
