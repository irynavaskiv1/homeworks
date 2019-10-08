class Human:
    pass


class Man(Human):
    pass


class Woman(Human):
    pass


def Job():
    Adam = Man()
    Eva = Woman()
    return ([Adam, Eva])
