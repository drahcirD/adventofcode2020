import pytest
from main import BoardingCard


@pytest.mark.parametrize(
    "test_input, row, col, id",
    [
        ("BFFFBBFRRR", 70, 7, 567),
        ("FFFBBBFRRR", 14, 7, 119),
        ("BBFFBBFRLL", 102, 4, 820),
    ],
)
def test_parse_boarding_card(test_input, row, col, id):
    card = BoardingCard(test_input)
    import pdb

    pdb.set_trace()
    assert card.row == row
    assert card.col == col
    assert card.id == id
