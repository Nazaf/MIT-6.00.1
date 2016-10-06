def oddTuples(aTup):
    #Converting tuple to a list to loop and [0::2] will take the first element and every other odd positoned values
    return tuple([item for item in list(aTup[0::2])])  #converting the tuple to list 
