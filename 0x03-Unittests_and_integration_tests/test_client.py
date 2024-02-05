#!/usr/bin/env python3
""" Parameterize and patch as decorators """


from parameterized import parameterized, parameterized_class
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
                          new_callable=PropertyMock):
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url,
                             TEST_DATA.get("repos_url"))

    @patch("client.GithubOrgClient._public_repos_url",
           new_callable=PropertyMock)
    def test_public_repos(self, mocK_public_repos_url):
        """Test public repos"""
        mocK_public_repos_url.return_value = "test_url"
        data = [{"name": "repo_1"}, {"name": "manucho_repo"}]

        with patch("client.get_json", return_value=data):
            client = GithubOrgClient("google")
            response = client.public_repos()

        res = ["repo_1", "manucho_repo"]
        mocK_public_repos_url.assert_called_once()
        self.assertEqual(response, res)

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(self, test_repo, license_name, expected_res):
        """test has license"""
        client = GithubOrgClient("test")
        self.assertEqual(client.has_license(test_repo, license_name),
                         expected_res)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD,
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration Test"""

    @classmethod
    def setUpClass(cls):
        """setup method"""
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.side_effect = [
            unittest.mock.Mock(json=lambda: cls.org_payload),
            unittest.mock.Mock(json=lambda: cls.repos_payload),
        ]
        cls.client = GithubOrgClient("test")

    def test_public_repos_no_license(self):
        """test public repos no license"""
        result = self.client.public_repos()
        self.assertEqual(result, self.expected_repos)

    def test_public_repos_with_license(self):
        """ test public repos with license """
        self.expected_repos = ['dagger', 'kratu',
                               'traceur-compiler', 'firmata.py']
        result = self.client.public_repos(license="apache-2.0")
        self.assertEqual(result, self.expected_repos)

    @classmethod
    def tearDownClass(cls):
        """teardown method"""
        cls.get_patcher.stop()
