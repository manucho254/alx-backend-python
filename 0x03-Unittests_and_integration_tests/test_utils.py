#!/usr/bin/env python3
""" Parameterize a unit test """

from parameterized import parameterized
import utils
import unittest
from unittest import mock
import requests


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
