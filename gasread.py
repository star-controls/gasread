
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from threading import Timer

from softioc.builder import aIn, records, PP
from softioc import alarm

from db_utils import db_load

class gasread(object):
    #_____________________________________________________________________________
    def __init__(self, dbname, basedir):
        #load records from the original TOF and TPC gas database
        self.pvs = db_load(dbname)
        #data files received from gas room
        inputs = [basedir+"/input"+str(i) for i in xrange(1,21)]
        #watch for input data files to update
        file_handler = PatternMatchingEventHandler(patterns=inputs)
        file_handler.on_modified = self.on_modified
        self.observer = Observer()
        self.observer.schedule(file_handler, path=basedir, recursive=False)
        self.observer.start()
        #timer to detect no updates from gas room
        self.timeout = 60 # sec
        self.timer = Timer(self.timeout, self.set_invalid)
        self.timer.start()

    #_____________________________________________________________________________
    def on_modified(self, event):
        #print("New data in " + event.src_path)
        #load input data to the records
        inp = open(event.src_path, "r")
        for line in inp:
            namval = line.split()
            self.pvs.get(namval[0]).set(float(namval[1]))
        inp.close()
        #reset timer after reading the input data from gas room
        self.reset_timer()

    #_____________________________________________________________________________
    def reset_timer(self):
        self.timer.cancel()
        self.timer = Timer(self.timeout, self.set_invalid)
        self.timer.start()

    #_____________________________________________________________________________
    def set_invalid(self):
        #mark all PVs as invalid
        for i in self.pvs.itervalues():
            i.set_alarm(alarm.INVALID_ALARM, alarm.TIMEOUT_ALARM)


class gasread_tof(gasread):
    #_____________________________________________________________________________
    def __init__(self, dbname, basedir):
        #call to base init
        super(gasread_tof, self).__init__(dbname, basedir)

        #create addidional calc records for isobuthane fractions in TOF and MTD
        self.c1 = self.make_fm_calc("MTD_FM2dFM1", "MTD_FM-2", "MTD_FM-1")
        self.c2 = self.make_fm_calc("tof_fm2dfm1", "tof_gas_FM-2", "tof_gas_FM-1")

    #_____________________________________________________________________________
    def make_fm_calc(self, name, anam, bnam):
        cx = records.calc(name, CALC="A/B", PREC=3, HOPR=0.065)
        inpa = self.pvs.get(anam)
        inpb = self.pvs.get(bnam)
        cx.INPA = inpa.name + " MS"
        cx.INPB = inpb.name + " MS"
        inpa.FLNK = PP(cx)
        inpb.FLNK = PP(cx)
        cx.EGU = "percent"
        cx.HIHI = 0.06
        cx.HIGH = 0.057
        cx.HHSV = "MAJOR"
        cx.HSV = "MINOR"


