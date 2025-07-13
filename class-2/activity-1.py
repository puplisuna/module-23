class rectangle():
    def __init__(self, w, h):
        self.width = w
        self.length = h

    def rectangle_area(self):
        return self.width * self.length

newrectangle = rectangle(12, 10)
print("dimensions of rectangle - length : %d width : %d" % (newrectangle.length, newrectangle.width))
print("area of rectangle : %d" % (newrectangle.rectangle_area()))
