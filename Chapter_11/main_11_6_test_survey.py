import pytest
from main_11_4_survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    """A survey that will be available to all test functions."""
    language_survey = AnonymousSurvey("What language did you first learn to speak?")
    return language_survey

def test_store_single_response(language_survey):
    """Test that a single response is stored properly."""
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_responses(language_survey):
    """Test that three individual responses are stored properly."""
    language_survey.store_response(['English', 'Spanish', 'Mandarin'])
    assert ['English', 'Spanish', 'Mandarin'] in language_survey.responses