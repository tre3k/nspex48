#!/usr/bin/env python
# -*- coding:utf-8 -*-

__all__ = ["PEX48", "PEX48Class", "main"]

__docformat__ = 'restructuredtext'

import PyTango
import sys
from tango import DevState

# Add additional import
#----- PROTECTED REGION ID(PEX48.additionnal_import) ENABLED START -----#

import pex48client

#----- PROTECTfrom tango import DevStateED REGION END -----#	//	PEX48.additionnal_import

# Device States Description
# No states for this device


class PEX48 (PyTango.LatestDeviceImpl):
    """NICOS server for PCI-bus digitizer PEX48"""
    
    # -------- Add you global variables here --------------------------
    #----- PROTECTED REGION ID(PEX48.global_variables) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	PEX48.global_variables

    def __init__(self, cl, name):
        PyTango.LatestDeviceImpl.__init__(self,cl,name)
        self.debug_stream("In __init__()")
        PEX48.init_device(self)
        #----- PROTECTED REGION ID(PEX48.__init__) ENABLED START -----#
        # need chagne ip addr and port. localhost:22224
        self._pex48c = pex48client.pex48client("localhost",22224)

        #self.dev = PyTango.DeviceProxy("device/counter/pex48")
        self.set_state(DevState.STANDBY)
        #----- PROTECTED REGION END -----#	//	PEX48.__init__
        
    def delete_device(self):
        self.debug_stream("In delete_device()")
        #----- PROTECTED REGION ID(PEX48.delete_device) ENABLED START -----#
        #----- PROTECTED REGION END -----#	//	PEX48.delete_device

    def init_device(self):
        self.debug_stream("In init_device()")
        self.get_device_properties(self.get_device_class())
        self.attr_value_read = 0
        self.attr_preselection_read = 0.0
        self.attr_active_read = False
        self.attr_version_read = ""
        #----- PROTECTED REGION ID(PEX48.init_device) ENABLED START -----#
        self.set_state(DevState.STANDBY)        
        #----- PROTECTED REGION END -----#	//	PEX48.init_device

    def always_executed_hook(self):
        self.debug_stream("In always_excuted_hook()")
        #----- PROTECTED REGION ID(PEX48.always_executed_hook) ENABLED START -----#
        #----- PROTECTED REGION END -----#	//	PEX48.always_executed_hook

    # -------------------------------------------------------------------------
    #    PEX48 read/write attribute methods
    # -------------------------------------------------------------------------
    
    def read_value(self, attr):
        self.debug_stream("In read_value()")
        #----- PROTECTED REGION ID(PEX48.value_read) ENABLED START -----#
        self.attr_value_read = self._pex48c.read()
        #self.attr_value_read = int(self.dev.read_attribute("value").value)
        attr.set_value(self.attr_value_read)
        #----- PROTECTED REGION END -----#	//	PEX48.value_read
        
    def read_preselection(self, attr):
        self.debug_stream("In read_preselection()")
        #----- PROTECTED REGION ID(PEX48.preselection_read) ENABLED START -----#
        self.attr_preselection_read = 1
        attr.set_value(self.attr_preselection_read)
        #----- PROTECTED REGION END -----#	//	PEX48.preselection_read
        
    def write_preselection(self, attr):
        self.debug_stream("In write_preselection()")
        data = attr.get_write_value()
        #----- PROTECTED REGION ID(PEX48.preselection_write) ENABLED START -----#
        #----- PROTECTED REGION END -----#	//	PEX48.preselection_write
        
    def read_active(self, attr):
        self.debug_stream("In read_active()")
        #----- PROTECTED REGION ID(PEX48.active_read) ENABLED START -----#
        self.attr_active_read = False
        attr.set_value(self.attr_active_read)
        #----- PROTECTED REGION END -----#	//	PEX48.active_read
        
    def write_active(self, attr):
        self.debug_stream("In write_active()")
        data = attr.get_write_value()
        #----- PROTECTED REGION ID(PEX48.active_write) ENABLED START -----#
        #----- PROTECTED REGION END -----#	//	PEX48.active_write
        
    def read_version(self, attr):
        self.debug_stream("In read_version()")
        #----- PROTECTED REGION ID(PEX48.version_read) ENABLED START -----#
        self.attr_version_read = '1'
        attr.set_value(self.attr_version_read)
        #----- PROTECTED REGION END -----#	//	PEX48.version_read

    def read_attr_hardware(self, data):
        self.debug_stream("In read_attr_hardware()")
        #----- PROTECTED REGION ID(PEX48.read_attr_hardware) ENABLED START -----#
        #----- PROTECTED REGION END -----#	//	PEX48.read_attr_hardware


    # -------------------------------------------------------------------------
    #    PEX48 command methods
    # -------------------------------------------------------------------------
    
    def Clear(self):
        """ Clears all values of the detector.
        """
        self.debug_stream("In Clear()")
        #----- PROTECTED REGION ID(PEX48.Clear) ENABLED START -----#
        #self.dev.command_inout("CleanMemory")
        #----- PROTECTED REGION END -----#	//	PEX48.Clear
        
    def GetProperties(self):
        """ Returns a string list of properties and their values, in the form [prop1, val1, prop2, val2, …].
        :rtype: PyTango.DevVarStringArray
        """
        self.debug_stream("In GetProperties()")
        argout = [""]
        #----- PROTECTED REGION ID(PEX48.GetProperties) ENABLED START -----#
        argout = dev.get_property(dev.get_property_list('*'))
        #----- PROTECTED REGION END -----#	//	PEX48.GetProperties
        return argout
        
    def SetProperties(self, argin):
        """ Returns True if the properties were saved persistently, False if they were only set for the current session. Set properties on the device. The argument must have the same form as the return value of “GetProperties”, but not all properties have to be present.
        :param argin: arg
        :type argin: PyTango.DevVarStringArray
        :rtype: PyTango.DevBoolean
        """
        self.debug_stream("In SetProperties()")
        argout = True
        #----- PROTECTED REGION ID(NsMotor.SetProperties) ENABLED START -----#
        dev.put_property(argin)
        #----- PROTECTED REGION END -----#	//	NsMotor.SetProperties
        return argout

    def Off(self):
        """ Switches the main function of the device off.
        """
        self.debug_stream("In Off()")
        #----- PROTECTED REGION ID(PEX48.Off) ENABLED START -----#
        self.set_state(DevState.OFF)
        #----- PROTECTED REGION END -----#	//	PEX48.Off
        
    def On(self):
        """ Switches the main function of the device on.
        """
        self.debug_stream("In On()")
        #----- PROTECTED REGION ID(PEX48.On) ENABLED START -----#
        self.set_state(DevState.ON)
        #----- PROTECTED REGION END -----#	//	PEX48.On
        
    def Prepare(self):
        """ Prepares the acquisition, so that a Start command can start it immediately.
        """
        self.debug_stream("In Prepare()")
        #----- PROTECTED REGION ID(PEX48.Prepare) ENABLED START -----#
        self.set_state(DevState.ON)
        #----- PROTECTED REGION END -----#	//	PEX48.Prepare
        
    def Reset(self):
        """ Resets the device to overcome a FAULT state.
        """
        self.debug_stream("In Reset()")
        #----- PROTECTED REGION ID(PEX48.Reset) ENABLED START -----#
        #self.dev.command_inout("Init")
        self.set_state(DevState.STANDBY)
        #----- PROTECTED REGION END -----#	//	PEX48.Reset
        
    def Resume(self):
        """ Prepares the acquisition, so that a Start command can start it immediately.
        """
        self.debug_stream("In Resume()")
        #----- PROTECTED REGION ID(PEX48.Resume) ENABLED START -----#
        self.set_state(DevState.ON)
        #self.dev.command_inout("Start")
        #----- PROTECTED REGION END -----#	//	PEX48.Resume
        
    def Start(self):
        """ Starts the acquisition
        """
        self.debug_stream("In Start()")
        #----- PROTECTED REGION ID(PEX48.Start) ENABLED START -----#
        #self.dev.command_inout("Start")
        print("Start!")
        self._pex48c.start()
        
        #----- PROTECTED REGION END -----#	//	PEX48.Start
        
    def Stop(self):
        """ Stops a running acquisition.
        """
        self.debug_stream("In Stop()")
        #----- PROTECTED REGION ID(PEX48.Stop) ENABLED START -----#
        #self.dev.command_inout("Stop")
        #print("Stop!")
        self._pex48c.stop()
        #----- PROTECTED REGION END -----#	//	PEX48.Stop
        

    #----- PROTECTED REGION ID(PEX48.programmer_methods) ENABLED START -----#
    #----- PROTECTED REGION END -----#	//	PEX48.programmer_methods

class PEX48Class(PyTango.DeviceClass):
    # -------- Add you global class variables here --------------------------
    #----- PROTECTED REGION ID(PEX48.global_class_variables) ENABLED START -----#
    #----- PROTECTED REGION END -----#	//	PEX48.global_class_variables


    #    Class Properties
    class_property_list = {
        }


    #    Device Properties
    device_property_list = {
        }


    #    Command definitions
    cmd_list = {
        'Clear':
            [[PyTango.DevVoid, "none"],
            [PyTango.DevVoid, "none"]],
        'GetProperties':
            [[PyTango.DevVoid, "none"],
            [PyTango.DevVarStringArray, "none"]],
        'SetProperties':
            [[PyTango.DevVarStringArray, "arg"],
            [PyTango.DevBoolean, "none"]],
        'Off':
            [[PyTango.DevVoid, "none"],
            [PyTango.DevVoid, "none"]],
        'On':
            [[PyTango.DevVoid, "none"],
            [PyTango.DevVoid, "none"]],
        'Prepare':
            [[PyTango.DevVoid, "none"],
            [PyTango.DevVoid, "none"]],
        'Reset':
            [[PyTango.DevVoid, "none"],
            [PyTango.DevVoid, "none"]],
        'Resume':
            [[PyTango.DevVoid, "none"],
            [PyTango.DevVoid, "none"]],
        'Start':
            [[PyTango.DevVoid, "none"],
            [PyTango.DevVoid, "none"]],
        'Stop':
            [[PyTango.DevVoid, "none"],
            [PyTango.DevVoid, "none"]],
        }


    #    Attribute definitions
    attr_list = {
        'value':
            [[PyTango.DevULong64,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'description': "Current counter value.",
            } ],
        'preselection':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'description': "Current preset value",
                'Memorized':"true"
            } ],
        'active':
            [[PyTango.DevBoolean,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'description': "If this channel can finish the measurement when preselection is reached.",
            } ],
        'version':
            [[PyTango.DevString,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'description': "This attribute contains the version of the device class and its parent classes (recursively). The format is “module1 version1, module2 version2, …”.",
            } ],
        }


def main():
    try:
        py = PyTango.Util(sys.argv)
        py.add_class(PEX48Class, PEX48, 'PEX48')
        #----- PROTECTED REGION ID(PEX48.add_classes) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	PEX48.add_classes

        U = PyTango.Util.instance()
        U.server_init()
        U.server_run()

    except PyTango.DevFailed as e:
        print ('-------> Received a DevFailed exception:', e)
    except Exception as e:
        print ('-------> An unforeseen exception occured....', e)

if __name__ == '__main__':
    main()
