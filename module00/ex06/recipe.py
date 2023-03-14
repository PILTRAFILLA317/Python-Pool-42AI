def recipeAdd(cookbook, name):
	ing = input("\nInsert recipe ingredients\n> ")
	type = input("Insert meal type\n> ")
	time = input("Insert recipe preparation time\n> ")
	cookbook[name] = {"ingredients" : ing.split(", "), "meal" : type, "prep_time" : time}
	print("")

def recipePrinter(recipe, name):
	print(f"\nRecipe for {name}")
	print(f"	Ingredients list: {recipe['ingredients']}")
	print(f"	To be eaten for {recipe['meal']}")
	print(f"	Takes {recipe['prep_time']}\n")

def bookPrinter(cookbook):
	for val in cookbook:
		recipePrinter(cookbook[val], val)

if __name__ == "__main__":
	bocadilloRecipe = {
	'ingredients': ['jamon', 'pam', 'queso', 'tomate'],
	'meal': 'almuerzo',
	'prep_time': '10',
	}
	tartaRecipe = {
	'ingredients': ['harina', 'azucar', 'huevos'],
	'meal': 'postre',
	'prep_time': '60',
	}
	ensaladaRecipe = {
	'ingredients': ['aguacate', 'rucula', 'espinacas', 'tomate'],
	'meal': 'almuerzo',
	'prep_time': '15',
	}
	cookbook = {
	"bocadillo" : bocadilloRecipe,
	"tarta" : tartaRecipe,
	"ensalada" : ensaladaRecipe,
	}
	print("Welcome to the Python Cookbook !\nList of available option:\n	1: Add a recipe\n	2: Delete a recipe\n	3: Print a recipe\n	4: Print the cookbook\n	5: Quit")
	while True:
		try:
			num = int(input("Please select an option\n>> "))
		except:
			print("Sorry, this option does not exist")
			continue
		if num == 1:
			print("")
			try:
				name = str(input("Please enter a recipe name to add\n>> "))
			except:
				print("Sorry, this option does not exist")
				continue
			if name in cookbook:
				print("Sorry, this option does alresy exist")
				continue
			recipeAdd(cookbook, name)
		if num == 2:
			print("")
			try:
				rem = str(input("Please enter a recipe name to delete\n>> "))
			except:
				print("Sorry, this option does not exist")
				continue
			if rem not in cookbook:
				print("Sorry, this option does not exist")
				continue
			del cookbook[rem]
			print("")
		if num == 3:
			print("")
			try:
				recipe = str(input("Please enter a recipe name to get its details\n>> "))
			except:
				print("Sorry, this option does not exist")
				continue
			if recipe not in cookbook:
				print("Sorry, this option does not exist")
				continue
			recipePrinter(cookbook[recipe], recipe)
		if num == 4:
			bookPrinter(cookbook)
		if num == 5:
			print ("\nCookbook closed. Goodbye !")
			exit(0)

