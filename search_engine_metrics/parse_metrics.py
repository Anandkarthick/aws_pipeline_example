
import pandas as pd
import boto3
import awswrangler as wr

from data_patterns import PatternMatch as pm

class SearchEngine:
    def __init__(self, path_to_metrics) -> None:
        self.boto3_Session = boto3.Session(profile_name='profile')
        self.s3_client = boto3.client('s3')
        self.path_to_metrics = path_to_metrics
        #self.metrics_df = pd.read_csv(self.path_to_metrics, sep='\t')
        self.search_engine = ['google', 'bing']
    
    def get_domain(self, string):
        if pm(string).get_domain_name():
            return pm(string).get_domain_name()[0]
        else:
            return ""

    def __parse_products__(self, product):
        return product.split(",")

    def calculate_revenue(self):
        pass
    

    
    
    