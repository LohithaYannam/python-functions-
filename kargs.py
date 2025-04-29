#function with keyword args
def info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
info(name='jk',age=26,city="busan")
