1. create an empty list for the _values_

## PROGRAM __solution__ of _number_ with _base_
// This function will always return a number which represents an ID and they all have to be unique

1. APPEND _number_ to _values_
1. SORT _number_ DESCENDING AND save it as a string on _x_
1. SORT _number_ ASCENDING AND save it as a string on _y_
1. __substract__ _x_ and _y_ of given _base_ AND save it on _z_
1. IF the number is repeated at least 4 times:
    1. save its distance from last one
    1. IF a preceeding number is repeated at least twice and with the same distance
        1. if all the numbers between those pairs are repeated with the same distance at least twice, RETURN the distance
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

## PROGRAM the _values_ __recycle__
1. we have an ever-growing infinite list
1. the problem is that there might be a part in the beginning where it doesn't repeat,
1. check for the first two consequent numbers that are repeated
1. when that pair has been returned for a third and fourth time, and it's in the same distance, AND the numbers in between repeat, return that distance.
1. else, do the same for the subsequent pair which is different from that one


v[0] = N
v[1] = x - y where x desc and y asc digits of N
in general:
v[n] = x - y where x desc and y asc digits of v[n - 1]
