from ipkiss.all import *
from .port import *
from .port_list import *
from ipkiss.aspects.port.port_list import PortListProperty, PortList
from ipkiss.aspects.aspect import __Aspect__
from ipkiss.aspects.port.aspect import PortAspect, TransformablePortAspect
from ipkiss.primitives.elements.basic import __Element__
from ipkiss.primitives.elements import SRef, ARef
from pysics.electromagnetics import RFDomain

class RFPortAspect(PortAspect):
    
    def define_rf_ports(self, ports):
        pl = RFPortList()
        for p in self.ports.get_ports_on_domain(RFDomain):
            pl.append(p)
        return pl
    rf_ports = RFPortListProperty(locked = True)

    def define_rf_in_ports(self):
        return self.rf_ports.in_ports
    rf_in_ports = RFPortListProperty(locked = True)

    def define_rf_out_ports(self):
        return self.rf_ports.out_ports
    rf_out_ports = RFPortListProperty(locked = True)
    
    def get_rf_ports_within_angles(self, start_angle, end_angle):
        p = self.rf_ports
        return p.get_ports_within_angles(start_angle,end_angle)

    def define_rf_west_ports(self):
        return self.get_rf_ports_within_angles(180.0 - 0.5 * self.port_angle_decision, 180.0 + 0.5 * self.port_angle_decision)
    rf_west_ports = RFPortListProperty(locked = True)

    def define_rf_east_ports(self):
        return self.get_rf_ports_within_angles(-0.5 * self.port_angle_decision, +0.5 * self.port_angle_decision)
    rf_east_ports = RFPortListProperty(locked = True)

    def define_rf_north_ports(self):
        return self.get_rf_ports_within_angles(90.0 - 0.5*self.port_angle_decision, 90.0 + 0.5 * self.port_angle_decision)
    rf_north_ports = RFPortListProperty(locked = True)

    def define_rf_south_ports(self):
        return self.get_rf_ports_within_angles(270.0 - 0.5*self.port_angle_decision, 270.0 + 0.5 * self.port_angle_decision)
    rf_south_ports = RFPortListProperty(locked = True)
    
    def get_rf_ports_on_process(self, process):
        return self.rf_ports.get_ports_on_process(process)

    def get_rf_ports_from_labels(self, labels):
        return self.rf_ports.get_ports_from_labels(labels)

    def get_rf_ports_not_from_labels(self, labels):
        return self.rf_ports.get_ports_not_from_labels(labels)

class RFPortListAspect(__Aspect__):    
    def define_rf_ports(self):
        pl = RFPortList()
        for p in self.get_ports_on_domain(RFDomain):
            pl.append(p)
        return pl
    rf_ports = property(define_rf_ports)
    
class TransformableRFPortAspect(RFPortAspect, StoredTransformable):
    def define_rf_ports(self, ports):
        return RFPortAspect.define_rf_ports(ports).transform_copy(self.transformation)
 
class SRefRFPortAspect(TransformableRFPortAspect):
    def define_rf_ports(self, ports):
        ports = self.reference.rf_ports.transform_copy(self.transformation).move(self.position).transform(-self.transformation)
        return ports

class ARefRFPortAspect(TransformablePortAspect):
    def define_rf_ports(self, ports):
        for p in self.positions:
            port_list = self.reference.rf_ports.transform_copy(self.transformation).move(p).transform(-self.transformation)
            ports.extend(port_list)
        return ports
            
PortList.mixin_first(RFPortListAspect)    
Structure.mixin_first(RFPortAspect)
__Element__.mixin_first(TransformableRFPortAspect)
SRef.mixin_first(SRefRFPortAspect)
ARef.mixin_first(ARefRFPortAspect)


        
    