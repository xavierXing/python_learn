"""
    空气质量计算v9.0
"""

import pandas as pd
import matplotlib.pyplot as plt

def main():
    """
        主函数
    """
    aqi_data = pd.read_csv('china_city_aqi.csv')
    # print(aqi_data.head(5))
    # print(aqi_data[['City', 'AQI']])

    clean_aqi_data = aqi_data[aqi_data['AQI'] > 0]

    print("AQI最大值: ", clean_aqi_data['AQI'].max())
    print("AQI最小值: ", clean_aqi_data['AQI'].min())
    print("AQI均值: ", clean_aqi_data['AQI'].mean())

    top50_cities = clean_aqi_data.sort_values(by=['AQI']).head(50)
    top50_cities.plot(kind='bar', x='City', y='AQI', title='空气质量最好的50个城市', figsize=(20, 10))
    plt.savefig('top50_aqi_bar.png')
    plt.show()

if __name__ == '__main__':
    main()