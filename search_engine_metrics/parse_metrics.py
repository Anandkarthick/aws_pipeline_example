import pandas as pd
import re
import json

class SearchEngine:
    def __init__(self, path_to_metrics) -> None:
        self.path_to_metrics = path_to_metrics
        self.metrics_df = pd.read_csv(self.path_to_metrics, sep='\t')
    
    