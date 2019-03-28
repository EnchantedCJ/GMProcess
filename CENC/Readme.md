# CENC地震动处理

Describe: 处理txt格式CENC地震动

Author: CJ

Last update: 2019.03.28

## 地震动文件格式

### 格式1：有时间列

	# INSTRUMENT TYPE: etna
	# serial_number: 5567
	# start time: 2018-09-04 05:53:16.000000
	# sample rate: 200
	# 
	0.00000000,3.79227018,-1.39669202,-9.63466959
	0.00500000,3.96534777,-1.33824324,-9.62812176
	0.01000000,4.10053539,-1.30691469,-9.60193042
	...

使用`CENC_GMs_Process_with_t.py`

### 格式2：无时间列

	# INSTRUMENT TYPE: etna
	# serial_number: 5478
	# start time: 2018-09-12 19:07:01.000000
	# sample rate: 200
	# 
	-7.81312607,-6.89156196,-23.92110733
	-7.80610997,-6.88172290,-23.91362409
	-7.81265833,-6.88359700,-23.91736571
	...

使用`CENC_GMs_Process_without_t.py`，**默认sample rate=200，如有变化请注意修改**

### 格式3：无时间列+有经纬度

	# stla:38.21  stlo:100.05
	# stationID: 63ZMS
	# start time: 2019-03-28 05:48:39
	# sample rate: 200
	# DataZ	DataE	DataN
	# 
	-20.54377779,-14.42029247,-29.60097418
	-20.54938662,-14.42497286,-29.61031850
	...

使用`CENC_GMs_Process_without_t_loc.py`

## 使用说明

- 将脚本放在txt格式地震动所在文件夹下
- 运行脚本
- 在脚本所在目录生成台站名文件夹，每个文件夹下三向地震动