# import DataFrame 
import pandas as pd 
  
# using DataFrame.to_html() method 
city_data_to_load = "Resources/cities.csv"

# Read City Data File and store into Pandas DataFrames
city_data = pd.read_csv(city_data_to_load)
html = city_data.to_html(index = False)

#write html to file
text_file = open("raw_data.html", "w")
text_file.write(html)
text_file.close()