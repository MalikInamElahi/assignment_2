import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker
from matplotlib.ticker import ScalarFormatter

file_name = 'Property Sales data.csv'
df= pd.read_csv(file_name)
print(df)


'''def line_chart_by_property_type(df):
    # Group data by Year and PropertyType and calculate the average price
    avg_price_by_year_property_type = df.groupby(['Year', 'propertyType'])['price'].mean().reset_index()

    # Plotting the line chart
    plt.figure(figsize=(10, 6))

    # Separate data for House and Unit
    house_price = avg_price_by_year_property_type[avg_price_by_year_property_type['propertyType'] == 'house']
    unit_price = avg_price_by_year_property_type[avg_price_by_year_property_type['propertyType'] == 'unit']

    # Plotting lines for House and Unit
    plt.plot(house_price['Year'], house_price['price'], marker='o', label='House')
    plt.plot(unit_price['Year'], unit_price['price'], marker='o', label='Unit')

    # Adding labels and title
    plt.xlabel('Year')
    plt.ylabel('Average Price')
    plt.title('Property Prices Over the Years by Property Type')
    plt.legend()
    plt.show()


line_chart_by_property_type(df)'''

'''def price_histogram(df):
    # Plotting the histogram
    plt.figure(figsize=(10, 6))
    plt.hist(df['price'], bins=20, color='black', edgecolor='black')

    # Adding labels and title
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.title('Distribution of Property Prices')
    plt.gca().xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
    plt.ticklabel_format(axis='x', style='plain')
    # Show the plot
    plt.show()

# Call the function with your DataFrame
price_histogram(df)'''




'''def bar_plot(df):
    # Group data by PropertyType and calculate the sum of prices
    price_sum_by_property_type = df.groupby('propertyType')['price'].sum()

    # Plotting the bar plot
    plt.figure(figsize=(10, 6))
    ax=price_sum_by_property_type.plot(kind='bar', color=['skyblue', 'salmon'])

    ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
    ax.ticklabel_format(axis='y', style='plain')

    # Adding labels and title
    plt.xlabel('Property Type')
    plt.ylabel('Total Price')
    plt.title('Total Price Sum for Houses and Units')

    # Show the plot
    plt.show()

# Call the function with your DataFrame
bar_plot(df)'''











