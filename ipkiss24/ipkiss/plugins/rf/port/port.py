from ipkiss.all import *
from math import cos, sin, pi
from ipkiss.log import IPKISS_LOG as LOG
from ipkiss.aspects.port.port import __InPort__, __OutPort__, __OrientedPort__,__OutOfPlanePort__
from ipkiss.plugins.rf.wg.definition import WaveguideDefCrossSectionProperty

from pysics.basics.domain import DomainProperty
from pysics.electromagnetics import RFDomain

class __RFPort:
    domain = DomainProperty(default=RFDomain)

class RFPort(__RFPort, __OrientedPort__):
    wg_definition = WaveguideDefCrossSectionProperty(
                        default = TECH.WGDEF.DEFAULT, 
                        doc = "Waveguide definition for the waveguide connecting to this port")

    corner1 = FunctionNameProperty(fget_name = "get_corner1")
    corner2 = FunctionNameProperty(fget_name = "get_corner2")

    def move_copy(self, coordinate):
        return self.__class__(position = self.position + coordinate, 
                              angle = self.angle_deg, 
                              wg_definition = self.wg_definition)

    def transform(self, transformation):
        if transformation.is_isometric():
            self.position = transformation.apply_to_coord(self.position)
            self.angle_deg = transformation.apply_to_angle_deg(self.angle_deg)
        else:
            self.position = transformation.apply_to_coord(self.position)
            self.angle_deg = transformation.apply_to_angle_deg(self.angle_deg)
            self.wg_definition = self.wg_definition.transform_copy(transformation)
        return self

    def transform_copy(self, transformation):
        if transformation.is_isometric():
            D = self.wg_definition
        else:
            D = self.wg_definition.transform_copy(transformation)
        return self.__class__(position = transformation.apply_to_coord(self.position), 
                              angle = transformation.apply_to_angle_deg(self.angle_deg), 
                              wg_definition = D)

    def flip(self):
        #gives RFPort in other direction
        return self.__class__(position = self.position, 
                              angle = (self.angle_deg+180.0)%360.0, 
                              wg_definition = self.wg_definition)

    def invert_copy(self):
        #changes the RFPort from InRFPort to OutRFPort. 
        # This is just added here for ease of coding
        return self.__invert_class__(position = self.position, 
                                     angle = self.angle_deg, 
                                     wg_definition = self.wg_definition)


    def is_match(self, other):
        return ((self.position == other.position) and
                (self.angle - other.angle) % 360.0 == 180.0 and
                (self.wg_definition == other.wg_definition) 
                )

    def __eq__(self, other):
        if not isinstance(other, RFPort): return False
        return (self.position==other.position and 
                (self.angle_deg == other.angle_deg) and
                (self.wg_definition == other.wg_definition)
                )


    def __ne__(self, other):
        return (self.position!=other.position or 
                (self.angle_deg != other.angle_deg) or
                (self.wg_definition != other.wg_definition)
                )

    def __repr__(self):
        return "<RFPort: (%f, %f), a=%f, D=%s>" %(self.position[0], self.position[1], self.angle_deg, self.wg_definition)

    def get_corner1(self):
        port_position = self.position
        port_angle = self.angle * DEG2RAD
        wg_width = self.wg_definition.wg_width
        port_corner1_x = port_position[0] + (wg_width / 2.0) * cos(port_angle-pi/2.0)
        port_corner1_y = port_position[1] + (wg_width / 2.0) * sin(port_angle-pi/2.0)
        corner1 = Coord3(port_corner1_x, port_corner1_y, 0) 
        return corner1

    def get_corner2(self):
        port_position = self.position
        port_angle = self.angle * DEG2RAD
        wg_width = self.wg_definition.wg_width
        port_corner2_x = port_position[0] + (wg_width / 2.0) * cos(port_angle+pi/2.0)
        port_corner2_y = port_position[1] + (wg_width / 2.0) * sin(port_angle+pi/2.0)
        corner2 = Coord3(port_corner2_x, port_corner2_y, 0) 
        return corner2       

RFPort.__invert_class__ = RFPort

class InRFPort(RFPort, __InPort__):
    pass

class OutRFPort(RFPort, __OutPort__):
    __invert_class__ = InRFPort

InRFPort.__invert_class__ = OutRFPort

def RFPortProperty(internal_member_name=None, restriction=None, **kwargs):
    """Property type for storing an RFPort"""
    R = RestrictType(RFPort) & restriction
    return RestrictedProperty(internal_member_name, restriction=R, **kwargs)
