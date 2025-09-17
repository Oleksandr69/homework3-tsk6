import math
import first_member
import second_member
import third_member
print("=== Калькулятор ===")
def main_menu():
	while True:
		print("\n=== Оберіть операцію ===")
		print("1-додати(+), 2-відняти(-), 3-помножити(*), 4-поділити(/).")
		print("5-цілочисельне ділення(//), 6-остача від ділення(%), 7-звести в ступінь, 8-здобути корінь.")
		print("9-sin(x), 10-cos(x), 11-tg(x), 12-чи парне x.")
		choice = input("===Ваш вибір: ")
		if choice == '1':
			first_member.add()
		elif choice == '2':
			first_member.subtraction()
		elif choice == '3':
			first_member.multiplication()
		elif choice == '4':
			first_member.division()
		elif choice == '5':
			second_member.integer_division()
		elif choice == '6':
			second_member.remainder_of_dividing()
		elif choice == '7':
			second_member.power()
		elif choice == '8':
			second_member.root()
		elif choice == '9':
			third_member.sin()
		elif choice == '10':
			third_member.cos()
		elif choice == '11':
			third_member.tg()
		elif choice == '12':
			third_member.is_even()
		elif choice == '0':
			print("До побачення!")
			break
		else:
			print("Невірний вибір!")

main_menu()