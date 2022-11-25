import re

class PatternMatch:
    def __init__(self, string) -> None:
        self.string = string

    def extract_url(self):
        return re.findall(r'http:\/\/.+?\/', self.string)
    
    def __isSearch__(self):
        return re.findall(r'http:\/\/.+?\/search', self.string)

    def extract_search_params(self):
        return re.findall(r'[a-z]=.+?&', self.string)
    
    def get_domain_name(self):
        return re.findall(r'\.([^\.]+)\.', self.string)
    

if __name__ == "__main__":

    string = 'http://www.google.com/search?hl=en&client=firefox-a&rls=org.mozilla%3Aen-US%3Aofficial&hs=ZzP&q=Ipod&aq=f&oq=&aqi='

    assert PatternMatch(string).extract_url() == ['http://www.google.com/']
    assert PatternMatch(string).__isSearch__() == ['http://www.google.com/search']
    assert PatternMatch(string).extract_search_params() == ['l=en&', 't=firefox-a&', 's=org.mozilla%3Aen-US%3Aofficial&', 's=ZzP&', 'q=Ipod&', 'q=f&']
    assert PatternMatch(string).get_domain_name() == ['google']