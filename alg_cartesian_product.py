"""Cartesian product."""

class CartesianProduct(object):
    def _product_two(self, nums1, nums2):
        two_products = []

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if isinstance(nums1[0], list):
                    # nums1[i] is a list.
                    two_products.append(nums1[i] + [nums2[j]])
                else:
                    # nums1[0] is not a list, i.e. nums1 is a list.
                    two_products.append([nums1[i]] + [nums2[j]])

        return two_products


    def repeated_product(self, nums, repeat):
        # Created repeated numbers as pool for Cartesian product.
        repeated_nums = [nums for _ in range(repeat)]

        result = repeated_nums[0]
        for r in range(1, repeat):
            result = self._product_two(result, repeated_nums[r])
        return result

    def product(self, nums):
        result = nums[0]
        for r in range(1, len(nums)):
            result = self._product_two(result, nums[r])
            return result


def main():
    nums = [1, 2, 3]
    repeat = 2
    print CartesianProduct().repeated_product(nums, repeat)

    nums = [[1, 2, 3], [4, 5]]
    print CartesianProduct().product(nums)


if __name__ == '__main__':
    main()
