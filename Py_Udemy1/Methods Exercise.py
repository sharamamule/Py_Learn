"""
Methods Exercise
Create a method, which takes the state and gross income as the arguments and returns the net income after 
   deducting tax based on the state.

Assume Federal Tax: 10%
Assume state tax on your wish.

You don’t have to do for all the states, just take 3-4 to solve the purpose of the exercise.

"""

def tax_usa (GrossI, state):
    """
    Calculation of Net income after federal and state tax
    :param state : state name
    :param GrossI : Gross Income
    :return: Net Income
    """
    state_tax = {'Atlanta':10,'Texas':9,'Nasville':0,'NYC':6}

#calculate the net income after federal tax       
    net = GrossI - (GrossI* .10)  # .10 = 10/100 = 10%

#calculate the net income after state tax
    # net = net -(GrossI * state_tax[state]/100)    -- Try this?
    if state in state_tax: 
       net = net -(GrossI * state_tax[state]/100)          
       print ("Your net income after all tax is: " + str(net))
       return net
    else:
       print ("STATE not in the list")
       return None

tax_usa(18000,'NjC')
