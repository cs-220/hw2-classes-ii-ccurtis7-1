from graphics import *

class Face:
    def __init__(self, win):
        c = Point(200, 200)
        r = 120
        self.win = win
        self.face = face = Circle(c, r)
        face.setFill('yellow')
        face.setWidth(6)
        face.draw(win)

        m1, m2 = Point(c.getX() - 0.5*r, c.getY() + 0.5*r), Point(c.getX() + 0.5*r, c.getY() + 0.5*r)
        self.mouth = mouth = Line(m1, m2)
        mouth.setWidth(8)
        mouth.draw(win)

        e1, e2 = Point(c.getX() - 0.4*r, c.getY() - 0.4*r), Point(c.getX() + 0.4*r, c.getY() - 0.4*r)
        l, w = 20, 10
        self.eye1 = eye1 = Oval(Point(e1.getX() - w, e1.getY() - l), Point(e1.getX() + w, e1.getY() + l))
        eye1.setFill('black')
        self.eye2 = eye2 = Oval(Point(e2.getX() - w, e2.getY() - l), Point(e2.getX() + w, e2.getY() + l))
        eye2.setFill('black')
        eye1.draw(win), eye2.draw(win)

def main():
    win = GraphWin('Make a face!', 400, 400)
    myFace = Face(win)
    p = win.getMouse()

if __name__ == '__main__':
    main()
