import unittest
from student import Student

class TestStudent(unittest.TestCase):

    # test for Student class to instantiated it and 
    # call the full_name method on it to assert 
    # whether it returned the first_name and last_name property values separated by a space
    def test_full_name(self):
        student = Student("John", "Doe")
        self.assertEqual(student.full_name, "John Doe")
    
    # test for a function called alert_santa to change the naughty_list property to True.
    def test_alert_santa(self):
        student = Student("John", "Doe")
        student.alert_santa()
        
        self.assertTrue(student.naughty_list)


if __name__ == "__main__":
    unittest.main()

  