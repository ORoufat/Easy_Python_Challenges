"""


Scenario:
İn a small town the population is po= 1000 at the beginning of a year.
The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live in town.
Howmany years does the town need to see its populatıon greater or equal to po=1200 inhabitants.

HINT:: at the end of the 1st year there will be:
1000 + 1000 * 0.02 + 50 = 1070

at the end of the 2nd year there will be :
1070 + 1070 * 0.02 + 50 = 1141

at the end of the 3rd year there will be
1070 + 1070 * 0.02 + 50 = 1213 ppl will be

SOLUTION:
"""

po = float(1000)
years = 0
inhab = 50
percent = 0.02

for year in range(20):
    equation = (po * percent) + (po + inhab)
    print(round(equation))
    po = equation
    if po >= 1213:
        break
