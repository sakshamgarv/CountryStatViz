from project import plot_gdp, plot_pops, plot_internet, plot_sex_ratio
import pytest

def test_plot_gdp():
    assert plot_gdp(['India', 'Russia', 'United States'], [2779.352, 1660.514, 20580.223]) == True

def test_plot_pops():
    assert plot_pops(['India', 'Russia', 'United States'], [1380.004, 145.934, 331.003]) == True

def test_plot_internet():
    assert plot_internet(['India', 'Russia', 'United States'], [34.4, 80.9, 87.3]) == True

def test_plot_sex_ratio():
    assert plot_sex_ratio(['India', 'Russia', 'United States'], [108.2, 86.4, 97.9] ) == True
