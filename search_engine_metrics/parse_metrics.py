import pandas as pd

class SearchEngine:
    def __init__(self, path_to_metrics) -> None:
        self.metrics_df = pd.read_csv(path_to_metrics, sep='\t')