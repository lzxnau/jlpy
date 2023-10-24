"""
Base module for Python language testing.

This module is the base module for all other objects @ JLPy.Lang namespace.
::

   Author  : JLPy
   Version : 2023.10.23.02

.. note::
   This is the note.
"""


class BaseClass:
  """
  Base Class for all other objects.
  
  This is the base Class for all other objects @ JLPy.Lang namespace.
  """
  
  def __init__(self):
    """Class constructor."""
    ...
  
  def print(self) -> None:
    """
    Printing class name.
    
    This method prints the class name of the instance for debugging.
    """
    obj = type(self)
    print(f'This is an instance of the {obj.__name__} class.')


if __name__ == '__main__':
  bc = BaseClass()
  bc.print()
