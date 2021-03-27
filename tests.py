import unittest 
import subprocess
from problem1 import print_depth,sort_output
from problem2 import print_depth_object

class TestProblemOne(unittest.TestCase):
    def setUp(self):
            self.empty_dict = {}
            self.multi_depth_dict = {"parent1":{"child1":5,"child2":8},"parent2":{"child3":2}}
            self.invalid_data = ['key1','key2']
            self.unsorted_dict = {'key1':1,'key5':4,'key3':2,'key4':3,'key2':2}

    def test_zero_depth(self):
        self.assertEqual(print_depth(self.empty_dict), "")

    def test_multi_depth(self):
        self.assertEqual(print_depth(self.multi_depth_dict), "parent1 1\nparent2 1\nchild1 2\nchild2 2\nchild3 2\n")

    def test_invalid_data(self):
        self.assertEqual(print_depth(self.invalid_data), "")

    def test_sort_output(self):
        self.assertEqual(sort_output(self.unsorted_dict), "key1 1\nkey2 2\nkey3 2\nkey4 3\nkey5 4\n")

class TestProblemTwo(unittest.TestCase):  
    def setUp(self):
        class Person(object):
            def __init__(self, first_name, last_name, father):
                self.first_name = first_name
                self.last_name = last_name
                self.father = father
        person_a = Person("User", "1", None)
        person_b = Person("User", "2", person_a)

    def test_object_depth(self):
        self.assertEqual()  

if __name__=='__main__':
    unittest.main()