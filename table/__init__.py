#!/bin/usr/bin/env python3
"""A table module for python
"""

__author__ = 'Evan Young'
__copyright__ = 'Copyright 2017, Evan Young'
__credits__ = 'Evan Young'

__license__ = 'GNU GPLv3'
__version__ = '0.1.16'
__maintainer__ = 'Evan Young'
__status__ = 'Alpha'



class align:
   LEFT = "<"
   CENTER = "^"
   RIGHT = ">"


class table:
   """The main class
   
   The table object, supports rows, formatting, dellimitters, an borders
   """
   def __init__(self, rows, fmt="default", dellim=" ", colbd="|", rowbd="-"):
      """The main function
      
      Does all the heavy lifting
      
      Arguments:
         rows   {array} -- An array of arrays of items in rows
      
      Keyword Arguments:
         fmt    {str}   -- The format string                                      (default: {"default"})
         dellim {str}   -- The character that expands string to the proper length (default: {" "})
         colbd  {str}   -- The column border                                      (default: {"|"})
         rowbd  {str}   -- The row border                                         (default: {"-"})
      """

      """
      Converts the items in rows to strings
      The headers are centered
      Every other item is lefted
      The maximum length of each column is determined
      """
      self.rows = [[str(x) for x in r] for r in rows]
      self.fmt = [[align.CENTER for x in self.rows[0]]]
      self.fmt.extend([[align.LEFT]*len(self.rows[i]) for i in range(len(self.rows)-1)])
      self.collen = [max([len(x[i])+2 for x in self.rows]) for i in range(len(self.rows[0]))]

      self.dellim = dellim
      self.colbd = colbd
      self.rowbd = rowbd


   def display(self):
      for rowind in range(len(self.rows)):
         row = self.rows[rowind]
         for strind in range(len(row)):
            txt = row[strind]
            fstr = f"{self.dellim}{self.fmt[rowind][strind]}{self.collen[strind]}"
            print(f"{self.colbd}{txt:{fstr}}", end="")
         print(f"{self.colbd}\n{self.rowbd*(sum(self.collen)+len(self.collen)+len(self.colbd))}")