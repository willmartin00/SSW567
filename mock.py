from unittest.mock import Mock, patch
from get_commits import get_commits

@patch('get_commits.requests.get')
def test_getting_commits(mock_get):
    commits = '[{"name":"name1"},{"name":"name2"}]'

    mock_get.return_value = commits

@patch('get_commits.input')
def test_getting_input(mock_get):
    mock_get.return_value = "willmartin00"