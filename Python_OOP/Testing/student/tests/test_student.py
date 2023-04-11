import unittest

from project.student import Student


class TestVehicle(unittest.TestCase):
    def setUp(self) -> None:
        self.test_guy = Student('Test1', {'Matematika': [2]})
        self.gosho = Student('Gosho')

    def test_init(self):
        self.assertEqual(self.test_guy.courses, {'Matematika': [2]})
        self.assertEqual(self.gosho.name, 'Gosho')
        self.assertEqual(self.gosho.courses, {})

    def test_enroll_check_courses(self):
        self.gosho.courses['Matematika'] = []
        result = self.gosho.enroll('Matematika', ['2'], '1')
        self.assertEqual(result, "Course already added. Notes have been updated.")
        self.assertEqual(self.gosho.courses['Matematika'], ['2'])

    def test_enroll_check_add_course_and_notes(self):
        self.gosho.courses['Matematika'] = []
        result = self.gosho.enroll('Risuvane', ['Mikelanjelo'], 'Y')
        self.assertEqual(result, "Course and course notes have been added.")
        self.assertEqual(self.gosho.courses['Risuvane'], ['Mikelanjelo'])

    def test_enroll_check_add_only_course(self):
        self.gosho.courses['Matematika'] = []
        result = self.gosho.enroll('Risuvane', ['Mikelanjelo'], 'Leonardo')
        self.assertEqual(result, "Course has been added.")
        self.assertEqual(self.gosho.courses['Risuvane'], [])

    def test_add_notes(self):
        self.gosho.courses['Matematika'] = []
        result = self.gosho.add_notes('Matematika', 2)
        self.assertEqual(result, "Notes have been updated")
        self.assertEqual(self.gosho.courses['Matematika'], [2])

        with self.assertRaises(Exception) as ex:
            self.gosho.add_notes('Risuvane', 2)

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course(self):
        self.gosho.courses['Matematika'] = []
        result = self.gosho.leave_course('Matematika')
        self.assertEqual(result, "Course has been removed")
        self.assertEqual(self.gosho.courses, {})

        with self.assertRaises(Exception) as ex:
            self.gosho.leave_course('Risuvane')

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))




if __name__ == '__main__':
    unittest.main()