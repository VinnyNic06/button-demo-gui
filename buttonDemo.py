"""
Program: labelDemo.py

Page: 250

Simple python GUI window with command buttons
"""

from breezyPythonGui import EasyFrame

class LabelDemo(EasyFrame):
	"""Illustrares command buttons and user events"""

	def __init__(self):
		"""Sets up the window and the label"""
		EasyFrame.__init__(self)
		
		# A single label in the first row
		self.label = self.addLabel(text="Hello World!", row = 0, column = 0, columnspan = 2, sticky = "NSEW")

		# Two command buttons in the second row
		self.clearBtn = self.addButton(text = "Clear", row = 1, column = 0, command = self.clear)
		self.restoreBtn = self.addButton(text = "Restore", row = 1, column = 1, state = "Disabled", command = self.restore)

	# Methods to handle user events 
	def clear(self):
		""" Resets the label to the Hello World! and updates the button states """
		self.label["text"] = "Hello World!"
		self.clearBtn["state"] = "normal"
		self.restoreBtn["state"] = "disabled"


	def restore(self):
		""" Resets the label to the empty string and updates the button states """
		self.label["text"] = ""
		self.clearBtn["state"] = "disabled"
		self.restoreBtn["state"] = "normal"


def main():
	""" initiates and pops up the window"""

	ButtonDemo().mainloop()

# Global call to the main() function
main()