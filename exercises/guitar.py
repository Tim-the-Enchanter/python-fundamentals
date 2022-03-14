# Guitar example from OOP
class Guitar:
    def __init__(self, material_type, sound_type, string_style, sound_state):
        self._material_type = material_type
        self._sound_type = sound_type
        self._string_style = string_style
        self._sound_state = sound_state

    def sound_state_strum_pick(self):
        print(str.format('The guitar is being {0}.', self._sound_state))

    @property
    def material_type(self):
        return self._material_type

    @material_type.setter
    def material_type(self, mtype):
        self._material_type = mtype

    @property
    def sound_type(self):
        return self._sound_type

    @sound_type.setter
    def sound_type(self, stype):
        self._sound_type = stype

    @property
    def string_style(self):
        return self._string_style

    @string_style.setter
    def string_style(self, strstyl):
        self.string_style = strstyl

    @property
    def sound_state(self):
        return self._sound_state

    @sound_state.setter
    def sound_state(self, varst):
        self._sound_state = varst


my_guitar = Guitar('resin', 'electric', '6 string', 'picked')
print(my_guitar.sound_state_strum_pick())
print('( ಠ_ಠ)')