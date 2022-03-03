from unittest.mock import Mock, patch
from get_commits import get_commits

@patch('get_commits.requests.get')
def test_getting_commits(mock_get):
    commits = '[{"name":"name1"},{"name":"name2"}]'

    mock_get.return_value = commits

    response = get_commits()