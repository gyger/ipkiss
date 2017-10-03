# IPKISS - Parametric Design Framework
# Copyright (C) 2002-2012  Ghent University - imec
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
# 
# i-depot BBIE 7396, 7556, 7748
# 
# Contact: ipkiss@intec.ugent.be



from ipkiss.all import *
from picazzo.wg.tapers.linear import WgElTaperLinear
from ipkiss.plugins.photonics.wg.basic import WgElDefinition
from ipkiss.plugins.photonics.wg.connect import __RoundedWaveguide__, __RoundedShape__
from ipkiss.plugins.photonics.wg.definition import WaveguideDefProperty
from ipkiss.plugins.photonics.routing.to_line import RouteToWestAtY, RouteToEastAtY
from ipkiss.plugins.photonics.routing.connect import RouteConnectorRounded
from ..adapter import IoBlockAdapter
from ipkiss.plugins.photonics.port.port import OpticalPort

# this class should be generated by a metaclass defining its class properties, so it becomes easy to define custom adapters
class IoCleave(__RoundedShape__, IoBlockAdapter):
    __name_prefix__ = "IoCleave"
    taper_length = PositiveNumberProperty(default = 300.0)
    wg_definition = WaveguideDefProperty(default=WgElDefinition(wg_width=3.0))
    connect_length = PositiveNumberProperty(default = 40.0)
    min_straight = NonNegativeNumberProperty(default = TECH.WG.SHORT_STRAIGHT)
    block_trench_position = PositiveNumberProperty(default = 650.0)
    block_trench_width = PositiveNumberProperty(default = 5.0)

    def define_elements(self, elems):
        # go over ports
        for i in range(len(self.struct_west_ports)):
            ip = self.struct_west_ports[i]
            
            # position tapers
            t_pos = (ip.position[0] - self.connect_length, self.__y_west__[i])

            T = WgElTaperLinear(start_position = t_pos, end_position = (t_pos[0] - self.taper_length, t_pos[1]), 
                                start_wg_def = ip.wg_definition,
                                end_wg_def = self.wg_definition)

            elems += T
            # draw straight waveguides            
            elems += self.wg_definition(shape = [T.west_ports[0].position, (0.0, t_pos[1])])
            # generic connector between structure port and taper port
            R = RouteToWestAtY(input_port = ip, 
                               y_position = T.east_ports[0].y, 
                               bend_radius = self.bend_radius, 
                               min_straight = self.minimum_straight, 
                               rounding_algorithm = self.rounding_algorithm)
            R.end_straight += R.out_ports[0].x - T.east_ports[0].x
            elems += RouteConnectorRounded(R)
            #blocking trenches
            elems += Line(PPLayer(self.wg_definition.process, TECH.PURPOSE.DF.TRENCH), 
                          (self.block_trench_position, 0.5*self.wg_definition.wg_width + self.wg_definition.trench_width), (self.block_trench_position, 0.5 * self.y_spacing), 
                          self.block_trench_width)
            elems += Line(PPLayer(self.wg_definition.process, TECH.PURPOSE.DF.TRENCH), 
                          (self.block_trench_position, -0.5*self.wg_definition.wg_width - self.wg_definition.trench_width), (self.block_trench_position, -0.5 * self.y_spacing), 
                          self.block_trench_width)

        for i in range(len(self.struct.east_ports)):
            op = self.struct_east_ports[i]
            # position tapers
            t_pos = (op.position[0] + self.connect_length, self.__y_east__[i])
            T = WgElTaperLinear(start_position = t_pos, end_position = (t_pos[0] + self.taper_length, t_pos[1]), 
                                start_wg_def = op.wg_definition, end_wg_def = self.wg_definition)
            elems += T
            # draw straight waveguides            
            elems += self.wg_definition(shape = [T.east_ports[0].position, (self.width, t_pos[1])])
            
            # generic connector between structure port and taper port
            R = RouteToEastAtY(input_port = ip, 
                               y_position = T.west_ports[0].y, 
                               bend_radius = self.bend_radius, 
                               min_straight = self.minimum_straight, 
                               rounding_algorithm = self.rounding_algorithm)
            R.end_straight += -R.out_ports[0].x + T.west_ports[0].x
            elems += RouteConnectorRounded(R)
            
        return elems

    def define_ports(self, ports):
        # should reflect number of in and outputs in center structure
        ports += [OpticalPort(position = (0.0, ypos), wg_definition = self.wg_definition, angle = 180.0) for ypos in self.__y_west__]
        ports += [OpticalPort(position = (self.width, ypos), wg_definition = self.wg_definition, angle = 180.0) for ypos in self.__y_east__]
        return ports
    
    
