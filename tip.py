from sample import calculate_rate, calculate_meal_costs
import sys

def main():
#why are there no variable names in main (I just followed example)?
	meal_base, tax_rate, tip_rate=float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
	meal_info=calculate_meal_costs(meal_base, tax_rate, tip_rate)
	#how do I do a do a multiline code?
	#does this not override meal_info as a dictionary in calculate_meal_costs?
	print meal_info['meal_base']
	print meal_info['tax_value']
	print meal_info['tip_rate']
	print meal_info['total']
	
if __name__ == '__main__':
    	try: 
    		main()
    	except ValueError:
    		print "Oops! There's a non-valid number. Try again..."
    		meal_base=float(raw_input("meal base cost"))
    		tax_rate=float(raw_input("tax rate"))
    		tip_rate=float(raw_input("tip rate"))
    		time_2=calculate_meal_costs(meal_base, tax_rate, tip_rate)
    		print meal_info['meal_base']
    		print meal_info['tax_value']
    		print meal_info['tip_rate']
    		print meal_info['total']
    		
    	