class Logger:
    def __init__(self):
        print("Logger object created.")

    def __del__(self):
        print("Logger object destroyed.")

log1=Logger()        # it creates the object
del log1             # it destoryed the object

log2=Logger()
del log2


