def calcMean(list: numList) -> int:
    '''Calculates the mean of a given list of integers'''
    l = sorted(numList)
    return int((l[0] + l[-1]) / 2)
def calcMode(numList):
    pass
def calcMedian(numList):
    size = len(numList)
    if size % 2 == 0:
        median = numList[int(size / 2)]
    else:
        x,y = int(size / 2),int(size/2 + 1)
        median = (numList[x] + numList[y]) / 2
    return median

# List with odd number of elements
nums1 = [i for i in range(13)]
# List with even number of elements
nums2 = [i for i in range(22)]
# Manually selecting nums
nums3 = [22, 43, 22, 99, 22, 13, 2, 13, 22]

print(calcMedian(nums1), calcMean(nums1))
print(calcMedian(nums2), calcMean(nums2))
print(calcMedian(nums3), calcMean(nums3))