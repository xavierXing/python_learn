"""
    空气质量计算 4.0版本
"""
import json
import csv 
import os

def process_json_file(filePath):
    """
        解码json文件
    """
    with open(filePath, "r", encoding="utf-8") as f:
        city_list = json.load(f)
    print(city_list)

def process_csv_file(filePath):
    """
        解码csv文件
    """
    with open(filePath, "r", encoding="utf-8", newline="") as f:
        render = csv.reader(f)
        for value in render:
            print(", ".join(value))


def main():
    """
     主函数
    """
    filePath = input('请输入文件路径: ')
    filename, file_ext = os.path.splitext(filePath)
    if file_ext == ".json":
        # json 文件
        process_json_file(filePath)
        pass
    elif file_ext == ".csv":
        process_csv_file(filePath)
        pass
    else:
        print("不支持文件格式! ")



if __name__ == '__main__':
    main()