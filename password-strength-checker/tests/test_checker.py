from app.checker import evaluate_password

def test_password_strength():
    score, strength, issues = evaluate_password("Abcd1234!")
    assert score == 5
    assert strength == "Very Strong"
    assert issues == []