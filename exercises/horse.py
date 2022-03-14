# Horse example from OOP
# print(my_Stallion.crnt_motion_state()) as well as all the other calls were printing none.
# I removed the print call and there was no more 'None'! ＼( °□° )／
class Horse:
    def __init__(self, size, rigging, mane_style, motion_state):
        self._size = size
        self._rigging = rigging
        self._mane_style = mane_style
        self._motion_state = motion_state

    def crnt_motion_state(self):
        print(str.format('\nThe horse is {0}.', self._motion_state))

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


my_horse = Horse('giant', 'saddled', 'unkempt', 'galloping')
my_horse.crnt_motion_state()

print('(╯°□°）╯')

# 4.Using your horse Objects from the Encapsulation exercise, create your 2 child
# objects from the OOP section of the previous class. Use the property decorator
# for your child objects. Put both children objects inside your horse.py file.


class Pony(Horse):
    def __init__(self, size, rigging, mane_style, motion_state):
        super().__init__(size, rigging, mane_style, motion_state)
        self._size = size
        self._rigging = rigging
        self._mane_style = mane_style
        self._motion_state = motion_state

    def crnt_motion_state(self):
        print(str.format('\nThe Pony is {0}.', self._motion_state))

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


my_pony = Pony('tiny', 'saddled', 'braided', 'cantering')
my_pony.crnt_motion_state()
print('~(˘▾˘~)')


class Stallion(Horse):
    def __init__(self, size, rigging, mane_style, motion_state):
        super().__init__(size, rigging, mane_style, motion_state)
        self._size = size
        self._rigging = rigging
        self._mane_style = mane_style
        self._motion_state = motion_state

    def crnt_motion_state(self):
        print(str.format('\nThe Stallion is {0}.', self._motion_state))

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


my_stallion = Stallion('large', 'bareback', 'flowing', 'full sprint')
my_stallion.crnt_motion_state()
print('(ﾉಥ益ಥ）ﾉ ')


class Horse:
    # constructor
    def __init__(self, family):
        self._family = family

    def info(self):
        pass

    def make_sound(self):
        return 'Nay goes the {0}'.format(self._family)

    def __str__(self):
        return self._family


class Pony(Horse):
    # Constructor
    def __init__(self, name):
        super().__init__('Shetlan')
        self._name = name

    def info(self):
        return '\nMy horse\'s name is {0} and he is a {1}'. format(self._name, self._family)

    def make_sound(self):
        return 'winny'

    def __str__(self):
        return self._name


class Stallion(Horse):
    def __init__(self, name):
        super().__init__('Wild Horse')
        self._name = name

    def info(self):
        return 'My Stallion\'s name is {0} and he is a {1}'.format(self._name, self._family)

    def __str__(self):
        return self._name


my_horse = Horse('Lucky')
my_pony = Horse('George')
my_pony.info()
my_stallion = Horse('Beauty')
