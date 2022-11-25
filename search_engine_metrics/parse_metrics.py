import boto3
import pandas as pd
import os
#import awswrangler as wr

from data_patterns import PatternMatch as pm

class SearchEngine:
    def __init__(self, path_to_metrics) -> None:
        self.path_list = path_to_metrics.split("/")
        self.path_to_metrics = path_to_metrics
        # adjusting environment
        try:
            self.boto3_Session = boto3.Session(profile_name='personal')
        except:
            self.boto3_Session = boto3.Session()
        # create s3 client object from session
        self.s3_client = self.boto3_Session.client('s3')
        # params for s3
        self.bucket = self.path_list[2]
        self.s3_key = "/".join(self.path_list[3:])
        self.file_name = self.path_list[-1]

        # download file from s3
        self.s3_client.download_file(self.bucket, self.s3_key, self.file_name)
        # read file in dataframe
        self.data = pd.read_csv(self.file_name, sep='\t')
        
        #self.boto3_Session = boto3.Session()
        #self.data = wr.s3.read_csv(path_to_metrics, sep='\t',  boto3_session=self.boto3_Session)
        #self.metrics_df = pd.read_csv(self.path_to_metrics, sep='\t')
    
    def get_domain(self):
        if 'referrer' in self.data.columns:
            self.data['Search Engine Domain'] = self.data['referrer'].apply(lambda x: pm(x).get_domain_name()[0])
        else:
            self.data['Search Engine Domain'] = ''
        return self

    def __parse_products__(self):
        if 'product_list' in self.data.columns:
            self.data['product_list'] = self.data['product_list'].fillna('')
            self.data['products'] = self.data['product_list'].apply(lambda x: str(x).split(","))
        else:
            self.data['products'] = []
        return self

    def __list_key_zero__(self, string, delim, key):
        result = 0
        try:
            result = int(string.split(delim)[key])
        except:
            return 0
        return result if result else 0

    def __calculate_revenue__(self, product_list):
        # calculate revenue
        revenue = 0
        for product in product_list:
            qty = self.__list_key_zero__(product, ";", 2)
            price = self.__list_key_zero__(product, ";", 3)
            revenue += (qty * price)
        return revenue

    def __calculate_keywords__(self, string):
        result = []
        for param in pm(string).extract_search_params():
            clean_search = param.replace("q=", '').replace("k=", '').replace("&", '')
            if param.lower().startswith(("q=", "k=")) and len(clean_search) > 1:
                result.append(clean_search.strip().lower())
        return " ".join(result)

    def get_keywords(self):
        self.data['Search Keyword'] = self.data['referrer'].apply(lambda x: self.__calculate_keywords__(x))
        return

    def get_revenue(self):
        # parse product to create lsit
        self.__parse_products__()
        self.data['Revenue'] = self.data['products'].apply(lambda x: self.__calculate_revenue__(x))
        return self
    
    def write_to_s3(self, dataframe, s3key, key):
        # write file locally
        dataframe.to_csv(key, sep='\t')
        response = self.s3_client.upload_file(key, self.bucket, key)

    """
    def write_to_s3_v1(self, dataframe, key):
       return  wr.s3.to_csv(dataframe,
                     path = key,
                     sep='\t',  boto3_session=self.boto3_Session)
    """
    
    
    
    