from project.gallery import Gallery

from unittest import TestCase, main


class TestGallery(TestCase):

    def setUp(self) -> None:
        self.gallery = Gallery("National", "Sofia", 123.4, True)

    def test_gallery_init(self):
        self.assertEqual("National", self.gallery.gallery_name)
        self.assertEqual("Sofia", self.gallery.city)
        self.assertEqual(123.4, self.gallery.area_sq_m)
        self.assertTrue(self.gallery.open_to_public)
        self.assertEqual({}, self.gallery.exhibitions)

    def test_name_not_only_letters_and_digits_raise(self):
        self.assertEqual("National", self.gallery.gallery_name)

        with self.assertRaises(ValueError) as ex:
            self.gallery.gallery_name = " National@"

        self.assertEqual("National", self.gallery.gallery_name)
        self.assertEqual("Gallery name can contain letters and digits only!",
                         str(ex.exception))

    def test_city_not_starting_with_letter_raise(self):
        self.assertEqual("Sofia", self.gallery.city)

        with self.assertRaises(ValueError) as ex:
            self.gallery.city = "1Sofia"

        self.assertEqual("Sofia", self.gallery.city)
        self.assertEqual("City name must start with a letter!", str(ex.exception))

    def test_area_less_than_or_equal_to_zero_raise(self):
        # Less than zero
        self.assertEqual(123.4, self.gallery.area_sq_m)

        with self.assertRaises(ValueError) as ex:
            self.gallery.area_sq_m = -123.4

        self.assertEqual(123.4, self.gallery.area_sq_m)
        self.assertEqual("Gallery area must be a positive number!", str(ex.exception))

        # Equal to zero
        self.assertEqual(123.4, self.gallery.area_sq_m)

        with self.assertRaises(ValueError) as ex:
            self.gallery.area_sq_m = 0

        self.assertEqual(123.4, self.gallery.area_sq_m)
        self.assertEqual("Gallery area must be a positive number!", str(ex.exception))

    def test_add_exhibition_already_existing_raise(self):
        self.assertEqual({}, self.gallery.exhibitions)
        self.gallery.exhibitions["Christmas"] = 1950
        self.assertEqual({"Christmas": 1950}, self.gallery.exhibitions)

        result = self.gallery.add_exhibition("Christmas", 1950)

        self.assertEqual({"Christmas": 1950}, self.gallery.exhibitions)
        self.assertEqual('Exhibition "Christmas" already exists.', result)

    def test_add_exhibition_not_existing(self):
        self.assertEqual({}, self.gallery.exhibitions)

        result = self.gallery.add_exhibition("Christmas", 1950)

        self.assertEqual({"Christmas": 1950}, self.gallery.exhibitions)
        self.assertEqual('Exhibition "Christmas" added for the year 1950.', result)

    def test_remove_exhibition_that_is_not_in_exhibitions_raise(self):
        self.assertEqual({}, self.gallery.exhibitions)

        result = self.gallery.remove_exhibition("Christmas")

        self.assertEqual({}, self.gallery.exhibitions)
        self.assertEqual('Exhibition "Christmas" not found.', result)

    def test_remove_existing_exhibition_from_exhibition(self):
        self.assertEqual({}, self.gallery.exhibitions)
        self.gallery.add_exhibition("Christmas", 1950)
        self.assertEqual({"Christmas": 1950}, self.gallery.exhibitions)

        result = self.gallery.remove_exhibition("Christmas")
        self.assertEqual({}, self.gallery.exhibitions)
        self.assertEqual('Exhibition "Christmas" removed.', result)

    def test_list_exhibition_open_to_public(self):
        self.assertTrue(self.gallery.open_to_public)
        self.assertEqual({}, self.gallery.exhibitions)

        # When there are no exhibitions
        result = self.gallery.list_exhibitions()
        self.assertEqual("", result)

        # When we have some exhibitions
        self.gallery.add_exhibition("Christmas", 1950)
        self.gallery.add_exhibition("Easter", 1980)
        self.assertEqual({"Christmas": 1950, "Easter": 1980}, self.gallery.exhibitions)

        result = self.gallery.list_exhibitions()

        self.assertEqual("Christmas: 1950\nEaster: 1980", result)

    def test_list_exhibitions_not_open_to_public(self):
        self.assertTrue(self.gallery.open_to_public)

        self.gallery.open_to_public = False
        self.assertFalse(self.gallery.open_to_public)

        result = self.gallery.list_exhibitions()

        self.assertFalse(self.gallery.open_to_public)
        self.assertEqual("Gallery National is currently closed for public! Check for "
                         "updates later on.", result)


if __name__ == "__main__":
    main()
