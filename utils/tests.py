def test_function(fun, test_data):
    """Utility function for testing
    
    Arguments
    ---------
    fun : function, the function to perform the test on
    test_data : dict, dictionary with two keys - 'inputs' and 'outputs'. Each
        value in the dict is a list. dict['inputs'][ii] is the input to the
        function fun for which the expected output is dict['outputs'][ii]
        
    Returns
    -------
    nr_errors : int, the number of tests that failed
    """
    nr_errors = 0
    for kk, vv in zip(test_data['inputs'], test_data['outputs']):
        ans = fun(kk)
        if ans != vv:
            print('fun({}) != {} (={})'.format(kk, vv, ans))
            errors += 1
    return nr_errors