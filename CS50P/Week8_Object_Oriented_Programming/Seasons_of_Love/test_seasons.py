from seasons import age_in_words
import pytest
from datetime import date


def test_user_input():
    with pytest.raises(SystemExit):
        age_in_words("february 19, 2024")
        age_in_words("1999/12/31")




