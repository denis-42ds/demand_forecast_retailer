import pickle
import pandas as pd
import numpy as np
import sklearn

model = pickle.load(open('model_cbr.pkl', 'rb'))

def forecast(sales: dict, item_info: dict, store_info: dict) -> list:
    """
    Функция для предсказания продаж
    :params sales: исторические данные по продажам
    :params item_info: характеристики товара
    :params store_info: характеристики магазина

    """
    ans = model.predict(list)
    print('answer', ans)
    return ans
    
    
    
    
    
    #sales = [el["sales_units"] for el in sales]
    #mean_sale = sum(sales) / len(sales)
    #return [mean_sale] * 5

