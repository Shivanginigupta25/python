class Demo:
    def __del__(self):
        print("Object destroyed")

d = Demo()   # object created
del d        # object deleted manually
