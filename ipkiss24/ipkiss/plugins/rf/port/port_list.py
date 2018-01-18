from ipkiss.geometry.transformable import *
from ipkiss.all import *
from .port import RFPort
from ipkiss.aspects.port.port_list import PortList, PortListProperty

class RFPortList(PortList):
    __item_type__ = RFPort
    port_angle_decision = FloatProperty(default = 90.0)
    
    def get_in_ports(self):
        from .port import InRFPort
        pl = self.__class__()
        for p in self:
            if isinstance(p, InRFPort):
                pl.append(p)
        return pl
    in_ports = property(get_in_ports)

    def get_out_ports(self):
        from .port import OutRFPort
        pl = self.__class__()
        for p in self:
            if isinstance(p, OutRFPort):
                pl.append(p)
        return pl
    out_ports = property(get_out_ports)

class RFPortListProperty(PortListProperty):
    __list_type__ = RFPortList
