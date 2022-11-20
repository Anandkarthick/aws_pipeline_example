import pandas as pd

search_metrics = pd.read_csv('search_engine_metrics/data.tsv', sep='\t')

print(search_metrics.head(5))