import random
import numpy as np 
import pandas as pd

#Spells level 0
def random_0_spells(): 
  df_spells = pd.read_excel("data/level_0_spells.xlsx")
  random_spell = df_spells.sample(1)
  spells_dict = {"Spell": random_spell.iloc[0,0]}
  return spells_dict

#Spells level 1
def random_1_spells(): 
  df_spells = pd.read_excel("data/level_1_spells.xlsx")
  random_spell = df_spells.sample(1)
  spells_dict = {"Spell": random_spell.iloc[0,0]}
  return spells_dict

#Spells level 2
def random_2_spells(): 
  df_spells = pd.read_excel("data/level_2_spells.xlsx")
  random_spell = df_spells.sample(1)
  spells_dict = {"Spell": random_spell.iloc[0,0]}
  return spells_dict

#Spells level 3
def random_3_spells(): 
  df_spells = pd.read_excel("data/level_3_spells.xlsx")
  random_spell = df_spells.sample(1)
  spells_dict = {"Spell": random_spell.iloc[0,0]}
  return spells_dict

#Spells level 4
def random_4_spells(): 
  df_spells = pd.read_excel("data/level_4_spells.xlsx")
  random_spell = df_spells.sample(1)
  spells_dict = {"Spell": random_spell.iloc[0,0]}
  return spells_dict

#Spells level 5
def random_5_spells(): 
  df_spells = pd.read_excel("data/level_5_spells.xlsx")
  random_spell = df_spells.sample(1)
  spells_dict = {"Spell": random_spell.iloc[0,0]}
  return spells_dict

#Spells level 6
def random_6_spells(): 
  df_spells = pd.read_excel("data/level_6_spells.xlsx")
  random_spell = df_spells.sample(1)
  spells_dict = {"Spell": random_spell.iloc[0,0]}
  return spells_dict

#Spells level 7
def random_7_spells(): 
  df_spells = pd.read_excel("data/level_7_spells.xlsx")
  random_spell = df_spells.sample(1)
  spells_dict = {"Spell": random_spell.iloc[0,0]}
  return spells_dict

#Spells level 8
def random_8_spells(): 
  df_spells = pd.read_excel("data/level_8_spells.xlsx")
  random_spell = df_spells.sample(1)
  spells_dict = {"Spell": random_spell.iloc[0,0]}
  return spells_dict

#Spells level 9
def random_9_spells(): 
  df_spells = pd.read_excel("data/level_9_spells.xlsx")
  random_spell = df_spells.sample(1)
  spells_dict = {"Spell": random_spell.iloc[0,0]}
  return spells_dict

