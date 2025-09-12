#!/usr/bin/python3

"""
prints name and first name
first_name: first name to print
last_name: last_name to print
"""
def say_my_name(first_name, last_name=""):
	"""
	prints first name and name
	"""
	if type(first_name) is not str:
		raise TypeError("first_name must be a string")
	if type(last_name) is not str:
		raise TypeError("last_name must be a string")
	print(f"My name is {first_name} {last_name}")


say_my_name("Walter", "White", "black")
say_my_name("Bob")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)