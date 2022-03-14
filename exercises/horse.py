# Horse example from OOP
class Horse:
    def __init__(self, size, rigging, mane_style, motion_state):
        self._size = size
        self._rigging = rigging
        self._mane_style = mane_style
        self._motion_state = motion_state

    def crnt_motion_state(self):
        print(str.format('The horse is {0}.', self._motion_state))

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, svar):
        self._size = svar

    @property
    def rigging(self):
        return self._rigging

    @rigging.setter
    def rigging(self, rtype):
        self._rigging = rtype

    @property
    def mane_style(self):
        return self._mane_style

    @mane_style.setter
    def mane_style(self, style):
        self.mane_style = style

    @property
    def motion_state(self):
        return self._motion_state

    @motion_state.setter
    def motion_state(self, state):
        self._motion_state = state


my_horse = Horse('giant', 'bareback', 'unkempt', 'galloping')
print(my_horse.crnt_motion_state())
print('(╯°□°）╯')