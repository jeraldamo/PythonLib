class RadioGroupException(Exception):
    pass

class RadioGroup(dict):
    def __init__(self, *arg, **kw):
        super(RadioGroup, self).__init__(*arg, **kw)
        self.activeKey = None
        self.sampleBool = True

    def __setitem__(self, key, value):
        if type(value) != type(self.sampleBool):
            raise RadioGroupException("Value is not a boolean")
        else:
            super(RadioGroup, self).__setitem__(key, value)

        if value:
            if self.activeKey:
                super(RadioGroup, self).__setitem__(self.activeKey, False)
            self.activeKey = key
        else:
            if key == self.activeKey:
                self.activeKey = None
