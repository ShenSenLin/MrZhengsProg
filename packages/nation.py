"""
本文件描述了国家类
"""


# 国家类
class Nation:
    def __init__(self, name):
        # 国家属性定义
        self.name = name  # 国家名.
        self.capital = None  # 首都
        self.cities = []  # 拥有城市
        self.war_level = 0  # 战争等级
        self.tech_lever = 0  # 工艺水平
        self.money = 0  # 资金
        self.income = 0  # 每回合收益
        # End

    # 重写打印输出
    def __str__(self):
        return self.name
