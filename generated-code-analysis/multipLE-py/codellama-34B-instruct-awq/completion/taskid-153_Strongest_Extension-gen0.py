from typing import List

def Strongest_Extension(class_name: str, extensions: List[str]) -> str:
    """You will be given the name of a class (a string) and a list of extensions.
    The extensions are to be used to load additional classes to the class. The
    strength of the extension is as follows: Let CAP be the number of the uppercase
    letters in the extension's name, and let SM be the number of lowercase letters 
    in the extension's name, the strength is given by the fraction CAP - SM. 
    You should find the strongest extension and return a string in this 
    format: ClassName.StrongestExtensionName.
    If there are two or more extensions with the same strength, you should
    choose the one that comes first in the list.
    For example, if you are given "Slices" as the class and a list of the
    extensions: ['SErviNGSliCes', 'Cheese', 'StuFfed'] then you should
    return 'Slices.SErviNGSliCes' since 'SErviNGSliCes' is the strongest extension 
    (its strength is -1).
    Example:
    >>> Strongest_Extension('my_class', ['AA', 'Be', 'CC'])
    'my_class.AA'
    """


    #your code goes here
    class_name += '.'
    strongest_extension = ''
    current_max = -1
    for i in range(len(extensions)):
        sum_upper = 0
        for j in range(len(extensions[i])):
            if extensions[i][j].isupper():
                sum_upper += 1
        strength = sum_upper - len(extensions[i]) + len(class_name) + len(extensions[i])
        if strength > current_max:
            current_max = strength
            strongest_extension = class_name + extensions[i]
    return strongest_extension
