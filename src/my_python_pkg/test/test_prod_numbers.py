"""Tests for prod_numbers module."""

import pytest

from my_python_pkg.prod_numbers import prod_numbers


def test_positive_numbers():
    """Test multiplication of positive numbers."""
    assert prod_numbers(2, 3) == 6


def test_negative_numbers():
    """Test multiplication of negative numbers."""
    assert prod_numbers(-2, -3) == 6


def test_mixed_numbers():
    """Test multiplication of mixed positive and negative numbers."""
    assert prod_numbers(10, -5) == -50


def test_zero_numbers():
    """Test multiplication with zero."""
    assert prod_numbers(0, 5) == 0
    assert prod_numbers(5, 0) == 0
    assert prod_numbers(0, 0) == 0
