from project.senior_student import SeniorStudent

from unittest import TestCase, main


class TestSeniorStudent(TestCase):

    def setUp(self) -> None:
        self.student = SeniorStudent('1234', 'Pesho', 4.2)
        self.another_studen = SeniorStudent('6789', 'Ivan', 4.2)

    def test_student_init(self):
        self.assertEqual('1234', self.student.student_id)
        self.assertEqual('Pesho', self.student.name)
        self.assertEqual(4.2, self.student.student_gpa)
        self.assertEqual(set(), self.student.colleges)

    def test_set_student_id_not_long_enough_raise(self):
        with self.assertRaises(Exception) as ex:
            self.student.student_id = '1 2'

        self.assertEqual("Student ID must be at least 4 digits long!", str(ex.exception))

    def test_set_student_name_null_or_empty_raise(self):
        with self.assertRaises(Exception) as ex:
            self.student.name = ''

        self.assertEqual("Student name cannot be null or empty!", str(ex.exception))

    def test_set_student_gpa_less_or_equal_to_one_raise(self):
        # Test if it's less than 1
        with self.assertRaises(Exception) as ex:
            self.student.student_gpa = -1

        self.assertEqual("Student GPA must be more than 1.0!", str(ex.exception))

        # Test if it's equal to 1
        with self.assertRaises(Exception) as ex:
            self.student.student_gpa = 1

        self.assertEqual("Student GPA must be more than 1.0!", str(ex.exception))

    def test_apply_for_college_not_enough_gpa(self):
        self.assertEqual(4.2, self.student.student_gpa)

        result = self.student.apply_to_college(5, "Oxford")

        self.assertEqual(4.2, self.student.student_gpa)
        self.assertEqual('Application failed!', result)

    def test_apply_for_college_enough_gpa(self):
        # Equal gpa needed
        self.assertEqual(4.2, self.student.student_gpa)

        result = self.student.apply_to_college(4.2, 'Reading')

        self.assertEqual(4.2, self.student.student_gpa)
        self.assertEqual({'READING'}, self.student.colleges)
        self.assertEqual("Pesho successfully applied to Reading.", result)

        # Less gpa needed
        self.assertEqual(4.2, self.student.student_gpa)

        result = self.student.apply_to_college(4.1, 'Reading')

        self.assertEqual(4.2, self.student.student_gpa)
        self.assertEqual({'READING'}, self.student.colleges)
        self.assertEqual("Pesho successfully applied to Reading.", result)

    def test_update_gpa_not_changing_it_when_is_less_than_or_equal_to_one(self):
        # Equal to 1
        self.assertEqual(4.2, self.student.student_gpa)

        result = self.student.update_gpa(1)

        self.assertEqual(4.2, self.student.student_gpa)
        self.assertEqual('The GPA has not been changed!', result)

        # Less than 1
        self.assertEqual(4.2, self.student.student_gpa)

        result = self.student.update_gpa(-2)

        self.assertEqual(4.2, self.student.student_gpa)
        self.assertEqual('The GPA has not been changed!', result)

    def test_update_gpa_when_greater_than_one(self):
        self.assertEqual(4.2, self.student.student_gpa)

        result = self.student.update_gpa(1.1)

        self.assertEqual(1.1, self.student.student_gpa)
        self.assertEqual('Student GPA was successfully updated.', result)

    def test_compare_students_gpa_if_they_are_equal(self):
        self.assertEqual(4.2, self.student.student_gpa)
        self.assertEqual(4.2, self.another_studen.student_gpa)

        result = self.student.__eq__(self.another_studen)

        self.assertTrue(result)
        self.assertEqual(4.2, self.student.student_gpa)
        self.assertEqual(4.2, self.another_studen.student_gpa)


if __name__ == "__main__":
    main()
