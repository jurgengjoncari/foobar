1. create an empty list for the _values_

## PROGRAM __solution__ of _number_ with _base_
// This function will always return a number which represents an ID and they all have to be unique

1. APPEND _number_ to _values_
1. SORT _number_ DESCENDING AND save it as a string on _x_
1. SORT _number_ ASCENDING AND save it as a string on _y_
1. __substract__ _x_ and _y_ of given _base_ AND save it on _z_
1. IF the _values_ keep on repeating, RETURN the number of those _values_
1. ELSE:
    1. save _z_ to _n_
    1. CALL this function again

## PROGRAM __substract__ _second_ from _first_ of given _base_
1. substract the last digits
1. IF the first one is smaller than the second one:
    1. substract 1 from the previews digit in the first
    2. add _base_ to the last digit of first
1. add the difference of each digit to the beginning of the list
1. repeat for all digits going backwards