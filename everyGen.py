import pandas as pd

data = [
    [True, True],
    [True, True],
    [True, False]
]
df = pd.DataFrame(data,
                  columns=['Każde pokolenie', 'Nasze pokolenie'],
                  index=['Ma własny czas', 'Chce zmienić świat', 'Odejdzie w cień'])
print(df)
