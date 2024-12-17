from project.furniture import Furniture

from unittest import TestCase, main


class TestFurniture(TestCase):

    def setUp(self) -> None:
        self.chair = Furniture("Videnov", 78.63, (10, 20, 50))

    def test_furniture_init(self):
        self.assertEqual("Videnov", self.chair.model)
        self.assertEqual(78.63, self.chair.price)
        self.assertEqual((10, 20, 50), self.chair.dimensions)
        self.assertTrue(self.chair.in_stock)
        self.assertEqual(None, self.chair.weight)

    def test_model_not_valid_name_raise(self):
        # When it is an empty string
        with self.assertRaises(ValueError) as ex:
            self.chair.model = ''

        self.assertEqual("Model must be a non-empty string with a maximum length of "
                         "50 characters.", str(ex.exception))

        # When the name is more than 50 characters
        with self.assertRaises(ValueError) as ex:
            self.chair.model = 's' * 51

        self.assertEqual("Model must be a non-empty string with a maximum length of "
                         "50 characters.", str(ex.exception))

    def test_price_lower_than_zero_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.chair.price = -200

        self.assertEqual("Price must be a non-negative number.", str(ex.exception))

    def test_not_three_dimensions_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.chair.dimensions = tuple()

        self.assertEqual("Dimensions tuple must contain 3 integers.", str(ex.exception))

    def test_negative_number_for_dimensions_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.chair.dimensions = (-2, 10, 20)

        self.assertEqual("Dimensions tuple must contain integers greater than zero.",
                         str(ex.exception))

    def test_weight_less_than_or_equal_to_zero_raise(self):
        # Less than zero
        with self.assertRaises(ValueError) as ex:
            self.chair.weight = -5

        self.assertEqual("Weight must be greater than zero.", str(ex.exception))

        # Equal to zero
        with self.assertRaises(ValueError) as ex:
            self.chair.weight = 0

        self.assertEqual("Weight must be greater than zero.", str(ex.exception))

    def test_availability_status(self):
        # When in stock
        self.assertTrue(self.chair.in_stock)

        result = self.chair.get_available_status()

        self.assertTrue(self.chair.in_stock)
        self.assertEqual("Model: Videnov is currently in stock.", result)

        # When not in stock
        self.assertTrue(self.chair.in_stock)
        self.chair.in_stock = False
        self.assertFalse(self.chair.in_stock)

        result = self.chair.get_available_status()

        self.assertFalse(self.chair.in_stock)
        self.assertEqual("Model: Videnov is currently unavailable.", result)

    def test_get_specifications(self):
        # If we do not have a value for the weight
        self.assertEqual(None, self.chair.weight)

        result = self.chair.get_specifications()

        self.assertEqual(None, self.chair.weight)
        self.assertEqual("Model: Videnov has the following dimensions: 10mm x 20mm x "
                         "50mm and weighs: N/A", result)

        # If we have a value for the weight
        self.assertEqual(None, self.chair.weight)
        self.chair.weight = 10

        result = self.chair.get_specifications()

        self.assertEqual(10, self.chair.weight)
        self.assertEqual("Model: Videnov has the following dimensions: 10mm x 20mm x "
                         "50mm and weighs: 10", result)


if __name__ == "__main__":
    main()
