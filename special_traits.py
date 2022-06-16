import random
import numpy as np 
import pandas as pd

#Special Traits
def random_special_trait(): 
  df_special_trait = pd.read_excel("data/special_traits.xlsx")
  random_special_trait = df_special_trait.sample(1)
  special_trait_dict = {"Special Trait": random_special_trait.iloc[0,0]}
  return special_trait_dict

