import pandas as pd

data = {
    'W': [68, 75, 86, 80, 66],
    'X': [78, 85, 96, 80, 86],
    'Y': [84, 94, 89, 83, 86],
    'Z': [86, 97, 96, 72, 83]
}

df = pd.DataFrame(data)

df_prefix = df.add_prefix("A_")
print(f"Prefix: \n {df_prefix} \n")

df_suffix = df.add_suffix("_1")
print(f"Suffix: \n {df_suffix}")
