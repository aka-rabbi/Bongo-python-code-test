import unittest 
import json
from problem1 import print_depth, sort_output
from problem2 import print_depth_object
from problem3 import lca

class Tree:
    def __init__(self, x):
        self.val = x
        self.left = None 
        self.right = None 

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

    def test_with_json_object(self):
        with open('test1.json') as f:
            data = json.loads(f.read())

        func_output = print_depth(data)

        with open('check1.txt') as f:
            check_output = f.read()

        self.assertTrue( check_output==func_output )

class TestProblemTwo(unittest.TestCase):  
    def setUp(self):
        class Person(object):
            def __init__(self, first_name, last_name, father):
                self.first_name = first_name
                self.last_name = last_name
                self.father = father
        person_a = Person("User", "1", None)
        person_b = Person("User", "2", person_a)
        self.test_dict = {"key1":{"key1":5,"key2":8},"key2":{"user":person_b}}
        self.nested_with_repeat_key_dict = {"key1":{"key1":1,"key2":{"key1":{"key1":1, "user":person_a}}}}

    def test_object_depth(self):
        self.assertEqual(print_depth_object(self.test_dict), "key1 1\nkey2 1\nkey1 2\nkey2 2\nuser 2\nfather 3\nfirst_name 3\nlast_name 3\nfather 4\nfirst_name 4\nlast_name 4\n")
    
    def test_nested_dict_with_repeat_key(self):
        self.assertEqual(print_depth_object(self.nested_with_repeat_key_dict), "key1 1\nkey1 2\nkey2 2\nkey1 3\nkey1 4\nuser 4\nfather 5\nfirst_name 5\nlast_name 5\n")

class TestProblemThree(unittest.TestCase):
    def setUp(self):
        self.root = Tree(5) 
        self.root.left = Tree(3)
        self.root.right = Tree(8)
        self.root.left.left = Tree(1)
        self.root.left.right = Tree(6)
        self.root.right.left = Tree(4)
        self.root.right.left = Tree(9)    

    def test_child_nodes_from_left_and_right(self):
        self.assertEqual( lca(self.root, 1, 9).val, 5 ) 

    def test_ancestor_of_itself(self):
        self.assertEqual( lca(self.root, 8, 4).val, 8 )

    def test_no_root(self):
        self.assertEqual( lca(None, 8, 4), None )

    def test_root_as_node(self):
        self.assertEqual( lca(self.root, 8, 5).val, 5 )


if __name__=='__main__':
    unittest.main()