import json
from unittest.mock import patch, Mock
from github_api import list_repositories

@patch("github_api.requests.get")
def test_expected_result(mock_get):
    repos = Mock()
    repos.text = json.dumps([
        {"name": "Triangle567"},
        {"name": "Square567"}
    ])

    triangle = Mock()
    triangle.text = json.dumps([
        {"foo": "abc"},
        {"bar": "def"}
    ])

    square = Mock()
    square.text = json.dumps([
        {"sha": "ghi"}
    ])

    mock_get.side_effect = [repos, triangle, square]

    result = list_repositories("richkempinski")

    expected = [
        {"name": "Triangle567", "commits": 2},
        {"name": "Square567", "commits": 1}
    ]

    assert result == expected


@patch("github_api.requests.get")
def test_no_repositories(mock_get):
    response = Mock()
    response.text = json.dumps([])
    mock_get.return_value = response

    result = list_repositories("richkempinski")

    assert result == []


@patch("github_api.requests.get")
def test_commit_count_one_repository(mock_get):
    repos = Mock()
    repos.text = json.dumps([
        {"name": "Triangle567"}
    ])

    # Mock three commits
    commits = Mock()
    commits.text = json.dumps([
        {"foo": "abc"},
        {"bar": "def"},
        {"sha": "ghi"}
    ])

    mock_get.side_effect = [repos, commits]

    result = list_repositories("richkempinski")

    expected = [
        {"name": "Triangle567", "commits": 3}
    ]

    assert result == expected
