#!/usr/bin/env python3
""" Parameterize and patch as decorators """


from parameterized import parameterized
from client import GithubOrgClient

import unittest
from unittest import mock
from unittest.mock import PropertyMock, patch


class TestGithubOrgClient(unittest.TestCase):
    """Test github org client"""

    @parameterized.expand([("google"), ("abc")])
    @mock.patch("requests.get")
    def test_org(self, name, mock_getter):
        """test org method"""
        client = GithubOrgClient(name)
        client.org
        mock_getter.assert_called_once()

    def test_public_repos_url(self):
        """Mocking a property"""
        data = {
            "repos_url": "https://api.github.com/users/google/repos",
        }
        with patch.object(
            GithubOrgClient, "org", return_value=data, new_callable=PropertyMock
        ) as mock_public_repos_url:
            client = GithubOrgClient("google")
            self.assertEqual(
                client._public_repos_url, "https://api.github.com/users/google/repos"
            )
