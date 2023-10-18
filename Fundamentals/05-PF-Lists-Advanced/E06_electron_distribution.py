# You are a mad scientist, and you have decided to play with electron distribution among atom shells. The basic idea of
# electron distribution is that electrons should fill a shell until it holds the maximum number of electrons.
# You will receive a single integer - the number of electrons. Your task is to fill shells until there are no more
# electrons left. The rules for electron distribution are as follows:
# •	The maximum number of electrons in a shell can be 2n2, where n is the position of a shell (starting from 1).
# For example, the maximum number of electrons in the 3rd shield can be 2*3^2 = 18.
# •	You should start filling the shells from the first one at the first position.
# •	If the electrons are enough to fill the first shell, the left unoccupied electrons should fill the following shell
# and so on.
# In the end, print a list with the filled shells.

def shells(number_electrons):
    shells_list = []
    count_shells = 1

    while number_electrons > 0:

        electrons_per_shell = 2 * (count_shells ** 2)

        if electrons_per_shell <= number_electrons:
            shells_list.append(electrons_per_shell)
            number_electrons -= electrons_per_shell
        else:
            shells_list.append(number_electrons)
            break

        count_shells += 1

    return shells_list


electrons = int(input())

print(shells(electrons))