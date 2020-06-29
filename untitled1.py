import pandas as pd

test = pd.DataFrame(['2019-09-24T05:09:10.000Z'])
#quotes['month_year'] = pd.to_datetime(quotes['date_approved']).dt.to_period('M')

print(pd.to_datetime(test[0]).dt.to_period('M'))
test[0] = (test[0].astype(str).str[:-17])