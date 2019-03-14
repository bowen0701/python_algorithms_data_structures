from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


"""Make Change.

Compute how many distinct ways you can make change that amount.
Assume that you have an infinite number of each kind of coin.
"""


def make_change_recur(amount, coins):
    """Make change by recursion.

    Time complexity: O(2^n).
    Space complexity: O(1).
    """
    if amount < 0:
        return 0
    if amount == 0:
        return 1

    # When number of coins is 0 but there is still amount remaining.
    n = len(coins)
    if n <= 0 and amount >= 1:
        return 0

    # Compute ways with coin n included plus that with coin excluded.
    count_in = make_change_recur(amount - coins[n - 1], coins)
    count_ex = make_change_recur(amount, coins[:(n - 1)])
    count = count_in + count_ex
    return count


def _make_change_memo(amount, coins, T):
    """Helper function for make_change_memo()."""
    if amount == 0:
        return 1
    if amount < 0:
        return 0

    n = len(coins)
    if n <= 0 and amount >= 1:
        return 0

    count_in = _make_change_memo(amount - coins[n - 1], coins, T)
    count_ex = _make_change_memo(amount, coins[:(n - 1)], T)
    T[n - 1][amount] = count_in + count_ex

    return T[n - 1][amount]


def make_change_memo(amount, coins):
    """Make change by top-bottom dynamic programming: 
    recursion + memoization.

    Time complexity: O(a * c), where a is amount, and c is number of coins.
    Space complexity: O(a * c).
    """
    n = len(coins)
    T = [[0] * (amount + 1) for c in range(n)]

    for c in range(n):
        T[c][0] = 1

    return _make_change_memo(amount, coins, T)


def make_change_dp(amount, coins):
    """Make change by bottom-up dynamic programming.

    Time complexity: O(a * c), where a is amount, and c is number of coins.
    Space complexity: O(a * c).
    """
    n = len(coins)
    T = [[0] * (amount + 1) for c in range(n)]

    for c in range(n):
        T[c][0] = 1

    for c in range(n):
        for a in range(1, amount + 1):
            if a >= coins[c]:
                count_in = T[c][a - coins[c]]
            else:
                count_in = 0

            if c >= 1:
                count_ex = T[c - 1][a]
            else:
                count_ex = 0

            T[c][a] = count_in + count_ex

    return T[-1][-1]


def main():
    import time

    amount = 5
    coins = [1, 2, 3]    # Ans = 5.

    start_time = time.time()
    print('Make change by recursion: {}'
          .format(make_change_recur(amount, coins)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('Make change by memo: {}'
          .format(make_change_memo(amount, coins)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('Make change by DP: {}'
          .format(make_change_dp(amount, coins)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
