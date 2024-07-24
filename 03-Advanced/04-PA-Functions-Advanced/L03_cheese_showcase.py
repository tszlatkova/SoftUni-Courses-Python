# Write a function called sorting_cheeses that receives keywords arguments:
# •	The key represents the name of the cheese
# •	The value is a list of quantities (integers) of the pieces of the given cheese
# The function should return the cheeses and their pieces' quantities sorted by the number
# of pieces of a cheese kind in descending order. If two or more cheeses have the same
# number of pieces, sort them by their names in ascending order (alphabetically). For each
# kind of cheese, return their piece quantities in descending order.
# For more clarifications, see the examples below.

def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    result = ""
    for cheese_name, quantities in sorted_cheeses:
        result += f"{cheese_name}\n"
        reversed_quantity = sorted(quantities, reverse=True)
        for quantity in reversed_quantity:
            result += f"{quantity}\n"
    return result


print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)
