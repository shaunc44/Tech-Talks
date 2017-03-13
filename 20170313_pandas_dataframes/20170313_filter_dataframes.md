#How do you filter a row of a Pandas DataFrame if you're looking for exact matches?  

```
>>> df
one  two  three
mouse     1    2      3
rabbit    4    5      6
```

#How do you filter if you have partial matches or substrings you're looking for?  

#### select rows containing 'bbi'

```python
df.filter(like='bbi', axis=0)
```
```
one  two  three
rabbit    4    5      6
```


#####*Sources:*  
<http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.filter.html>  