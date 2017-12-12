"""
    空气质量计算 2.0版本
"""
import json

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
    top5 = city_list[:5]

    f = open("top5_aqi.json", mode="w", encoding="utf-8")
    json.dump(top5, f, ensure_ascii=False)
    f.close()

    print(city_list)

if __name__ == '__main__':
    main()