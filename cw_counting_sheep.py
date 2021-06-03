"""Codewars: Counting sheep...
8 kyu

URL: https://www.codewars.com/kata/54edbc7200b811e956000556/

Consider an array of sheep where some sheep may be missing from their place.
We need a function that counts the number of sheep present in the array
(true means present).

For example,
[True,  True,  True,  False,
 True,  True,  True,  True ,
 True,  False, True,  False,
 True,  False, False, True ,
 True,  True,  True,  True ,
 False, False, True,  True]
The correct answer would be 17.

Hint: Don't forget to check for bad values like null/undefined
"""

def count_sheeps(arrayOfSheeps):
    """
    Iterate with a counter.

    Time complexity: O(n).
    Space complexity: O(1).
    """
    count = 0
    for sheep in arrayOfSheeps:
        if sheep is True:
            count += 1

    return count


def main():
    # Output: 17.
    arrayOfSheeps = [True,  True,  True,  False,
                     True,  True,  True,  True ,
                     True,  False, True,  False,
                     True,  False, False, True ,
                     True,  True,  True,  True ,
                     False, False, True,  True]
    print count_sheeps(arrayOfSheeps)


if __name__ == '__main__':
    main()
