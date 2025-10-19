import pytest
from main import Calculator


class TestCalculator:
    """Test suite for Calculator class"""
    
    def test_add(self):
        """Test addition operation"""
        calc = Calculator(10, 5)
        assert calc.add(10, 5) == 15
        assert calc.add(0, 0) == 0
        assert calc.add(-5, 5) == 0
        assert calc.add(-10, -5) == -15
    
    def test_sub(self):
        """Test subtraction operation"""
        calc = Calculator(10, 5)
        assert calc.sub(10, 5) == 5
        assert calc.sub(5, 10) == -5
        assert calc.sub(0, 0) == 0
        assert calc.sub(-5, -5) == 0
    
    def test_multiply(self):
        """Test multiplication operation"""
        calc = Calculator(10, 5)
        assert calc.multiply(10, 5) == 50
        assert calc.multiply(0, 5) == 0
        assert calc.multiply(-5, 5) == -25
        assert calc.multiply(-5, -5) == 25
    
    def test_divide(self):
        """Test division operation"""
        calc = Calculator(10, 5)
        assert calc.divide(10, 5) == 2.0
        assert calc.divide(10, 2) == 5.0
        assert calc.divide(-10, 5) == -2.0
        assert calc.divide(7, 2) == 3.5
    
    def test_divide_by_zero(self):
        """Test division by zero handling"""
        calc = Calculator(10, 0)
        result = calc.divide(10, 0)
        assert result == "Error: Division by zero"
    
    def test_instance_creation(self):
        """Test Calculator instance creation"""
        calc = Calculator(100, 50)
        assert calc.a == 100
        assert calc.b == 50
    
    def test_with_floats(self):
        """Test operations with floating point numbers"""
        calc = Calculator(10.5, 2.5)
        assert calc.add(10.5, 2.5) == 13.0
        assert calc.sub(10.5, 2.5) == 8.0
        assert calc.multiply(10.5, 2.5) == 26.25
        assert calc.divide(10.5, 2.5) == 4.2


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
