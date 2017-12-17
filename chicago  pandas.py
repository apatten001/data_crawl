import pandas as pd

headers = ['name', 'title', 'department', 'sal or hrly','salary']
chicago = pd.read_csv("chicago emp.csv", header = None, names = headers)

# header = False moves top row down and names = changes the names of headers

print(chicago)
print(chicago.tail(7))

dept = chicago.groupby("department")
# groupby funnction groups it by depaartment which is key index 

#print(dept.count().head(6))

#print(dept.size().head(15))
# shows the number of instances in that department


# dataframe.mean() or sum() allows you to get the summ or mean of the
# dataframe. we cant do that now because salary are in $

chicago.set_index("title", inplace = True)

#print(chicago[10:15])

