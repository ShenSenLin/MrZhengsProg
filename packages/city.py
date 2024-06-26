"""
本文件包括城市类
主要用于描述城市
"""


# 所有可能会出现的城市名
# 采用结构体形式
class CityNames:
    def __init__(self):
        pass


class City:
    def __init__(self):
        self.name = None
        self.coordinate = [0, 0, 0]  # 坐标
        self.nation = None  # 所属国家
