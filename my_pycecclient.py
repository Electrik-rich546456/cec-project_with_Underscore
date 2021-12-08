#! /usr/bin/python3
import cec
num = ""
class pyCecClass(*num):
    
    cecconfig = cec.libcec_configuration()
    lib = {}
    # create a new libcec_configuration
    def SetConfiguration(self):
        self.cecconfig.strDeviceName   = "Richards-Pc"
        self.cecconfig.bActivateSource = 0
        self.cecconfig.deviceTypes.Add(cec.CEC_DEVICE_TYPE_RECORDING_DEVICE)
        self.cecconfig.clientVersion = cec.LIBCEC_VERSION_CURRENT
    def DetectAdapter(self):        
        retval = None
        adapters = self.lib.DetectAdapters()
#        print(self.lib.DetectAdapters())
        for adapter in adapters:            
              retval = adapter.strComName
#        print (retval)
        return retval
    def InitLibCec(self,  *num):
        self.lib = cec.ICECAdapter.Create(self.cecconfig)
        # print libCEC version and compilation information
        # print("libCEC version " + self.lib.VersionToString(self.cecconfig.serverVersion) + " loaded: " + self.lib.GetLibInfo())
        # search for adapters
        adapter = self.DetectAdapter()
#        print(adapter)
#        print(self.DetectAdapter())
        if adapter == None:
            print("No adapters found")
        else:
            if self.lib.Open(adapter):
#                print(self.lib.Open(adapter))
                for n in num:
                    if n == 1:
                        self.Hdmione()
                    if n == 2:
#                        pass
                        self.Hdmitwo()
                    if n == 3:
                        self.Hdmithree()
                    if n == 4:
                        self.power_toggle()
                    
#                print("connection opened")
#                self.MainLoop()
            else:
                print("failed to open a connection to the CEC adapter")
    # send an active source message
    def ProcessCommandActiveSource(self):
        self.lib.SetActiveSource()
    # send a standby command
    def ProcessCommandStandby(self):
        self.lib.StandbyDevices(cec.CECDEVICE_BROADCAST)
#---------------------------------------------------------------------My edits-----------------    
  # send a power on command
    def ProcessCommandpoweron(self):
        self.lib.PowerOnDevices(cec.CECDEVICE_BROADCAST)
        return
    def Hdmione(self):
        self.ProcessCommandTx('4F:82:10:00')
        return
    #    "4F:82:10:00"
    def Hdmitwo(self):
        self.ProcessCommandTx('4F:82:30:00')
        return
    def Hdmithree(self):
        self.ProcessCommandTx('4F:82:20:00')
        return
#---------------------------------------------------------------------------------------------
# send a custom command like source switch
    def ProcessCommandTx(self, data):
        cmd = self.lib.CommandFromString(data)
#        print(cmd)
        print("transmit " + data)
        if self.lib.Transmit(cmd):
            print("command sent")
            exit
        else:
            print("failed to send command")
    def power_toggle(self):
        addresses = self.lib.GetActiveDevices()
        #    activeSource = self.lib.GetActiveSource()
        x = 0
        if addresses.IsSet(x):
            power  = self.lib.GetDevicePowerStatus(x)
            x += 1
            global pow
            if power:
                self.ProcessCommandpoweron()
            else:
                self.ProcessCommandStandby()    
    # main loop, do commands
    def MainLoop(self):
#        self.power_toggle() # power toggle
#        self.Hdmione()
#        self.Hdmitwo()                         # self explanotory
#        self.Hdmithree()
        pass

    def __init__(self):
        self.SetConfiguration()
#        print(self.SetConfiguration())
#print(__name__)
if __name__ == '__main__':
    # initialise libCEC
    lib =  pyCecClass()
    lib.InitLibCec(2)
#    print(__name__)
