from engine import Engine
from utils import Vec3


class GameObject:


    def __init__(self) -> None:
        self.position = Vec3(0, 0, 0)
        self.rotation = Vec3(0, 0, 0)



    def forward(self):
        return Engine.rotate(Vec3(0, 0, 1), Vec3.mul(self.rotation, -1))


    def backward(self):
        return Vec3.mul(self.forward(), -1)


    def right(self):
        return Engine.rotate(Vec3(1, 0, 0), Vec3.mul(self.rotation, -1))

    def left(self):
        return Vec3.mul(self.right(), -1)


    def up(self):
        return Engine.rotate(Vec3(0, 1, 0), Vec3.mul(self.rotation, -1))

    def down(self):
        return Vec3.mul(self.up(), -1)
