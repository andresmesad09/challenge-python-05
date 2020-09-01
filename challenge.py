import math


def square_area(side):
    """Returns the area of a square"""
    # You have to code here
    # REMEMBER: Tests first!!!
    area = side * side
    return area


def rectangle_area(base, height):
    """Returns the area of a rectangle"""
    # You have to code here
    # REMEMBER: Tests first!!!
    area = base * height
    return area


def triangle_area(base, height):
    """Returns the area of a triangle"""
    # You have to code here
    # REMEMBER: Tests first!!!
    area = (base * height) / 2
    return area


def rhombus_area(diagonal_1, diagonal_2):
    """Returns the area of a rhombus"""
    # You have to code here
    # REMEMBER: Tests first!!!
    area = (diagonal_1 * diagonal_2) / 2
    return area


def trapezoid_area(base_minor, base_major, height):
    """Returns the area of a trapezoid"""
    # You have to code here
    # REMEMBER: Tests first!!!
    area = ((base_minor + base_major) / 2) * height
    return area


def regular_polygon_area(perimeter, apothem):
    """Returns the area of a regular polygon"""
    # You have to code here
    # REMEMBER: Tests first!!!
    area = (perimeter * apothem) / 2
    return area


def circumference_area(radius):
    """Returns the area of a circumference"""
    # You have to code here
    # REMEMBER: Tests first!!!
    # Use math.pi for π value
    area = math.pi * (radius ** 2)
    return area


if __name__ == '__main__':
    import unittest

    class GeometrySuite(unittest.TestCase):

        def setUp(self):
            # Initialize the needed values for the tests
            # Squares <- side: area
            self.squares = {
                2: 4,
                3: 9,
                4: 16,
                5: 25
            }
            #Rectangles <- area: [base, height]
            self.rectangles = {
                20: [4, 5],
                28: [7, 4],
                32: [8, 4],
                100: [10, 10],
            }
            # Triangles <- area: [base, height]
            self.triangles = {
                10: [4, 5],
                14: [7, 4],
                16: [8, 4],
                50: [10, 10],
            }
            #Rhombus: <- area: [diagonal1, diagonal2]
            self.rhombuses = {
                7.5: [5, 3],
                14: [7, 4],
                12: [6, 4],
                24: [8, 6],
            }
            #Trapezoids
            self.trapezoids = {
                36: [6, 12, 4],
                105: [12, 18, 7],
                60: [7, 13, 6],
                63: [7, 14, 6],
            }
            #Regular poygons
            self.regular_polygons = {
                23.4: [18, 2.6],
                47.25: [27, 3.5],
                35.1: [27, 2.6],
                7.2: [9, 1.6],
            }
            #Circumferences
            self.circumferences = {
                3: 28.274,
                6: 113.097,
                9: 254.469,
                12: 452.3893,
            }

        def test_square_area(self):
            # Make this test first...
            for side, area in self.squares.items():
                self.assertTrue(side > 0), 'El valor de un lado debe ser positivo'
                self.assertAlmostEqual(area, square_area(side), places=3), 'Las áreas no son iguales'
            

        def test_rectangle_area(self):
            # Make this test first...
            for area, dim_list in self.rectangles.items():
                self.assertTrue(dim_list[0] > 0 and dim_list[1] > 0), 'Base y altura deben ser mayores a 0'
                self.assertAlmostEqual(area, rectangle_area(dim_list[0], dim_list[1]), places=3), 'Las áreas no son iguales'
                
        def test_triangle_area(self):
            # Make this test first...
            for area, dim_list in self.triangles.items():
                self.assertTrue(dim_list[0] > 0 and dim_list[1] > 0), 'Base y altura deben ser mayores a 0'
                self.assertAlmostEqual(area, triangle_area(dim_list[0], dim_list[1]), places=3), 'Las áreas no son iguales'
                
                
        def test_rhombus_area(self):
            # Make this test first...
            for area, dim_list in self.rhombuses.items():
                self.assertTrue(dim_list[0] > 0 and dim_list[1] > 0), 'Las diagonales deben ser mayores a cero'
                self.assertAlmostEqual(area, rhombus_area(dim_list[0], dim_list[1]), places=3), 'Las áreas no son iguales'
                
                
        def test_trapezoid_area(self):
            # Make this test first...
            for area, dim_list in self.trapezoids.items():
                self.assertTrue(dim_list[0] > 0 and dim_list[1] > 0 and dim_list[2]), 'Bases (mayor y menor) y altura deben ser mayores a cero'
                self.assertAlmostEqual(area, trapezoid_area(dim_list[0], dim_list[1], dim_list[2]), places=3), 'Las áreas no son iguales'

        def test_regular_polygon_area(self):
            # Make this test first...
            for area, dim_list in self.rhombuses.items():
                self.assertTrue(dim_list[0] > 0 and dim_list[1] > 0), 'Las diagonales deben ser mayores a cero'
                self.assertAlmostEqual(area, rhombus_area(dim_list[0], dim_list[1]), places=3), 'Las áreas no son iguales'

        def test_circumference_area(self):
            # Make this test first...
            for radius, area in self.circumferences.items():
                self.assertTrue(radius > 0), 'El radio debe ser mayor a cero'
                self.assertAlmostEqual(area, circumference_area(radius), places=3), 'Las áreas no son iguales'

        def tearDown(self):
            # Delete the needed values for the tests
            del(self.squares)
            del(self.rectangles)
            del(self.triangles)
            del(self.rhombuses)
            del(self.trapezoids)
            del(self.regular_polygons)
            del(self.circumferences)

    unittest.main()
