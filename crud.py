import pickle

def save(data,file:str = "data.pickle"):
    """save data to pickle file"""
    with open(file,"wb") as f:
        pickle.dump(data,f)


def load(file:str = "data.pickle"):
    """Loads a pickle file and return data"""
    with open(file,"rb") as f:
        data = pickle.load(file=f)
    return data
