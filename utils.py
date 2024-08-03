import numpy as np

def dictionary_to_vector(parameters):
    """
    converts parameter dictionary to a single vector

    Arguments:
    parameters: dictionary of parameters

    Return:
    vector: vector of model parameters
    """
    vector = []
    for i in parameters:
        reshaped = np.reshape(parameters[i], parameters[i].shape[0]*parameters[i].shape[1])
        vector.extend(reshaped)
    return np.array(vector)

def vector_to_dictionary(vector, parameters):
    """
    converts parameter vector back into dictionary

    Arguments:
    vector: vector of parameters
    paramters: dictionary of original model parameters

    Return:
    parameters: dictionary of parameters
    """
    params = {}
    for i in parameters:
        params[i] = vector[:parameters[i].shape[0]*parameters[i].shape[1]].reshape(parameters[i].shape)
    return params
