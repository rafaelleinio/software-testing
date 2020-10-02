from __future__ import annotations

from typing import List


class KataBowling:
    def __init__(self, rolls: List[int] = None):
        self.rolls = rolls if rolls else []

    def roll(self, round_score: int):
        return KataBowling(rolls=self.rolls + [round_score])

    @property
    def score(self) -> int:
        score = 0
        frame_index = 0
        for frame in range(10):
            if self._is_strike(frame_index):
                score += 10 + self._strike_bonus(frame_index)
                frame_index += 1
            elif self._is_spare(frame_index):
                score += 10 + self._spare_bonus(frame_index)
                frame_index += 2
            else:
                score += self._normal_frame(frame_index)
                frame_index += 2
        return score

    def _get_roll_score(self, i):
        return self.rolls[i] if i < len(self.rolls) else 0

    def _is_strike(self, i: int) -> bool:
        return self._get_roll_score(i) == 10

    def _is_spare(self, i: int) -> bool:
        return self._get_roll_score(i) + self._get_roll_score(i + 1) == 10

    def _strike_bonus(self, i: int) -> int:
        return self._get_roll_score(i + 1) + self._get_roll_score(i + 2)

    def _spare_bonus(self, i: int) -> int:
        return self._get_roll_score(i + 2)

    def _normal_frame(self, i: int) -> int:
        return self._get_roll_score(i) + self._get_roll_score(i + 1)
