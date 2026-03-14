import pytest
from unittest.mock import MagicMock
from dark_mode import DarkMode
import json
import os

@pytest.fixture
def mock_local_storage():
    return MagicMock()

@pytest.fixture
def mock_document():
    return MagicMock()

def test_dark_mode_happy_path(mock_local_storage, mock_document):
    mock_local_storage.getItem.return_value = 'light'
    mock_document.body = MagicMock()
    dark_mode = DarkMode()
    dark_mode.theme = 'light'
    dark_mode.applyTheme()
    mock_document.body.classList.remove.assert_called_once_with('dark-mode')

def test_dark_mode_error_case(mock_local_storage, mock_document):
    mock_local_storage.getItem.return_value = None
    mock_document.body = MagicMock()
    dark_mode = DarkMode()
    dark_mode.theme = 'light'
    dark_mode.applyTheme()
    mock_document.body.classList.remove.assert_called_once_with('dark-mode')

def test_dark_mode_edge_case(mock_local_storage, mock_document):
    mock_local_storage.getItem.return_value = 'invalid'
    mock_document.body = MagicMock()
    dark_mode = DarkMode()
    dark_mode.theme = 'light'
    dark_mode.applyTheme()
    mock_document.body.classList.remove.assert_called_once_with('dark-mode')

def test_toggle_theme_happy_path(mock_local_storage, mock_document):
    mock_local_storage.getItem.return_value = 'light'
    mock_document.body = MagicMock()
    dark_mode = DarkMode()
    dark_mode.theme = 'light'
    dark_mode.toggleTheme()
    mock_local_storage.setItem.assert_called_once_with('theme', 'dark')
    mock_document.body.classList.add.assert_called_once_with('dark-mode')

def test_toggle_theme_error_case(mock_local_storage, mock_document):
    mock_local_storage.getItem.return_value = None
    mock_document.body = MagicMock()
    dark_mode = DarkMode()
    dark_mode.theme = 'light'
    dark_mode.toggleTheme()
    mock_local_storage.setItem.assert_called_once_with('theme', 'dark')
    mock_document.body.classList.add.assert_called_once_with('dark-mode')

def test_toggle_theme_edge_case(mock_local_storage, mock_document):
    mock_local_storage.getItem.return_value = 'invalid'
    mock_document.body = MagicMock()
    dark_mode = DarkMode()
    dark_mode.theme = 'light'
    dark_mode.toggleTheme()
    mock_local_storage.setItem.assert_called_once_with('theme', 'dark')
    mock_document.body.classList.add.assert_called_once_with('dark-mode')
