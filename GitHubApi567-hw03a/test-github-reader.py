import json
from github_api import list_repositories


def test_expected_result():
    result = list_repositories("Kayy07")
    assert isinstance(result, list)

    for repo in result:
        assert "name" in repo
        assert "commits" in repo
        assert isinstance(repo["commits"], int)
    


def test_no_repositories():
    result = list_repositories("")
    assert result == []


def test_commit_count_one_repository():
    result = list_repositories("Kayy07")

    # assert len(result) > 0

    repo = result[0]
    assert repo["commits"] >= 0