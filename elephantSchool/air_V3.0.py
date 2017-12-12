"""
    空气质量计算 3.0版本
"""
import json
import csv

def process_json_file(filePath):
    """
        解码json文件
    """
    f = open(filePath, "r", encoding="utf-8")
    city_list = json.load(f)
    return city_list

def main():
    """
     主函数
    """
    filePath = input('请输入json文件路径: ')
    city_list = process_json_file(filePath)
    city_list.sort(key=lambda city: city["aqi"])

    lines = []
    # 列名
    lines.append(list(city_list[0].keys()))
    for city in city_list:
        lines.append(list(city.values()))

    f = open("aqi.csv", "w", encoding="utf-8", newline="")
    writer = csv.writer(f)
    for line in lines:
        writer.writerow(line)
    f.close()


if __name__ == '__main__':
    main()