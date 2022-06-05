import random
from time import perf_counter
import math
from pylint import epylint as lint


def linear_search(lyst, target):
    '''
    TAKES IN TWO ARGUMENTS THE ITERABLE AND THE TARGET
    OUTPUTS A BOOLEAN VALUE DETERMINING WHETHER TARGET
    IS FOUND IN THE LYST. IF FOUND = TRUE, ELSE FALSE
    THE LYST MUST BE A SORTED LIST.
    '''
    if lyst is None:
        return None
    for i in lyst:
        if i == target:
            return True
    return False

def jump_search(lyst, target):
    '''
    TAKES IN TWO PARAMETERS LYST AND TARGET.
    THE FUNCTION COMPARES WHETHER TARGET IS FOUND IN LYST.
    IF SO, RETURN TRUE, OTHERWISE FALSE. THE JUMP VALUE IS
    DETERMINED BY TAKING THE SQRT OF THE LENGTH OF LYST.
    '''
    if lyst is None:
        return None
    lyst_len = len(lyst)
    jump_size = int(math.sqrt(lyst_len))
    lower_end = 0
    higher_end = jump_size-1
    while higher_end<=lyst_len:
        if lyst[higher_end]==target:
            return True
        # IF THE VALUE AT LIST OF HIGHER_END IS GREATER THAN THE TARGET
        # WE WANT TO ITERATE BACKWARDS UNTIL IT REACHES THE LOWER END.
        # IF THAT'S NOT THE CASE, WE RETURN FALSE, BUT IF IT'S THE CASE
        # WE RETURN TRUE.
        elif lyst[higher_end-1] > target:
            if (higher_end + jump_size) >= len(lyst):
                tmp_high = len(lyst)
                tmp_low = lower_end
            else:
                tmp_high = higher_end
                tmp_low = lower_end
            for i in lyst[tmp_low:tmp_high]:
                if i == target:
                    return True
            return False
        # THIS CASE THE VALUE IS LESS THAN THE TARGET. ITERATE THROUGH TO FIND
        # THE VALUE WHICH MATCHES THE TARGET OR IS GREATER THAN THE TARGET.
        else:
            lower_end += jump_size
            higher_end += jump_size
    return False

def binary_search(lyst, target):
    '''
    FUNCTION TAKES IN TWO PARAMETERS LYST AND TARGET.
    BINARY SEARCH WILL TAKE THE FIRST AND LAST INDEX, SUM THEM UP & DIVIDE
    BY TWO TO GET A MIDDLE INDEX. IT WILL COMPARE THE VALUE OF MIDDLE INDEX
    TO THE TARGET. IF THE LYST[INDEX]==TARGET, THEN TRUE, OTHERWISE FALSE IF
    THE TARGET IS NOT FOUND IN LYST.
    '''
    if lyst is None:
        return None
    upper_bound = len(lyst)
    lower_bound = 0
    mid_index = (upper_bound+lower_bound)//2
    # if lyst[upper_bound]==target or lyst[lower_bound]==target:
    #     return True
    # else:
    for i in range(int(math.log2(len(lyst)))+1):
        if lyst[mid_index]<target:
            lower_bound = mid_index
            mid_index = (upper_bound+lower_bound)//2
        elif lyst[mid_index]>target:
            upper_bound = mid_index
            mid_index = (upper_bound+lower_bound)//2
        else:
            return True
    return False

def main():
    '''
    THE MAIN RUNS THROUGH THE FUNCTIONS AND ENSURES THEY HAVE
    CORRECT VALUES. ALSO USES TIME MODULE TO COMPARE THE TIMES
    OF BINARY, LINEAR, & JUMP SEARCH.
    '''
    range_lyst = list(range(10000000))
    test_lyst = sorted(random.sample(range_lyst,1000000))
    random.seed(1)
    find_rand_value = random.randint(0,10000000)

    last_val_test_lyst = test_lyst[-1]
    first_val_test_lyst = test_lyst[0]

    mid_index = len(test_lyst)//2
    mid_val_test_lyst = test_lyst[mid_index]

    not_in_test_lyst = -1

    lyst_iterables = [(first_val_test_lyst, 'First Value in List:'),
    (last_val_test_lyst,'Last Value in List:'),
    (mid_val_test_lyst,'Mid Value in List:'),(not_in_test_lyst,'Element Not in List (-1):'),
    (find_rand_value,'Random Integer:')]

    for i in lyst_iterables:
        print('\n'+i[-1]+'\n')
        start = perf_counter()
        print('For linear search: ',linear_search(test_lyst, i[0]))
        end = perf_counter()
        total_time = end-start
        print(total_time)

        start = perf_counter()
        print('For jump search: ',jump_search(test_lyst, i[0]))
        end = perf_counter()
        total_time = end-start
        print(total_time)

        start = perf_counter()
        print('For binary search: ',binary_search(test_lyst, i[0]))
        end = perf_counter()
        total_time = end-start
        print(total_time)

    (pylint_stdout, pylint_stderr) = lint.py_run('search.py', return_std=True)
    expected = 8.5
    actual = pylint_stdout.getvalue()
    print(actual)



if __name__ == '__main__':
    main()
