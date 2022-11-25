import sys

from data_patterns import PatternMatch as pm
from parse_metrics import SearchEngine as se
from datetime import datetime

def lambda_function(event, context):
    path_to_file = sys.argv[1]
    metrics = se(path_to_file)
    metrics.get_domain().get_revenue().get_keywords()
    print(f"Shape of dataframe after initial formatting, {metrics.data.shape}")
    # select columns
    final_df = metrics.data[['Search Engine Domain', 'Search Keyword', 'Revenue']]\
            .groupby(['Search Engine Domain', 'Search Keyword']).sum('Revenue')\
            .reset_index().sort_values(by=['Revenue'], ascending=False)
    # filter out data to ignore shop domain
    final_df = final_df[final_df['Search Engine Domain'] != 'esshopzilla']    
    # write to s3
    file_name = f"{datetime.now().strftime('%Y-%m-%d')}_SearchKeywordPerformance.tab"
    derived_s3_path = "/".join(path_to_file.split("/")[2:-1])
    s3_key = f"s3://{derived_s3_path}/{file_name}"
    metrics.write_to_s3(final_df, s3_key, file_name)

if __name__ == "__main__":
    lambda_function(event="a", context="b")