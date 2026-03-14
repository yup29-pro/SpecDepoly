import pytest
from config import config
import json

def test_config_happy_path():
    assert config['theme']['light']['background'] == '#ffffff'
    assert config['theme']['light']['text'] == '#000000'
    assert config['theme']['dark']['background'] == '#000000'
    assert config['theme']['dark']['text'] == '#ffffff'

def test_config_error_case():
    with pytest.raises(KeyError):
        config['invalid']

def test_config_edge_case():
    with pytest.raises(KeyError):
        config['theme']['invalid']
