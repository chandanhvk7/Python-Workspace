"""
A bunch of utility functions created by Lecius Karigann 

Version 1.0
"""

def dirr(obj):
    """
    This method returns non-dunder attributes of the given obj
    """
    # attrs=[]
    # for attr in dir(obj):
    #     if not attr.startswith('_'):
    #         attrs.append(attr)
    # return attrs
    return [each_attr for each_attr in dir(obj) if not each_attr.startswith('_')]

def to_float(str_num):
    """converts the given str to a float if possible else returns 0.0"""
    try:
        return float(str_num)
    except ValueError:
        return 0.0