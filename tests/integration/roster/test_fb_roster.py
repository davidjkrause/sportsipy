import mock
import pandas as pd
from flexmock import flexmock
from os import path
from pyquery import PyQuery as pq
from sportsipy.fb.roster import Roster


EXPECTED_NUM_PLAYERS = 34


def read_file(filename):
    filepath = path.join(path.dirname(__file__), 'fb', filename)
    return open('%s.html' % filepath, 'r', encoding='utf8').read()


def mock_pyquery(url, timeout=None):
    class MockPQ:
        def __init__(self, html_contents):
            self.status_code = 200
            self.html_contents = html_contents
            self.text = html_contents

    return MockPQ(read_file('tottenham-hotspur-2019-2020'))


class TestFBRoster:
    @mock.patch('requests.get', side_effect=mock_pyquery)
    def setup_method(self, *args, **kwargs):
        self.results = {
            'name': 'Harry Kane',
            'player_id': '21a66f6a',
            'nationality': 'England',
            'position': 'FW',
            'age': 26,
            'matches_played': 29,
            'starts': 29,
            'minutes': 2587,
            'goals': 18,
            'assists': 2,
            'penalty_kicks': 2,
            'penalty_kick_attempts': 2,
            'corners_in': 0,
            'corners_out': 0,
            'corners_straight': 0,
            'yellow_cards': 4,
            'red_cards': 0,
            'goals_per_90': 0.63,
            'assists_per_90': 0.07,
            'goals_and_assists_per_90': 0.70,
            'goals_non_penalty_per_90': 0.56,
            'goals_and_assists_non_penalty_per_90': 0.63,
            'expected_goals': 12.5,
            'expected_goals_non_penalty': 10.9,
            'expected_assists': 3.3,
            'expected_goals_per_90': 0.43,
            'expected_assists_per_90': 0.11,
            'expected_goals_and_assists_per_90': 0.55,
            'expected_goals_non_penalty_per_90': 0.38,
            'expected_goals_and_assists_non_penalty_per_90': 0.49,
            'own_goals': 0,
            'goals_against': None,
            'own_goals_against': None,
            'goals_against_per_90': None,
            'shots_on_target_against': None,
            'saves': None,
            'save_percentage': None,
            'wins': None,
            'draws': None,
            'losses': None,
            'clean_sheets': None,
            'clean_sheet_percentage': None,
            'penalty_kicks_attempted': None,
            'penalty_kicks_allowed': None,
            'penalty_kicks_saved': None,
            'penalty_kicks_missed': None,
            'free_kick_goals_against': None,
            'corner_kick_goals_against': None,
            'post_shot_expected_goals': None,
            'post_shot_expected_goals_per_shot': None,
            'post_shot_expected_goals_minus_allowed': None,
            'launches_completed': None,
            'launches_attempted': None,
            'launch_completion_percentage': None,
            'keeper_passes_attempted': None,
            'throws_attempted': None,
            'launch_percentage': None,
            'average_keeper_pass_length': None,
            'goal_kicks_attempted': None,
            'goal_kick_launch_percentage': None,
            'average_goal_kick_length': None,
            'opponent_cross_attempts': None,
            'opponent_cross_stops': None,
            'opponent_cross_stop_percentage': None,
            'keeper_actions_outside_penalty_area': None,
            'keeper_actions_outside_penalty_area_per_90': None,
            'average_keeper_action_outside_penalty_distance': None,
            'shots': 79,
            'shots_on_target': 35,
            'free_kick_shots': 7,
            'shots_on_target_percentage': 44.3,
            'shots_per_90': 2.75,
            'shots_on_target_per_90': 1.22,
            'goals_per_shot': 0.20,
            'goals_per_shot_on_target': 0.46,
            'expected_goals_non_penalty_per_shot': 0.14,
            'goals_minus_expected': 5.5,
            'non_penalty_minus_expected_non_penalty': 5.1,
            'assists_minus_expected': -1.3,
            'key_passes': 27,
            'passes_completed': 380,
            'passes_attempted': 581,
            'pass_completion': 65.4,
            'short_passes_completed': 221,
            'short_passes_attempted': 300,
            'short_pass_completion': 73.7,
            'medium_passes_completed': 102,
            'medium_passes_attempted': 150,
            'medium_pass_completion': 68.0,
            'long_passes_completed': 37,
            'long_passes_attempted': 76,
            'long_pass_completion': 48.7,
            'free_kick_passes': 5,
            'through_balls': 13,
            'corner_kicks': 0,
            'throw_ins': 7,
            'final_third_passes': 52,
            'penalty_area_passes': 18,
            'penalty_area_crosses': 2,
            'minutes_per_match': 89,
            'minutes_played_percentage': 75.6,
            'nineties_played': 28.7,
            'minutes_per_start': 89,
            'subs': 0,
            'minutes_per_sub': None,
            'unused_sub': 0,
            'points_per_match': 1.62,
            'goals_scored_on_pitch': 49,
            'goals_against_on_pitch': 36,
            'goal_difference_on_pitch': 13,
            'goal_difference_on_pitch_per_90': 0.45,
            'net_difference_on_pitch_per_90': 0.34,
            'expected_goals_on_pitch': 35.1,
            'expected_goals_against_on_pitch': 36.1,
            'expected_goal_difference': -0.9,
            'expected_goal_difference_per_90': -0.03,
            'net_expected_goal_difference_per_90': 0.55,
            'soft_reds': 0,
            'fouls_committed': 37,
            'fouls_drawn': 44,
            'offsides': 20,
            'crosses': 19,
            'tackles_won': 12,
            'interceptions': 6,
            'penalty_kicks_won': 1,
            'penalty_kicks_conceded': 0,
            'successful_dribbles': 28,
            'attempted_dribbles': 55,
            'dribble_success_rate': 50.9,
            'dribblers_tackled': 4,
            'dribblers_contested': 17,
            'tackle_percentage': 23.5,
            'times_dribbled_past': 13
        }
        self.keeper = {
            'name': 'Hugo Lloris',
            'player_id': '8f62b6ee',
            'nationality': 'France',
            'position': 'GK',
            'age': 32,
            'matches_played': 21,
            'starts': 21,
            'minutes': 1807,
            'goals': 0,
            'assists': 0,
            'penalty_kicks': 0,
            'penalty_kick_attempts': 0,
            'corners_in': 0,
            'corners_out': 0,
            'corners_straight': 0,
            'yellow_cards': 0,
            'red_cards': 0,
            'goals_per_90': 0.0,
            'assists_per_90': 0.0,
            'goals_and_assists_per_90': 0.0,
            'goals_non_penalty_per_90': 0.0,
            'goals_and_assists_non_penalty_per_90': 0.0,
            'expected_goals': 0.0,
            'expected_goals_non_penalty': 0.0,
            'expected_assists': 0.0,
            'expected_goals_per_90': 0.0,
            'expected_assists_per_90': 0.0,
            'expected_goals_and_assists_per_90': 0.0,
            'expected_goals_non_penalty_per_90': 0.0,
            'expected_goals_and_assists_non_penalty_per_90': 0.0,
            'own_goals': 0,
            'goals_against': 21,
            'own_goals_against': 1,
            'goals_against_per_90': 1.05,
            'shots_on_target_against': 99,
            'saves': 78,
            'save_percentage': 80.8,
            'wins': 11,
            'draws': 6,
            'losses': 4,
            'clean_sheets': 6,
            'clean_sheet_percentage': 28.6,
            'penalty_kicks_attempted': 3,
            'penalty_kicks_allowed': 2,
            'penalty_kicks_saved': 1,
            'penalty_kicks_missed': 0,
            'free_kick_goals_against': 0,
            'corner_kick_goals_against': 2,
            'post_shot_expected_goals': 30.4,
            'post_shot_expected_goals_per_shot': 0.28,
            'post_shot_expected_goals_minus_allowed': 10.4,
            'post_shot_expected_goals_minus_allowed_per_90': 0.52,
            'launches_completed': 105,
            'launches_attempted': 252,
            'launch_completion_percentage': 41.7,
            'keeper_passes_attempted': 421,
            'throws_attempted': 97,
            'launch_percentage': 42.0,
            'average_keeper_pass_length': 35.3,
            'goal_kicks_attempted': 150,
            'goal_kick_launch_percentage': 50.0,
            'average_goal_kick_length': 35.2,
            'opponent_cross_attempts': 312,
            'opponent_cross_stops': 16,
            'opponent_cross_stop_percentage': 5.1,
            'keeper_actions_outside_penalty_area': 8,
            'keeper_actions_outside_penalty_area_per_90': 0.40,
            'average_keeper_action_outside_penalty_distance': 10.2,
            'shots': 0,
            'shots_on_target': 0,
            'free_kick_shots': 0,
            'shots_on_target_percentage': None,
            'shots_per_90': 0.0,
            'shots_on_target_per_90': 0.0,
            'goals_per_shot': None,
            'goals_per_shot_on_target': None,
            'expected_goals_non_penalty_per_shot': None,
            'goals_minus_expected': 0.0,
            'non_penalty_minus_expected_non_penalty': 0.0,
            'assists_minus_expected': 0.0,
            'key_passes': 0,
            'passes_completed': 414,
            'passes_attempted': 573,
            'pass_completion': 72.3,
            'short_passes_completed': 106,
            'short_passes_attempted': 108,
            'short_pass_completion': 98.1,
            'medium_passes_completed': 153,
            'medium_passes_attempted': 155,
            'medium_pass_completion': 98.7,
            'long_passes_completed': 149,
            'long_passes_attempted': 302,
            'long_pass_completion': 49.3,
            'free_kick_passes': 35,
            'through_balls': 0,
            'corner_kicks': 0,
            'throw_ins': 0,
            'final_third_passes': 5,
            'penalty_area_passes': 0,
            'penalty_area_crosses': 0,
            'minutes_per_match': 86,
            'minutes_played_percentage': 52.8,
            'nineties_played': 20.1,
            'minutes_per_start': 86,
            'subs': 0,
            'minutes_per_sub': None,
            'unused_sub': 0,
            'points_per_match': 1.86,
            'goals_scored_on_pitch': 36,
            'goals_against_on_pitch': 21,
            'goal_difference_on_pitch': 15,
            'goal_difference_on_pitch_per_90': 0.75,
            'net_difference_on_pitch_per_90': 0.80,
            'expected_goals_on_pitch': 24.2,
            'expected_goals_against_on_pitch': 31.0,
            'expected_goal_difference': -6.7,
            'expected_goal_difference_per_90': -0.34,
            'net_expected_goal_difference_per_90': -0.36,
            'soft_reds': 0,
            'fouls_committed': 0,
            'fouls_drawn': 1,
            'offsides': 0,
            'crosses': 0,
            'tackles_won': 0,
            'interceptions': 1,
            'penalty_kicks_won': 0,
            'penalty_kicks_conceded': 0,
            'successful_dribbles': 0,
            'attempted_dribbles': 0,
            'dribble_success_rate': None,
            'dribblers_tackled': 0,
            'dribblers_contested': 0,
            'tackle_percentage': None,
            'times_dribbled_past': 0
        }

        self.roster = Roster('Tottenham Hotspur')

    def test_outfield_player_roster_returns_expected_stats(self):
        harry_kane = self.roster('Harry Kane')

        for attribute, value in self.results.items():
            assert getattr(harry_kane, attribute) == value

    def test_keeper_player_roster_returns_expected_stats(self):
        hugo_lloris = self.roster('Hugo Lloris')

        for attribute, value in self.keeper.items():
            assert getattr(hugo_lloris, attribute) == value

    def test_outfield_player_id_returns_expected_player(self):
        harry_kane = self.roster('21a66f6a')

        for attribute, value in self.results.items():
            assert getattr(harry_kane, attribute) == value

    def test_number_of_players_returns_expected(self):
        for count, player in enumerate(self.roster):
            pass

        assert count + 1 == EXPECTED_NUM_PLAYERS

    def test_roster_len_returns_expected_roster_size(self):
        assert len(self.roster) == EXPECTED_NUM_PLAYERS

    def test_fb_roster_dataframe_returns_dataframe(self):
        df = pd.DataFrame([self.results], index=['21a66f6a'])

        harry_kane = self.roster('Harry Kane')
        # Pandas doesn't natively allow comparisons of DataFrames.
        # Concatenating the two DataFrames (the one generated during the test
        # and the expected on above) and dropping duplicate rows leaves only
        # the rows that are unique between the two frames. This allows a quick
        # check of the DataFrame to see if it is empty - if so, all rows are
        # duplicates, and they are equal.
        frames = [df, harry_kane.dataframe]
        df1 = pd.concat(frames).drop_duplicates(keep=False)

        assert df1.empty

    @mock.patch('requests.get', side_effect=mock_pyquery)
    def test_fb_invalid_tables_returns_nothing(self, *args, **kwargs):
        roster = Roster('Tottenham Hotspur')
        stats = roster._pull_stats(pq('<div></div>'))

        assert stats == {}

    def test_fb_roster_string_representation(self):
        expected = """Toby Alderweireld (f7d50789)
Serge Aurier (5c2b4f07)
Harry Kane (21a66f6a)
Son Heung-min (92e7e919)
Moussa Sissoko (2acd49b9)
Davinson Sánchez (da7b447d)
Harry Winks (2f7acede)
Lucas Moura (2b622f01)
Dele Alli (cea4ee8f)
Hugo Lloris (8f62b6ee)
Jan Vertonghen (ba23a904)
Paulo Gazzaniga (63d17038)
Ben Davies (44781702)
Giovani Lo Celso (d7553721)
Eric Dier (ac861941)
Érik Lamela (abe66106)
Tanguy Ndombele (5cdddffa)
Christian Eriksen (980522ec)
Danny Rose (89d10e53)
Steven Bergwijn (a29b1131)
Japhet Tanganga (e9971f2d)
Ryan Sessegnon (6aa3e78b)
Kyle Walker-Peters (984a5a64)
Oliver Skipp (6250083a)
Juan Foyth (6c7762c3)
Gedson Fernandes (e2dde94c)
Victor Wanyama (e0900238)
Troy Parrott (4357f557)
Georges-Kévin N'Koudou (76c131da)
Brandon Austin (5e253986)
Dennis Cirken (307ea3b6)
Michel Vorm (1bebde9d)
Harvey White (4d90ce8c)
Alfie Whiteman (3f2587ee)"""

        assert self.roster.__repr__() == expected

    def test_fb_player_string_representation(self):
        player = self.roster('Harry Kane')

        assert player.__repr__() == 'Harry Kane (21a66f6a)'
