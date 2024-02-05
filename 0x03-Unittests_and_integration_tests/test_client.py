#!/usr/bin/env python3
""" Parameterize and patch as decorators """


from parameterized import parameterized
from client import GithubOrgClient

import unittest
from unittest import mock
from unittest.mock import PropertyMock, patch
from fixtures import TEST_PAYLOAD


TEST_DATA = {
    "repos_url": "https://api.github.com/users/google/repos",
}


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
        with patch.object(GithubOrgClient, "org",
                          return_value=TEST_DATA,
                          new_callable=PropertyMock
                          ) as mock_public_repos_url:
            client = GithubOrgClient("google")
            self.assertEqual(
                client._public_repos_url, TEST_DATA.get("repos_url")
            )

    @mock.patch("requests.get")
    def test_public_repos(self, get_json_getter):
        """Test public repos"""

        data = TEST_PAYLOAD[0][1]
        # get_json response return value
        get_json_getter.return_value.json.return_value = data
        with patch.object(
            GithubOrgClient,
            "_public_repos_url",
            return_value=data,
            new_callable=PropertyMock,
        ) as mock_public_repos_url:
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, data)
            expected_public_repos = [
                "episodes.dart",
                "cpp-netlib",
                "dagger",
                "ios-webkit-debug-proxy",
                "google.github.io",
                "kratu",
                "build-debian-cloud",
                "traceur-compiler",
                "firmata.py",
            ]
            self.assertEqual(client.public_repos(), expected_public_repos)

        get_json_getter.assert_called_once()
