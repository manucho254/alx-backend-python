#!/usr/bin/env python3
""" Parameterize a unit test """

from parameterized import parameterized
from typing import Callable
import utils
import unittest
from unittest import mock
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """class TestAccessNestedMap for testing utils access_nested_map"""

    @parameterized.expand(
        [
            (
                {"a": 1},
                ("a",),
                1,
            ),
            (
                {"a": {"b": 2}},
                ("a",),
                {"b": 2},
            ),
            (
                {"a": {"b": 2}},
                ("a", "b"),
                2,
            ),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        """test access nested map function"""
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError),
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """test access nested map invalid key"""
        with self.assertRaises(expected) as er:
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """class to test get_json"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    @mock.patch("requests.get")
    def test_get_json(self, test_url, test_payload, get_json_getter):
        """test get json"""

        get_json_getter.return_value.json.return_value = test_payload
        self.assertEqual(utils.get_json(test_url), test_payload)
        get_json_getter.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Test utils memoize method"""

    def test_memoize(self):
        """test memoize method"""

        class TestClass:
            """Test class"""

            def a_method(self) -> int:
                """a method
                Return:
                     int number 42
                """
                return 42

            @utils.memoize
            def a_property(self) -> Callable:
                """a property
                Return:
                    a callable
                """
                return self.a_method()

        with patch.object(TestClass,
                          "a_method", return_value=42) as mock_method:
            test_obj = TestClass()
            test_obj.a_property
            test_obj.a_property
            mock_method.assert_called_once()
