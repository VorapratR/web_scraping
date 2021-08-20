# Webscraping, API, and machine learning interface problem
## Objectives:
- to write a web scraping to scrap the data
- to feed the data into machine learning model
- to write a REST API to interface with user

## Requirements
API input
- user keys in an equity name (e.g. 'scg-packaging-plc','apple-computer-inc')

API specification
1. API receive a request from a user
2. the system shall get real-time values of equity price from investing.com
3. the system shall call machine learning function
4. the system shall return the predicted value to the user

API output
- a predicted value from ml_model


## ml_model function
def ml_model(lst_x = [1,2,3,4,5]):
    y = (lst_x[-1]+lst_x[-2]+lst_x[-3])/3
    return y




```python

```


```python

```


```python

```


```python

```
