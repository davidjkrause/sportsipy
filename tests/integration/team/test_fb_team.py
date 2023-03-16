from mock import patch
from os import path
from sportsipy.fb.team import Team


def read_file(filename):
    filepath = path.join(path.dirname(__file__), 'fb_stats', filename)
    return open('%s' % filepath, 'r', encoding='utf8').read()


def mock_pyquery(url, timeout=None):
    class MockPQ:
        def __init__(self, html_contents):
            self.status_code = 200
            self.html_contents = html_contents
            self.text = html_contents

    contents = read_file('tottenham-hotspur-2019-2020.html')
    return MockPQ(contents)


class TestFBTeam:
    def setup_method(self):
        self.results = {
            'name': 'Tottenham Hotspur',
            'short_name': 'Tottenham',
            'season': '2019-2020',
            'record': '16-11-11',
            'points': 59,
            'position': 6,
            'league': 'Premier League',
            'home_record': '12-3-4',
            'home_wins': 12,
            'home_draws': 3,
            'home_losses': 4,
            'home_games': 19,
            'home_points': 39,
            'away_record': '4-8-7',
            'away_wins': 4,
            'away_draws': 8,
            'away_losses': 7,
            'away_games': 19,
            'away_points': 20,
            'goals_scored': 61,
            'goals_against': 47,
            'goal_difference': 14,
            'expected_goals': 47.9,
            'expected_goals_against': 54.2,
            'expected_goal_difference': -6.3,
            'manager': None,
            'country': 'England',
            'gender': 'Male'
        }

    @patch('requests.get', side_effect=mock_pyquery)
    def test_fb_team_returns_correct_attributes(self, *args, **kwargs):
        tottenham = Team('Tottenham Hotspur')

        for attribute, value in self.results.items():
            assert getattr(tottenham, attribute) == value

    @patch('requests.get', side_effect=mock_pyquery)
    def test_team_name(self, *args, **kwargs):
        team = Team('Tottenham Hotspur')

        assert team.__repr__() == 'Tottenham Hotspur (361ca564) - 2019-2020'
