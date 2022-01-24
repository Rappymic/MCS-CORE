'''Problem Statement – Stephan is a vampire. And he is fighting with his brother Damon. Vampires get energy from human bloods, so they need to feed on human blood, killing the human beings. Stephan is also less inhuman, so he will like to take less life in his hand. Now all the people’s blood has some power, which increases the powers of the Vampire. Stephan just needs to be more powerful than Damon, killing the least human possible. Tell the total power Steohan will have after drinking the bloods before the battle.

Note that: Damon is a beast, so no human being will be left after Damon drinks everyone’s blood. But Stephan always comes early in the town.
Input Format:

First line with the number of people in the town, n.

Second line with a string with n characters, denoting the one digit power in every blood.

Output Format:

Total minimum power Stephan will gather before the battle.

Constraints:

n<=10^4
Sample input :

6

093212

Sample output :

9

Explanation:

Stephan riches the town, drinks the blood with power 9. Now Damon cannot reach 9 by drinking all the other bloods'''

def sum_list(li):
    a = 0
    for i in li:
        a += i
    return a

n = 6

string1 = '935652'

list_power = [int(i) for i in string1]
list_power.sort(reverse=True)
# list_power_copy = list_power[:]
print(list_power)
a = list_power[0]
for i in range(1, len(list_power)):
    if a < sum_list(list_power[i:]):
        a += list_power[i]
    else:
        break

print(a, i)