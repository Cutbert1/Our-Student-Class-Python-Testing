import unittest
from student import Student
from datetime import timedelta

class TestStudent(unittest.TestCase):

    # Run code once at the  beginning of our tests.We can’t use the setUp method as that 
    # gets called at the beginning of each test method
    @classmethod 
    def setUpClass(cls):
        print("setUpClass")

    # Destroy code or database once at the  end of our tests.We can’t use the tearDown method as that 
    # gets called at the end of each test method
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    # using setUp method to prevent repeatition of code, DRY - DO NOT REPEAT YOURSELF
    # setUp method can be used to create temporary files and folders or set up a database connection during tests
    def setUp(self):
        print("setUp")
        self.student = Student("John", "Doe")

    # tearDown method used to remove temporary files or folders or close a connection to a database
    def tearDown(self):
        print("tearDown")

    # test for Student class to instantiated it and 
    # call the full_name method on it to assert 
    # whether it returned the first_name and last_name property values separated by a space
    def test_full_name(self):
        print("test_full_name")
        self.assertEqual(self.student.full_name, "John Doe")

    # test read-only method that will return a student’s email address
    def test_email(self):
        print("test_email")
        self.assertEqual(self.student.email, "john.doe@email.com")
    
    # test for a function called test_alert_santa to change the naughty_list property to True.
    def test_alert_santa(self):
        print("test_alert_santa")
        self.student.alert_santa()
        
        self.assertTrue(self.student.naughty_list)

    # test a function called test_apply_extention offered to student to help them finish the course
    def test_apply_extention(self):
        old_end_date = self.student.end_date
        self.student.apply_extension(5)

        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=5))
        

if __name__ == "__main__":
    unittest.main()

   
