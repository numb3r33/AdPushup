import numpy as np

class Thompson(object):
    
    def __init__(self, n_ads):
        self.hits = [1] * n_ads # example: total number of hits
        self.views = [1.] * n_ads # example: total number of views
        self.values = [1.] * n_ads # example: hits / views
        self.n = n_ads
    
    def set_views(self, views):
        self.views = views
    
    def set_values(self, values):
        self.values = values
    
    def set_hits(self, hits):
        self.hits = hits
    
    def get_views(self):
        return self.views
    
    def get_values(self):
        return self.values
    
    def get_hits(self):
        return self.hits
    
    
    def recommend_ad(self):
        """Recommends ads"""
        
        for i in range(self.n):
            no_hits = 1 if (self.views[i] - self.hits[i] <= 0)  else (self.views[i] - self.hits[i]) 
            self.values[i] = np.random.beta(self.hits[i], no_hits)

        index_ad = np.argmax(self.values)

        self.update(index_ad, 1)
        
        return index_ad
            
        
    def update(self, ad, reward):
        """Update an ad with some reward""" # Example: click = 1; no click = 0
        
        # update hit stats
        if reward == 1:
            self.hits[ad] = self.hits[ad] + 1

        hit = self.hits[ad]
        
        # update views stat
        self.views[ad] = self.views[ad] + 1
        view = self.views[ad]
        
        # update values
        for i in range(self.n):
            no_hits = 1 if (self.views[i] - self.hits[i] <= 0)  else (self.views[i] - self.hits[i])
            self.values[i] = np.random.beta(self.hits[i], no_hits)