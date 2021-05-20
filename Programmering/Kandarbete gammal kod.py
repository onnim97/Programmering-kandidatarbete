"""
def movingaverage(interval, window_size):
    window = np.ones(int(window_size)) / float(window_size)
    return np.convolve(interval, window, 'same')

Centeredmovingav = movingaverage(LTStimeseries,12)
Centeredmovingav = Centeredmovingav[6:-6]


deseasonalization1 = LTStimeseries[6:-6]
deseasonalizationallyears1 = []
k = 0
for p in range(0, years):
    deseasonalizationayear = []
    for j in range(0, 12):
        deseasonalizationayear.append(LTStimeseries[k + j] / float(monthseasonalaverages[j]))
    k += 4
    deseasonalizationallyears.append(deseasonalizationayear)

deseasonalization = np.array(deseasonalizationallyears)
deseasonalization = np.hstack(deseasonalization)
"""
"""
mylist = LTStimeseries
N = 3
cumsum, moving_aves = [0], []

for l, x in enumerate(mylist, 1):
    cumsum.append(cumsum[l - 1] + x)
    if l >= N:
        moving_ave = (cumsum[l] - cumsum[l - N]) / N
        # can do stuff with moving_ave here
        moving_aves.append(moving_ave)

moving_aves = np.array(moving_aves)
"""

"""
ax = plt.axes(projection=ccrs.PlateCarree())
ax.stock_img()
ax.coastlines()
ax.gridlines()
ax.set_xticks([-180,-120 ,-60 ,0, 60, 120, 180], crs=ccrs.PlateCarree())
ax.set_yticks([-80 , -40 , 0 , 40 ,80], crs=ccrs.PlateCarree())
lon_formatter = LongitudeFormatter(zero_direction_label=True)
lat_formatter = LatitudeFormatter()
ax.xaxis.set_major_formatter(lon_formatter)
ax.yaxis.set_major_formatter(lat_formatter)
currentAxis = plt.gca()
regionleftcorners = [0, -20, -90, -20, -130, 20, 95, -35, -35, 15]
for i in range(0, len(regionleftcorners), 2):
    currentAxis.add_patch(
        Rectangle((regionleftcorners[i], regionleftcorners[i + 1],), 10, 10, fc="None", color='black', linewidth=2,
                  linestyle="-"))
plt.tight_layout(pad=0.3, h_pad=0.3, w_pad=0.3)


plt.show()
"""