import pandas as pd

class GraphDataFrame:
    def __init__(self):
        self.df = pd.read_csv("Nutricion nestor.csv")
        
    def getCategories(self):
        return self.df['category'].unique().tolist()

    def getDataCategory(self, category):
        if category is None: category = 'healthy'
        
        return self.df.loc[self.df['category'] == category]

    def getDataProperty(self, property):
        if property is None: property = 'sodium'
        
        return self.df[['category', property]]
    
    def getDataPurpose(self, purpose):
        
        data = self.df[['category','name','calories']]
        
        if purpose == 'enflacar':
            ncat1 = 'healthy'
            ncat2 = 'sugar free'
            
        elif purpose == 'ganar_musculo':
            ncat1 = 'raw'
            ncat2 = 'cooked'
            
        else:
            ncat1 = 'healthy'
            ncat2 = 'cooked'
        
        category1 = data.loc[data['category'] == ncat1]
        category2 = data.loc[data['category'] == ncat2]
        
        categories = pd.concat([category1, category2])
        
        return categories #.groupby(['category', 'name'])['calories'].mean()
    
    def getDataCharacteristics(self, characteristics):
        if characteristics is None: characteristics = 'sodium'
        
        return self.df[['category', characteristics]]


def getCategoryOptions(categories):
    options = []
    
    for category in categories:
        dic = {'label': category, 'value': category}
        options.append(dic)
        
    return options

# gdf = GraphDataFrame()
# print(gdf.getDataPurpose('enflacar'))