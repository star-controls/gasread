#!/usr/local/epics/modules/pythonIoc/pythonIoc

from softioc import softioc, builder
from softioc.softioc import dbpf

from gasread import gasread, gasread_tof

#TOF and TPC gas data
tofgas = gasread_tof("tof_gas.db", "/home/stargas/tof_gas_sys_data")
tpcgas = gasread("gas.db", "/home/stargas/tpc_gas_sys_data")

builder.LoadDatabase()
softioc.iocInit()

#TOF alarm limits

# gas alarms after talking with LK 04/05/09
# for fm1 

dbpf("tof_gas_FM-1.LOW", "180")
dbpf("tof_gas_FM-1.LOLO", "180")
dbpf("tof_gas_FM-1.HIGH", "2050")
dbpf("tof_gas_FM-1.HIHI", "2050")

dbpf("tof_gas_FM-2.LOW", "5")
dbpf("tof_gas_FM-2.LOLO", "5")

dbpf("tof_gas_PT-1.LOW", "5.5")
dbpf("tof_gas_PT-1.LOLO", "5")
dbpf("tof_gas_PT-1.HIGH", "20")
dbpf("tof_gas_PT-1.HIHI", "200")

dbpf("tof_gas_PT-2.LOW", "5")
dbpf("tof_gas_PT-2.LOLO", "0")
dbpf("tof_gas_PT-2.HIGH", "20")
dbpf("tof_gas_PT-2.HIHI", "200")

dbpf("tof_gas_PT-4.LOW", "30")
dbpf("tof_gas_PT-4.LOLO", "30")

# jp requested 
dbpf("tof_gas_PT-4.HIGH", "105")
dbpf("tof_gas_PT-4.HIHI", "110")


dbpf("tof_gas_iButh_fm.LOW", "3.5")
dbpf("tof_gas_iButh_fm.LOLO", "3.5")
dbpf("tof_gas_iButh_fm.HIGH", "3.5")
dbpf("tof_gas_iButh_fm.HIHI", "5.5")

# Added on 4/27/2017 by Jarda
dbpf("tof_gas_PT-2.LOW", "5.5")
dbpf("tof_gas_PT-2.LOLO", "4")

#TPC alarm limits

# Added the following limit changes on 1/24/2005 to silenc alarms due to High Wind
dbpf("cu_tpc_gas_PT-5.HIGH", "1.75")
dbpf("cu_tpc_gas_PT-5.HIHI", "1.8")
# Added the following limit changes on 3/02/2006 because of a bad sensor
 
dbpf("cu_tpc_gas_PI-13.HIGH", "4.3")
dbpf("cu_tpc_gas_PI-13.HIHI", "4.5")
# Added the following limit changes on 3/19/2006 because of a bad sensor
 
dbpf("cu_tpc_gas_PI-13.HIGH", "4.5")
dbpf("cu_tpc_gas_PI-13.HIHI", "4.5")


# added based on the request of JT 03/05/09
dbpf("cu_tpc_gas_PI-15.LOW", "0.8")
dbpf("cu_tpc_gas_PI-15.LOLO", "0.7")


# added based on the request of JT 03/05/09
dbpf("cu_tpc_gas_PI-8.LOW", "1.6")
dbpf("cu_tpc_gas_PI-8.LOLO", "1.4")

# added based on the request of AL 03/13/09
dbpf("cu_tpc_gas_CH4-M4.HIGH", "10.8")
dbpf("cu_tpc_gas_CH4-M4.HIHI", "10.9")


#end - wtw
# Added the following on 04/16/2007 to quiet a gas alarm due to extreme Hurricane type barametric pressures
dbpf("cu_tpc_gas_PT-B.LOW", "960")
dbpf("cu_tpc_gas_PT-B.LOLO", "955")


# Added the following limit changes on 1/24/2005 to silenc alarms due to High Wind
dbpf("cu_tpc_gas_PT-3.HIGH", "8.")
dbpf("cu_tpc_gas_PT-3.HIHI", "10.")

dbpf("cu_tpc_gas_PI-8.LOW", "1.2")
dbpf("cu_tpc_gas_PI-8.LOLO", "1.15")

# Added on 4/27/2017 by Jarda
dbpf("cu_tpc_gas_PI-14.HIGH", "150")
dbpf("cu_tpc_gas_PI-14.HIHI", "155")


softioc.interactive_ioc(globals())

