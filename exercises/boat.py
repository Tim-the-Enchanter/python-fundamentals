# Boat example from OOP
class Boat:
    def __init__(self, surface_color, frame_type, engine_type, engine_idle):
        self._surface_color = surface_color
        self._frame_type = frame_type
        self._engine_type = engine_type
        self._engine_idle = engine_idle

    def engine_idle_on_off(self):
        print(str.format('The engine is {0}', self._engine_idle))

    @property
    def surface_color(self):
        return self._surface_color

    @surface_color.setter
    def surface_color(self, color):
        self._frame_type = color

    @property
    def frame_type(self):
        return self._frame_type

    @frame_type.setter
    def frame_type(self, ftype):
        self._frame_type = ftype

    @property
    def engine_type(self):
        return self._engine_type

    @engine_type.setter
    def engine_type(self, etype):
        self.engine_type = etype

    @property
    def engine_idle(self):
        return self._engine_idle

    @engine_idle.setter
    def engine_idle(self, color):
        self._engine_idle = color


my_boat = Boat('White', 'Wooden', 'Sailboat', 'Off')
print(my_boat.engine_idle_on_off())
print('"None" in output (ノಠ益ಠ)ノ彡┻━┻ ')
# Not sure why its saying none on output, but i remember in the video you mentioned you would go over it later.

