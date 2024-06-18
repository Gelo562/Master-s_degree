import pandas as pd
import numpy as np

covidcases = pd.read_csv("covidcases720.csv")

#a
print("a)")
dailyvars = ['casedate', 'new_cases', 'new_deaths']
totvars = ['location', 'total_cases', 'total_deaths']
demovars = ['population', 'population_density', 'median_age', 'gdp_per_capita', 'hospital_beds_per_thousand', 'region']
print("dailyvars:",dailyvars)
print("totvars:",totvars)
print("demovars:",demovars)

#b
print("b)")
subset_columns = dailyvars + totvars + demovars
subset_df = covidcases[subset_columns]
print(subset_df.head(3).transpose())

#c
print("c)")
coviddaily = covidcases[['location'] + dailyvars]
print("Rozmiar coviddaily:", coviddaily.shape)
print("Pierwsze 5 wierszy:\n", coviddaily.head(5))

#d
print("d)")
unique_locations = covidcases['location'].nunique()
print("Liczba unikalnych wartości w kolumnie 'location':", unique_locations)

#e
print("e)")
coviddemo = covidcases[['casedate'] + totvars + demovars]
coviddemo = coviddemo.sort_values(by=['location', 'casedate'])
coviddemo = coviddemo.drop_duplicates(subset='location', keep='last')
coviddemo = coviddemo.rename(columns={'casedate': 'lastdate'})
print(coviddemo)