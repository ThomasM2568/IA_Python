import pandas as pd
from datetime import datetime


current_date = pd.Timestamp(datetime.now().date())
print("Current date :", current_date)