import pandas as pd

data = {
    "weekdays": ["monday", "friday", "saturday"],
    "roll no": ["45", "56", "79"]
}
# df=pd.DataFrame(data)
df = pd.Series(data)
print(df)
