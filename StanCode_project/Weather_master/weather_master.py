"""
File: weather_master.py
Name: Tony
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
# This constant controls when to stop
EXIT = -1


def main():
	"""
	This program finds 4 outcomes among user inputs
	a. Maximum
	b. Minimum
	c. Average
	d. cold days (data that are lower than 16)
	"""
	print("stanCode \"Weather Master 4.0\"")
	data = int(input("Next Temperature: (or -1 to quit): "))
	if data == EXIT:
		print("No number were entered")
	else:
		minimum = data
		maximum = data
		number = 0
		total = data
		if data < 16:
			count = 1
		else:
			count = 0
		while True:
			data = int(input("Next Temperature: (or -1 to quit): "))
			number += 1
			total = total + data
			if data == EXIT:
				break
			if data < 16:
				count += 1
			if data < minimum:
				minimum = data
			elif data > maximum:
				maximum = data
		print("Highest temperature = " + str(maximum))
		print("Lowest temperature = " + str(minimum))
		print("Average = " + str((total + 1) / number))
		print(str(count) + " cold day(s) ")


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
