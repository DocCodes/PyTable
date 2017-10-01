#!/bin/usr/bin/env python3
"""A table module for python
"""

__author__ = 'Evan Young'
__copyright__ = 'Copyright 2017, Evan Young'
__credits__ = 'Evan Young'

__license__ = 'GNU GPLv3'
__version__ = '0.1.27'
__maintainer__ = 'Evan Young'
__status__ = 'Alpha'



class alignment:
   LEFT = "<"
   CENTER = "^"
   RIGHT = ">"


class table:
   """The main class
   
   The table object, supports rows, formatting, delimiters, an borders
   """
   def __init__(self, rows, align="default", delim=" ", colbd="|", rowbd="-", title="", talign=alignment.CENTER, hpad=2, vpad=0):
      """The main function
      
      Does all the heavy lifting
      
      Arguments:
         rows    {array} -- An array of arrays of items in rows
      
      Keyword Arguments:
         align   {str}   -- The format string                                      (default: {"default"})
         delim   {str}   -- The character that expands string to the proper length (default: {" "})
         colbd   {str}   -- The column border                                      (default: {"|"})
         rowbd   {str}   -- The row border                                         (default: {"-"})
         title   {str}   -- The table's title                                      (default: {""})
         talign  {str}   -- The table's title alignment                            (default: {alignment.CENTER})
         hpad    {int}   -- The horizontal spacing between each cell               (default: {2})
         vpad    {int}   -- The vertical spacing between each cell                 (default: {0})
      """

      """About the self (lbl)

      Converts the items in rows to strings
      If the alignment is untouched
      The headers are centered
      Every other item is lefted
      Elif the alignment variable pertains to the columns
      Apply the alignment to each cell in the columns
      Elif the alignment variable pertains to each cell
      Apply the alignment to each cell
      The maximum length of each column is determined
      """
      self.rows = [[str(x) for x in r] for r in rows]
      if(align == "default"):
         self.align = [[alignment.CENTER for x in self.rows[0]]]
         self.align.extend([[alignment.LEFT]*len(self.rows[i]) for i in range(len(self.rows)-1)])
      elif(len(align) == len(self.rows[0])):
         self.align = [align for i in range(len(self.rows))]
      else:
         self.align = align
      self.collen = [max([len(x[i])+hpad for x in self.rows]) for i in range(len(self.rows[0]))]
      
      self.title = title
      self.talign = talign
      self.delim = delim
      self.colbd = colbd
      self.rowbd = rowbd
      self.hpad = hpad
      self.vpad = vpad

      self.realen = sum(self.collen)+len(self.collen)+len(self.colbd)


   def display(self):
      """Displays the table
      
      Determines the borders, spacing, padding, et al.
      """
      if(self.title != ""):
         fstr = f"{self.delim}{self.talign}{self.realen}"
         print(f"{self.title:{fstr}}")

      if(self.rowbd != ""):
         print(f"{self.rowbd*self.realen}")

      """About the for (lbl)
      
      Select the current row
      For cell in row
      Select the text of the cell
      Get the format (delimiter, align, spacing) of the cell
      Print the cell
      Print the cell border end
      Print vertical padding
      If the rowbd isn't empty
      Print the rowbd with the correct length
      Otherwise, line-feed
      """
      colemp = "|"
      for i in range(len(self.rows[0])):
         colemp += f"{' '*self.collen[i]}|"
      colemp += "\n"

      for rowind in range(len(self.rows)):
         row = self.rows[rowind]
         print(colemp*self.vpad, end="")
         for strind in range(len(row)):
            txt = row[strind]
            fstr = f"{self.delim}{self.align[rowind][strind]}{self.collen[strind]}"
            print(f"{self.colbd}{txt:{fstr}}", end="")

         print(self.colbd)
         print(colemp*self.vpad, end="")
         if(self.rowbd != ""):
            print(f"{self.rowbd*self.realen}")
         else:
            print()


def test_main():
   r = [
      ["Game", "Developer", "Year"],
      ["Terraria", "Re-Logic", 2011],
      ["Minecraft", "Mojang", 2011],
      ["Skyrim", "Bethesda", 2011],
      ["Fallout 4", "Bethesda", 2015]
   ]
   t = table(r)
   assert type(t) != None
   assert type(t.display).__name__ == "method"
   try:
      t.display()
   except:
      assert 0
   else:
      assert 1