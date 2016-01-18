import unittest
import link_components

# Two test case examples for one of our components
class oxygen_concentrator_test(unittest.TestCase):
  O2 = link_components.oxygen_concentrator

  def test_dimensions(self):

    d = {"W": 18.375, "H": 26.375, "D": 14.375}
    """Dimensions should match d"""
    self.assertEqual(O2.dimensions, d, 
                     'incorrect dimensions set for oxygen_concentrator')

  def test_voltage(self):

    v = (120, "AC")
    """Input Voltage should match v"""
    self.assertEqual(O2.input_voltage, v,
                     'incorrect voltage set for oxygen_concentrator')

if __name__ == '__main__':
      unittest.main()
