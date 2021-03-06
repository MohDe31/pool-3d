import pygame

from engine import Engine
from gameobject import GameObject
from camera import Camera
from triangle import Triangle
from utils import Utils

class Mesh(GameObject):

    def __init__(self, pos = [0, 0, 0], rot = [0, 0, 0]) -> None:
        super(Mesh, self).__init__(pos, rot)

        self.triangles = []

        Engine.meshes += [self]


    def get_avg_z(self):
        return sum(map(Triangle.get_avg_z, self.triangles)) / len(self.triangles)


    def draw(self, screen):

        self.calc_cs()

        for triangle in self.triangles:
            rotated_p1 = Engine.rotate_cs(triangle.points[0], self.cos, self.sin)
            rotated_p2 = Engine.rotate_cs(triangle.points[1], self.cos, self.sin)
            rotated_p3 = Engine.rotate_cs(triangle.points[2], self.cos, self.sin)
            
            translated_1 = Utils.add_vec_r(rotated_p1, self.position)
            translated_2 = Utils.add_vec_r(rotated_p2, self.position)
            translated_3 = Utils.add_vec_r(rotated_p3, self.position)

            triangle.avg_z = (translated_1[2] + translated_2[2] + translated_3[2]) / 3.0

            cen = Utils.div_r(Utils.add_vec_r(Utils.add_vec_r(translated_1, translated_2), translated_3), 3)

            cam_ = Utils.sub_vec_r(cen, Camera.main.position)

            norm = Engine.calc_normal(translated_1, translated_2, translated_3)

            v_ = Utils.dot(norm, cam_)
            
            # _normal_line_start = Camera.main.world_to_screen_point(cen)
            # _normal_line_end = Camera.main.world_to_screen_point(Utils.add_vec_r(cen, norm))
            
            if 0 or v_ < 0:
                # pygame.draw.line(screen, (0, 255, 0), _normal_line_start, _normal_line_end, 3)
                
                uv1 = Camera.main.world_to_screen_point(translated_1)
                uv2 = Camera.main.world_to_screen_point(translated_2)
                uv3 = Camera.main.world_to_screen_point(translated_3)

                # norm_c = [*map(abs,Vec3.mul(norm, 255).values()),]
                
                norm_c = [* map(abs, Utils.mul_r(norm, 255)) ,]

                # pygame.draw.polygon(screen, norm_c, (uv1, uv2, uv3))
                pygame.draw.line(screen, norm_c, uv1, uv3, 3)
                pygame.draw.line(screen, norm_c, uv1, uv2, 3)
                pygame.draw.line(screen, norm_c, uv3, uv2, 3)
            