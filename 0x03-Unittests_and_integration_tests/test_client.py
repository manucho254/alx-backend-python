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
                          ):
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url,
                             TEST_DATA.get("repos_url"))

    @mock.patch("client.GithubOrgClient._public_repos_url",
        return_value=TEST_DATA,
        new_callable=PropertyMock,
    )
    def test_public_repos(self, mocK_public_repos_url):
        """Test public repos"""
        mocK_public_repos_url.return_value = "test_url"
        data = [{"name": "repo-1"}, {"name": "manucho_repo"}]
        with patch("client.get_json", return_value=data):
            client = GithubOrgClient("google")
            response = client.public_repos()
            
        mocK_public_repos_url.assert_called_once()
        self.assertEqual(response, ["repo-1", "manucho_repo"])
