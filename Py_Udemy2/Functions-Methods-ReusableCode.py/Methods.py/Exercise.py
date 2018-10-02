"""
Methods Exercise :
Create a method, which takes the state and gross income as the arguments and returns the net income after deducting tax based on the state.

Assume Federal Tax: 10%
Assume state tax on your wish.

You don’t have to do for all the states, just take 3-4 to solve the purpose of the exercise.
"""

def CaliculateNetIncome(gross, state):
    state_tax ={'NYC':10 ,'WASH':8,'CAL':8}
    net = gross - (gross * .10)
    if state in state_tax :
        net = net - (gross * state_tax[state]/100)
        print("you income after tax is :" , str(net))
        return net
    else:
        print ("state not in the list")
        return None

CaliculateNetIncome (500000,'NYC')

    