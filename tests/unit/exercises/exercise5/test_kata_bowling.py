from software_testing.exercises.exercise5 import KataBowling


class TestKataBowling:
    def test_gutter_game(self):
        # arrange
        game = KataBowling(rolls=[0] * 20)

        # act
        output = game.score

        # assert
        assert output == 0

    def test_all_ones(self):
        # arrange
        game = KataBowling(rolls=[1] * 20)

        # act
        output = game.score

        # assert
        assert output == 20

    def test_spare(self):
        # arrange
        game = KataBowling().roll(5).roll(5).roll(3)
        print(">>>", game.rolls)

        # act
        output = game.score

        # assert
        assert output == 16

    def test_strike(self):
        # arrange
        game = KataBowling().roll(10).roll(3).roll(4)

        # act
        output = game.score

        # assert
        assert output == 24

    def test_perfect_game(self):
        # arrange
        game = KataBowling(rolls=[10] * 12)

        # act
        output = game.score

        # assert
        assert output == 300
