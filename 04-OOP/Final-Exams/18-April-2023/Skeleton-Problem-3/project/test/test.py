from project.robot import Robot

from unittest import TestCase, main


class TestRobot(TestCase):
    def setUp(self) -> None:
        self.robot = Robot('1', 'Education', 50, 66.9)
        self.robot2 = Robot('2', 'Military', 100, 250)
        self.robot3 = Robot('3', 'Education', 100, 250)
        self.allowed_categories = ['Military', 'Education', 'Entertainment', 'Humanoids']
        self.price_increment = 1.5

    def test_robot_init(self):
        self.assertEqual('1', self.robot.robot_id)
        self.assertEqual('Education', self.robot.category)
        self.assertEqual(50, self.robot.available_capacity)
        self.assertEqual(66.9, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_robot_category_not_in_set_category_raises(self):
        self.assertEqual(self.allowed_categories, self.robot.ALLOWED_CATEGORIES)
        with self.assertRaises(ValueError) as ex:
            self.robot.category = 'Animal'

        self.assertEqual(f"Category should be one of '{self.allowed_categories}'",
                         str(ex.exception))

        self.assertEqual(self.allowed_categories, self.robot.ALLOWED_CATEGORIES)

    def test_robot_set_price_lower_than_zero_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.robot.price = -100

        self.assertEqual("Price cannot be negative!", str(ex.exception))

    def test_upgrade_hardware_component_in_hardware_upgrades(self):
        self.assertEqual([], self.robot.hardware_upgrades)
        self.robot.hardware_upgrades.append("Upgrade1")
        self.assertEqual(["Upgrade1"], self.robot.hardware_upgrades)

        result = self.robot.upgrade("Upgrade1", 100)

        self.assertEqual("Robot 1 was not upgraded.", result)
        self.assertEqual(["Upgrade1"], self.robot.hardware_upgrades)

    def test_upgrade_hardware_component_not_in_hardware_upgrades(self):
        self.assertEqual([], self.robot.hardware_upgrades)
        expected_new_price = self.robot.price + 100 * self.price_increment

        result = self.robot.upgrade("Upgrade1", 100)

        self.assertEqual(["Upgrade1"], self.robot.hardware_upgrades)
        self.assertEqual(expected_new_price, self.robot.price)
        self.assertEqual("Robot 1 was upgraded with Upgrade1.", result)

        # Second Upgrade
        expected_new_price = self.robot.price + 100 * self.price_increment

        result = self.robot.upgrade("Upgrade2", 100)

        self.assertEqual(["Upgrade1", "Upgrade2"], self.robot.hardware_upgrades)
        self.assertEqual(expected_new_price, self.robot.price)
        self.assertEqual("Robot 1 was upgraded with Upgrade2.", result)

    def test_robot_update_there_are_no_software_updates_raise(self):
        self.assertEqual(self.robot.software_updates, [])
        self.assertEqual(self.robot.available_capacity, 50)

        result = self.robot.update(15, 200)

        self.assertEqual("Robot 1 was not updated.", result)

        self.assertEqual(self.robot.software_updates, [])
        self.assertEqual(self.robot.available_capacity, 50)

    def test_has_software_updates_but_the_version_is_less_than_or_equal_than_max(self):
        # Less than
        self.assertEqual(self.robot.software_updates, [])
        self.robot.software_updates.append(2.3)
        self.robot.software_updates.append(3.1)
        self.assertEqual(self.robot.software_updates, [2.3, 3.1])

        result = self.robot.update(2.2, 30)

        self.assertEqual("Robot 1 was not updated.", result)
        self.assertEqual(self.robot.software_updates, [2.3, 3.1])

        # Equal version
        result = self.robot.update(3.1, 30)

        self.assertEqual("Robot 1 was not updated.", result)
        self.assertEqual(self.robot.software_updates, [2.3, 3.1])

    def test_valid_data_for_update(self):
        self.assertEqual(self.robot.software_updates, [])
        self.assertEqual(self.robot.available_capacity, 50)
        self.robot.software_updates.append(2.3)
        self.assertEqual(self.robot.software_updates, [2.3])

        result = self.robot.update(3.1, 20)

        self.assertEqual(self.robot.software_updates, [2.3, 3.1])
        self.assertEqual(self.robot.available_capacity, 30)
        self.assertEqual("Robot 1 was updated to version 3.1.", result)

    def test_compare_two_robots__the_second_one_with_greater_price(self):
        self.assertEqual(self.robot.price, 66.9)
        self.assertEqual(self.robot2.price, 250)

        result = self.robot2.__gt__(self.robot)
        self.assertEqual("Robot with ID 2 is more expensive than Robot with ID 1.",
                         result)
        self.assertEqual(self.robot.price, 66.9)
        self.assertEqual(self.robot2.price, 250)

    def test_compare_two_robots_with_equal_price(self):
        self.assertEqual(self.robot2.price, 250)
        self.assertEqual(self.robot3.price, 250)

        result = self.robot2.__gt__(self.robot3)
        self.assertEqual("Robot with ID 2 costs equal to Robot with ID 3.",
                         result)
        self.assertEqual(self.robot2.price, 250)
        self.assertEqual(self.robot3.price, 250)

    def test_compare_two_robots_the_second_one_with_lower_price(self):
        self.assertEqual(self.robot.price, 66.9)
        self.assertEqual(self.robot2.price, 250)

        result = self.robot.__gt__(self.robot2)
        self.assertEqual("Robot with ID 1 is cheaper than Robot with ID 2.",
                         result)
        self.assertEqual(self.robot.price, 66.9)
        self.assertEqual(self.robot2.price, 250)


if __name__ == '__main__':
    main()
