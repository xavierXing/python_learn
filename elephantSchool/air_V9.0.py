"""
    空气质量计算v9.0
"""

import pandas as pd


def main():
    """
        主函数
    """
    aqi_data = pd.read_csv('china_city_aqi.csv')
    # print(aqi_data.head(5))
    # print(aqi_data[['City', 'AQI']])
    print("基本信息: ")
    print(aqi_data.info())

    print("数据预览: ")
    print(aqi_data.head())

    print("AQI最大值: ", aqi_data['AQI'].max())
    print("AQI最小值: ", aqi_data['AQI'].min())
    print("AQI均值: ", aqi_data['AQI'].mean())

    top10_city = aqi_data.sort_values(by=['AQI']).head(10)
    print("空气质量最好的10个城市: ")
    print(top10_city)

    # bottom10_city = aqi_data.sort_values(by=['AQI']).tail(10)
    bottom10_city = aqi_data.sort_values(by=['AQI'], ascending=False).head(10)
    print("空气质量最差的10个城市: ")
    print(bottom10_city)

    #保存csv文件
    top10_city.to_csv('top10_aqi.csv', index=False, encoding='utf-8')
    bottom10_city.to_csv('bottom10_aqi.csv', index=False, encoding='utf-8')

if __name__ == '__main__':
    main()