import CustomerParse
import unittest
import json

class TestCustomerMethods(unittest.TestCase):
    def setUp(self):
        self.test_customer1 = CustomerParse.Customer(json.loads('{ "latitude": "35.92893", "user_id": 1, "name": "Alice Cahill", "longitude": "-120.27699" }'))
        self.test_customer2 = CustomerParse.Customer(json.loads('{ "latitude": "37.788802", "user_id": 1, "name": "Alice Cahill", "longitude": "-122.4025067" }'))
        print(self.test_customer2)

    def test_calc_distance(self):
        #self.assertEqual(CustomerParse.Customer.calc_distance(test_customer1, 37.788802,-122.4025067), xx, "incorrect distance calcualtion")
        self.assertEqual(CustomerParse.Customer.calc_distance(self.test_customer2, 37.788802, -122.4025067), 0.0, "incorrect distance calculation")

class TestPartyMethods(unittest.TestCase):
    def test_determine_invites(self):
        #TODO: finish test
    def generate_list(self):
        #TODO: finish test

"""Additional Testing
- Ensure that Data is "good" (not null, contains correct fields, no null data fields, in range coordinates)
- Test with other edge case data (i.e. Customer location = Office Location(as in CustomerData2.txt), location at the poles, coordinates out of range)

"""

if __name__ == '__main__':
    unittest.main()

