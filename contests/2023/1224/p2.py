from typing import *

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9 + 7
        hFences.extend([1, m])
        vFences.extend([1, n])
        hFences.sort()
        vFences.sort()
        h_diff = set()
        v_diff = set()
        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                h_diff.add(hFences[j] - hFences[i])

        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                v_diff.add(vFences[j] - vFences[i])

        ans = -1
        for num in h_diff:
            if num in v_diff:
                ans = max(ans, num)
        if ans == -1:
            return ans
        else:
            return ((ans % MOD) ** 2) % MOD


sl = Solution()
examples = [
    (4, 3, [2,3], [2], 4),
    (6, 7, [2], [4], -1),
    (1187, 9893, [258,238,1167,566,491,644,857,1059,860,749,628,182,12,304,1065,62,95,28,534,624,1186,1138,1032,620,438,961,323,716,106,293,892,856,1175,90,648,1049,451,448,24,461,563,840,1148,841,154,631,1024,948,342,454,870,848,1168,194,5,113,551,719,1182,380,66,666,352,347,285,834,525,296,803,682,687,886,379,142,398,31,764,320,528,128,345,487,104,664,389,838,994,974,227,7,196,667,239,1160,299,990,946,420,779,351,1083,467,819,721,138,941,220,283,393,773,30,817,918,996,1026,1036,1052,16,536,884,1183,96,344,202,741,822,183,3,756,724,395,1103,193,681,613,506,429,810,61,440,594,626,684,653,565,203,1115,422,569,328,1110,504,83,733,505,850,346,516,921,866,508,1001,406,11,1116,750,1102,502,214,435,805,308,638,187,260,972,1090,387,482,474,593,1077,1143,492,224,371,873,647,632,48,230,550,1174,839,341,413,147,815,1027,1042,15,471,416,188,711,526,409,985,57,88,549,441,81,1157,878,598,759,910,981,917,400,655,885,599,568,348,513,662,637,1121,1033,472,1010,567,1108,329,970,40,896,895,651,801,877,1069,1126,103,229,1176,601,332,745,201,358,524,725,829,82,576,795,943,179,242,360,1022,888,280,696,35,652,241,232,1043,1137,1095,674,934,1120,25,715,709,431,675,898,361,752,769,1106,207,68,437,798,940,1123,1091,427,1158,1111,1117,1089,418,425,87,760,1124,178,259,1129,767,597,671,1028,49,864,470,570,704,19,85,231,29,165,1068,963,288,557], [3591,1665,4738,6500,9879,5396,9180,3669,9474,3662,8178,8032,5291,9522,7073,5223,5568,5951,2055,8197,2643,7440,4915,4972,4884,2075,8934,1099,7711,2301,6160,4004,7608,3073,7235,2787,8249,3636,7828,3465,7433,526,7172,6650,4817,598,917,3972,2923,7604,2490,5582,6271,9221,627,3311,4596,4699,4237,9486,2889,6221,6000,4444,1148,311,8154,2486,4028,8218,2554,8957,9012,7761,597,1168,4637,8603,107,6813,7263,795,3172,661,3385,2029,2083,3992,6709,4419,4885,907,6576,8468,4463,8513,6582,3084,1165,1209,1667,9009,8420,6232,4794,7999,977,5332,8414,3224,9437,8622,5251,2584,863,1883,7938,3696,5006,727,9497,2296,7972,2979,1612,4793,4207,5846,2734,2371,1911,9514,707,902,1671,2683,8722,9511,3502,3244,3279,298,96,49,2352,3445,1633,4982,1726,5377,3374,5341,9516,429,4194,7890,5343,903,7818,1280,1863,3877,2583,2574,5313,2629,7827,3479,3331,7663,470,292,1536,2283,9808,8673,1870,5160,7186,2892,7736,4874,1437,6515,5221,6178,8590,649,3469,1318,1955,9543,6632,4383,6244,2084,2095,9370,3418,6006,4926,1418,8204,6176,9661,8040,2391,8873,4415,4713,7704,4218,9457,3682,7127,2652,7812,9731,6685,9739,2565,9550,2147,6814,2044,5537,7277,3436,9252,5275,4029,1581,7779,85,3698,8569,2035,8827,8050,5262,1271,6844,2205,2658,3809,5616,1032,9537,6527,2174,3916,704,2502,5814,6629,7977,4346,7790,3929,3126,914,6791,2242,3612,1912,5327,6578,2074,2888,6181,6794,3403,9258,5394,1557,2487,8328,2277,5815,2415,3597,1567,9223,6481,1602,9452,6329,9507,4749,1137,7564,9534,5987,6567,9303,8348,1565,1012,1689,7213,6788,6409,7005,7567,6039,333,7814,5570,300,7249,783,7472,7404,8989,5657,4344,4830,6302,6424,2720,9598,2796,943,5360,4946,5139,9345,2580,6013,1024,3419,7418,5843,4312,6873,8401,2336,9580,9542,8656,2105,3753,8396,9662,20,4863,1951,8086,6848,4307,4083,3900,1086,9403,1027,2141,4805,4686,766,7420,9603,8411,8544,8753,7931,4390,1879,4239,2393,782,7451,4508,1066,9028,4629,6825,3167,8901,6879,3654,7477,3834,9878,7168,2885,8935,9727,4795,1854,6429,4595,6439,4311,161,2350,7607,8466,9869,4725,4692,6047,4422,1232,516,3286,697,2573,1298,123,8769,4469,4403,6872,8159,5193,6731,3983,3595,7359,2501,9052,4283,7039,1948,2383,9182,5867,6532,3090,2315,8799,1362,8233,5215,1191,2582,6071,3607,7524,2457,2626,2614,564,1105,6109,9759,2738,3788,3442,7550,3280,8652,7312,3590,2822,9892,3574,1981,6864,1611,1045,7343,163,1153,7833,2924,6413,1660,7636,4081,734,1164,9812,1517,4844,3320,5617,684,1605,2798,1186,7747,3008,3277,6891,7036,3560,2621,639,7592,8691], 0)
]
for example in examples:
    m, n, h, v, ans = example
    print(f"Output: {sl.maximizeSquareArea(m, n, h, v)}, Ans: {ans}")