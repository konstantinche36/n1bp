from itertools import count


class BObj:
    _ids = count(0)

    def __init__(self, name=None):
        self.id = next(self._ids)
        if name is None:
            self.name = 'def_name_' + str(self.id)
        else:
            self.name = name + '_' + str(self.id)

    def get_name(self):
        return self.name


class BPoint(BObj):
    B_POINT_NAME_PART = 'POINT_'
    DEF_COLOR = (0, 0, 250)
    DEF_RADIUS = 3

    def __init__(self, name, x, y, color: (int, int, int) = DEF_COLOR, radius: int = DEF_RADIUS):
        super().__init__(BPoint.B_POINT_NAME_PART + name)
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_color(self, color: (int, int, int) = DEF_COLOR):
        self.color = color

    def get_color(self):
        return self.color

    def set_radius(self, radius: int = DEF_RADIUS):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def __str__(self):
        return f'{self.name} x:{self.x}, y:{self.y}'
