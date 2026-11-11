import pandas as pd

# using list
product_data=[['e-book', 2000], ['plants', 6000], ['Pencil', 3000]] #
#2d list, similar to 2d array
indexes=[1,2,3]
columns_name=['product', 'unit_sold']
product_df = pd.DataFrame(data=product_data, index=indexes,
columns=columns_name)
print(product_df)


