"""
本文件包括:
    【士兵类】
    【市民类】
    【奴隶类】
    【领导者类】
主要描述游戏中可以移动的各单位
"""


# 单位类
# 是所有可以移动的单位类的父类
class Unit:
    def __init__(self):
        self.coordinate = [0, 0, 0]  # 坐标
        self.nation = None  # 所属国家
        self.health = 0  # 生命值

    # 移动函数
    def move(self):
        pass


class Soilder(Unit):  # 士兵
    def __init__(self):
        pass

    # 攻击 - 攻击指定地点
    def attack(self):
        pass

    # 保护 - 保护指定单位
    def protect(self):
        pass


class Citizen(Unit):  # 市民
    def __init__(self):
        pass


class Slaves(Unit):  # 奴隶
    def __init__(self):
        pass


class Leader(Unit):
    def __init__(self):
        pass