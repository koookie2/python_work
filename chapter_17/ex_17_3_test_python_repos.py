from main_17_1_python_repos import python_repos

print(python_repos)

def test_function():
    """Is the status code equal to 200?"""
    python_repo = python_repos()
    assert python_repo == 200

test_function()