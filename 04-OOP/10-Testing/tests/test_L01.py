# Create the following tests:

# •	Test if the worker is initialized with the correct name, salary, and energy
# •	Test if the worker's energy is incremented after the rest method is called
# •	Test if an error is raised if the worker tries to work with negative energy or equal
# to 0
# •	Test if the worker's money is increased by his salary correctly after the work method
# is called
# •	Test if the worker's energy is decreased after the work method is called
# •	Test if the get_info method returns the proper string with the correct values

# Do not submit in Judge

from L01_worker import Worker

# Submit in Judge
from unittest import TestCase, main


class TestWorker(TestCase):

    def test_init_worker(self):

        # Act
        w = Worker("Test", 1000, 100)

        # Assert
        self.assertEqual("Test", w.name)  # is w.name == "Test"
        self.assertEqual(1000, w.salary)
        self.assertEqual(100, w.energy)
        self.assertEqual(0, w.money)

    def test_work_worker_does_not_have_energy_raises(self):

        # Arrange
        w = Worker("Test", 1000, 0)
        self.assertEqual(0, w.energy)
        self.assertEqual(0, w.money)

        # Act
        with self.assertRaises(Exception) as ex:
            w.work()

        # Assert
        self.assertEqual('Not enough energy.', str(ex.exception)) # check the message
        self.assertEqual(0, w.energy)  # We want to assert that he doesnt get money
        self.assertEqual(0, w.money)

        # Another test, when the energy is negative
        w = Worker("Test", 1000, -1)
        self.assertEqual(-1, w.energy)
        self.assertEqual(0, w.money)

        # Act
        with self.assertRaises(Exception) as ex:
            w.work()

        # Assert
        self.assertEqual('Not enough energy.', str(ex.exception))  # check the message
        self.assertEqual(-1, w.energy)  # We want to assert that he doesn's get money
        self.assertEqual(0, w.money)

    def test_work_worker_works(self):

        # Arrange
        w = Worker("Test", 1000, 100)
        self.assertEqual(0, w.money)
        self.assertEqual(100, w.energy)

        # Act
        w.work()

        # Assert
        self.assertEqual(1000, w.money)
        self.assertEqual(99, w.energy)

        # Act - to see if it works the second time; for example to check if money is += ..
        w.work()

        # Assert
        self.assertEqual(2000, w.money)
        self.assertEqual(98, w.energy)

    def test_rest_worker_energy_increases(self):

        # Arrange
        w = Worker("Test", 1000, 100)
        self.assertEqual(100, w.energy)

        # Act
        w.rest()

        # Assert
        self.assertEqual(101, w.energy)

    def test_get_info(self):

        # Arrange
        w = Worker("Test", 1000, 100)

        # Act
        result = w.get_info()
        expected = 'Test has saved 0 money.'

        # Assert
        self.assertEqual(expected, result)

        # Try with saved money
        w.work()
        self.assertEqual(w.salary, w.money)

        # Act
        result = w.get_info()
        expected = 'Test has saved 1000 money.'

        # Assert
        self.assertEqual(expected, result)


if __name__ == 'main':
    main()  # if the file is run, run all of tests in it
