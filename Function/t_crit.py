data = [
    # 0.05  0.01     0.001
    [12.70,	 63.65,	 636.61],
    [4.303,	 9.925,	 31.602],
    [3.182,	 5.841,	 12.923],
    [2.776,	 4.604,	 8.610],
    [2.571,	 4.032,	 6.869],
    [2.447,	 3.707,	 5.959],
    [2.365,	 3.499,	 5.408],
    [2.306,	 3.355,	 5.041],
    [2.262,	 3.250,	 4.781],
	[2.228,	 3.169,	 4.587],
	[2.201,	 3.106,	 4.437],
	[2.179,	 3.055,	 4.318],
	[2.160,	 3.012,	 4.221],
	[2.145,	 2.977,	 4.140],
	[2.131,	 2.947,	 4.073],
	[2.120,	 2.921,	 4.015],
	[2.110,	 2.898,	 3.965],
	[2.101,	 2.878,	 3.922],
	[2.093,	 2.861,	 3.883],
	[2.086,	 2.845,	 3.850],
	[2.080,	 2.831,	 3.819],
	[2.074,	 2.819,	 3.792],
	[2.069,	 2.807,	 3.768],
	[2.064,	 2.797,	 3.745],
	[2.060,	 2.787,	 3.725],
	[2.056,	 2.779,	 3.707],
	[2.052,	 2.771,	 3.690],
	[2.049,	 2.763,	 3.674],
	[2.045,	 2.756,	 3.659],
	[2.042,	 2.750,	 3.646],
	[2.040,	 2.744,	 3.633],
	[2.037,	 2.738,	 3.622],
	[2.035,	 2.733,	 3.611],
	[2.032,	 2.728,	 3.601],
	[2.030,	 2.724,	 3.591],
	[2.028,	 2.719,	 3.582],
	[2.026,	 2.715,	 3.574],
	[2.024,	 2.712,	 3.566],
	[2.023,	 2.708,	 3.558],
	[2.021,	 2.704,	 3.551],
	[2.020,	 2.701,	 3.544],
	[2.018,	 2.698,	 3.538],
	[2.017,	 2.695,	 3.532],
	[2.015,	 2.692,	 3.526],
	[2.014,	 2.690,	 3.520],
	[2.013,	 2.687,	 3.515],
	[2.012,	 2.685,	 3.510],
	[2.011,	 2.682,	 3.505],
	[2.010,	 2.680,	 3.500],
	[2.009,	 2.678,	 3.496],
	[2.008,	 2.676,	 3.492],
	[2.007,	 2.674,	 3.488],
	[2.006,	 2.672,	 3.484],
	[2.005,	 2.670,	 3.480],
	[2.004,	 2.688,	 3.476],
	[2.003,	 2.667,	 3.473],
	[2.002,	 2.665,	 3.470],
	[2.002,	 2.663,	 3.466],
	[2.001,	 2.662,	 3.463],
	[2.000,	 2.660,	 3.460],
	[2.000,	 2.659,	 3.457],
	[1.999,	 2.657,	 3.454],
	[1.998,	 2.656,	 3.452],
	[1.998,	 2.655,	 3.449],
	[1.997,	 2.654,	 3.447],
	[1.997,	 2.652,	 3.444],
	[1.996,	 2.651,	 3.442],
	[1.995,	 2.650,	 3.439],
	[1.995,	 2.649,	 3.437],
	[1.994,	 2.648,	 3.435],
	[1.994,	 2.647,	 3.433],
	[1.993,	 2.646,	 3.431],
	[1.993,	 2.645,	 3.429],
	[1.993,	 2.644,	 3.427],
	[1.992,	 2.643,	 3.425],
	[1.992,	 2.642,	 3.423],
	[1.991,	 2.641,	 3.422],
	[1.991,	 2.640,	 3.420],
	[1.990,	 2.639,	 3.418],
	[1.990,	 2.639,	 3.416]
]


def getVal(alpha, n):
    if(alpha == 0.05):
        return data[n][0]
    if(alpha == 0.01):
        return data[n][1]
    if(alpha == 0.001):
        return data[n][2]
    return -1