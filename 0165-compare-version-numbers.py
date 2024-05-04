class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # maybe what we can do here is just split
        # string by dots?
        lv1, lv2 = version1.split('.'), version2.split('.')
        n = max(len(lv1), len(lv2))
        for i in range(n):
            # no additional space past dot? treat it as zero
            # otherwise convert to an int the components
            v1 = int(lv1[i]) if i < len(lv1) else 0
            v2 = int(lv2[i]) if i < len(lv2) else 0
            # specified return values
            if v1 < v2:
                return -1
            if v1 > v2:
                return 1
        # if we get here then versions are the same
        return 0
