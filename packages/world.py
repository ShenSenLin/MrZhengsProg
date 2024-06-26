"""
本文件包括世界地图类和地图块类
描述世界地图和每一个地图块
"""


# 世界地图类
# 这是描述整个地图的类
class WorldMap:
    def __init__(self):
        self.world = [[]]  # 地图列表 二维 储存mapBlock
        self.width = 0  # 地图宽
        self.height = 0  # 地图高

    # 创建地图 （约等于重置）
    def create_map(self):
        pass

    # 打印地图
    def print_map(self):
        pass


# 地图块类
# 描述每一个地图上的地图块
# 本类隶属于地图类
class MapBlock:
    def __init__(self):
        # 地图块可以有的类型
        self.TYPE_BUILDING = "building"  # 建筑类型
        self.TYPE_SPACE = "space"   # 空地类型
        self.TYPE_WATER_AREA = "water_area"  # 水域类型
        self.TYPE_RESOURCE = "resource"  # 资源点
        # End

        self.elevation = 0  # 海拔
        self.type = self.TYPE_SPACE  # 地图块类型 比如建筑、空地、水域等
        self.lodger = [[]]  # 停留在这块地上的东西 比如士兵、奴隶、市民
