"""
A simple calculator module that provides basic arithmetic operations.
"""
from typing import Union, Optional

class Calculator:
    """
    A calculator class that performs basic arithmetic operations.
    
    Attributes:
        num1: The first number for calculations
        num2: The second number for calculations
    """
    
    def __init__(self, num1: Union[int, float], num2: Union[int, float]):
        """
        Initialize the Calculator with two numbers.
        
        Args:
            num1: The first number
            num2: The second number
        """
        self.num1 = num1
        self.num2 = num2
    
    def add(self, num1: Optional[Union[int, float]] = None, num2: Optional[Union[int, float]] = None) -> Union[int, float]:
        """
        Add two numbers.
        
        Args:
            num1: First number (uses self.num1 if None)
            num2: Second number (uses self.num2 if None)
            
        Returns:
            The sum of the two numbers
        """
        n1 = self.num1 if num1 is None else num1
        n2 = self.num2 if num2 is None else num2
        return n1 + n2
    
    def sub(self, num1: Optional[Union[int, float]] = None, num2: Optional[Union[int, float]] = None) -> Union[int, float]:
        """
        Subtract the second number from the first.
        
        Args:
            num1: First number (uses self.num1 if None)
            num2: Second number (uses self.num2 if None)
            
        Returns:
            The difference between the two numbers
        """
        n1 = self.num1 if num1 is None else num1
        n2 = self.num2 if num2 is None else num2
        return n1 - n2
    
    def mul(self, num1: Optional[Union[int, float]] = None, num2: Optional[Union[int, float]] = None) -> Union[int, float]:
        """
        Multiply two numbers.
        
        Args:
            num1: First number (uses self.num1 if None)
            num2: Second number (uses self.num2 if None)
            
        Returns:
            The product of the two numbers
        """
        n1 = self.num1 if num1 is None else num1
        n2 = self.num2 if num2 is None else num2
        return n1 * n2
    
    def div(self, num1: Optional[Union[int, float]] = None, num2: Optional[Union[int, float]] = None) -> Union[int, float]:
        """
        Divide the first number by the second.
        
        Args:
            num1: First number (uses self.num1 if None)
            num2: Second number (uses self.num2 if None)
            
        Returns:
            The quotient of the two numbers
            
        Raises:
            ZeroDivisionError: If the second number is zero
        """
        n1 = self.num1 if num1 is None else num1
        n2 = self.num2 if num2 is None else num2
        if n2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return n1 / n2
    
    def mod(self, num1: Optional[Union[int, float]] = None, num2: Optional[Union[int, float]] = None) -> Union[int, float]:
        """
        Get the remainder of dividing the first number by the second.
        
        Args:
            num1: First number (uses self.num1 if None)
            num2: Second number (uses self.num2 if None)
            
        Returns:
            The remainder of the division
            
        Raises:
            ZeroDivisionError: If the second number is zero
        """
        n1 = self.num1 if num1 is None else num1
        n2 = self.num2 if num2 is None else num2
        if n2 == 0:
            raise ZeroDivisionError("Modulo by zero is not allowed")
        return n1 % n2


if __name__ == "__main__":
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        
        calc = Calculator(num1, num2)
        
        print(f"Addition: {calc.add()}")
        print(f"Subtraction: {calc.sub()}")
        print(f"Multiplication: {calc.mul()}")
        print(f"Division: {calc.div()}")
        print(f"Modulo: {calc.mod()}")
    except ValueError:
        print("Please enter valid numbers")
    except ZeroDivisionError as e:
        print(e)