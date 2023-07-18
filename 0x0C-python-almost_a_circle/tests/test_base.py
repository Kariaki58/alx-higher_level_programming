from __future__ import print_function
import unittest
from models.base import Base

class TestBaseClass(unittest.TestCase):
    def testNone(self):
        t1 = Base()
        self.assertEqual(t1.id, 1)

    def test_string(self):
        t1 = Base("hello")
        self.assertEqual(t1.id, "hello")
    
    def test_multiple_instance(self):
        Base()
        Base()
        Base()
        t3 = Base(4)
        self.assertEqual(t3.id, 4)
    
    def test_public_vaiable(self):
        t1 = Base(12)
        t1.id = 20
        self.assertTrue(t1.id == 20)
    
    def test_private_cls(self):
        t1 = Base(14)
        with self.assertRaises(AttributeError):
            print(t1.__nb_objects)
    
    def test_base_dictionary(self):
        t1 = Base({"1": 1, "2": 2, "3": 3})
        self.assertEqual(t1.id, {"1": 1, "2": 2, "3": 3})
    
    def test_base_list(self):
        self.assertEqual(Base([1, 2, 3, 4]).id, [1, 2, 3, 4])
    
    def test_base_tuple(self):
        self.assertEqual(Base((1, 2)).id, (1, 2))
    
    def test_base_float(self):
        self.assertEqual(Base(10.32).id, 10.32)
    
    def test_base_type(self):
        self.assertTrue(type(Base(5).id) == int)
    
    def test_base_float_inf(self):
        self.assertTrue(Base(float('inf')).id, float('inf'))

    def test_json_string(self):
        t1 = Base(None)
        t2 = Base(None)
        self.assertTrue(t1.id == (t2.id - 1))

if __name__ == "__main__":
    unittest.main()
