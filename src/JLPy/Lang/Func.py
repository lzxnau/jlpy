"""
Module for Python language function testing.

Testing Python language function features @ JLPy.Lang namespace.
::
  
   Author  : JLPy
   Version : 2023.10.23.02
   
.. note::
   This is the note.
"""
from JLPy.Lang.Base import BaseClass


class FuncTest(BaseClass):
  """
  Function Test Class.
  
  This is the call to test the Python language function features.
  """
  
  def __init__(self):
    """Class constructor."""
    super().__init__()
  
  @staticmethod
  def first(**kwargs):
    def outer(fl2):
      def inner():
        if kwargs['ist']:
          print('Test!')
        if kwargs['isp']:
          print('Print!')
        fl2()
      
      return inner
    
    return outer
  
  @staticmethod
  def second(fl1):
    def inner():
      print('second')
      fl1()
    
    return inner
  
  @staticmethod
  @first(ist=False, isp=True)
  @second
  def third():
    print('Hello World!')


if __name__ == '__main__':
  ft = FuncTest()
  FuncTest.third()
