##How do you filter a Pandas DataFrame row if you're looking for exact matches?  

```
>>> df
animal    one  two    three
mouse     1    2      3
rabbit    4    5      6
```

#### select rows containing 'mouse'

```python
print (df[df['animal'].str.contains("mouse")])
```
```
animal    one  two    three
mouse     1    2      3
```

##How do you filter if you have partial matches or substrings you're looking for?  

#### select rows containing 'bbi'

```python
df.filter(like='bbi', axis=0)
```
```
animal    one  two    three
rabbit    4    5      6
```


#####*Sources:*  
<http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.filter.html>  