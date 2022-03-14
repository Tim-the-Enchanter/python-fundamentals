# Watch example from OOP
class Watch:
    def __init__(self, hand_type, finish, battery_type, time_stopped):
        self._hand_type = hand_type
        self._finish = finish
        self._battery_type = battery_type
        self._time_stopped = time_stopped

    def time_watch_stopped(self):
        print(str.format('The time stopped at {0}.', self._time_stopped))

    @property
    def hand_type(self):
        return self._hand_type

    @hand_type.setter
    def hand_type(self, htype):
        self._hand_type = htype

    @property
    def finish(self):
        return self._finish

    @finish.setter
    def finish(self, ftype):
        self._finish = ftype

    @property
    def battery_type(self):
        return self._battery_type

    @battery_type.setter
    def battery_type(self, btype):
        self.battery_type = btype

    @property
    def time_stopped(self):
        return self._time_stopped

    @time_stopped.setter
    def time_stopped(self, val):
        self._time_stopped = val


my_watch = Watch('Analog', 'Brass', 'Kinetic', '11:11')
print(my_watch.time_watch_stopped())
