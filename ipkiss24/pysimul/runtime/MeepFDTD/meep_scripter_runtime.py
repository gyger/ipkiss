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


########################## LICENSE ####################################################################
### THIS FILE IS LICENSED UNDER THE GPL LICENSE AND IS NOT PART OF THE IPKISS SOFTWARE FRAMEWORK   ####
### A Python-Meep script that was generated by MeepScripter will need this module for execution    ####
### (c) Ghent University - imec - 2011                                                             ####
#######################################################################################################

try:
    import meep as meep
except ImportError, e:
    try :
        import meep_mpi as meep
    except ImportError, e:
        raise Exception("Modules 'meep' or 'meep_mpi' not found.")    


import h5py
import math
import numpy


class __MeepMaterialPolygonsFromFile__(object):  
    def __init__(self):
        self.south_west_coord = 0.0

    def __getstate__(self): #for pickle : do not serialize
        return None    

    def __transform_coords_to_numpy_array(self, coords):
        transformed_coords = []
        for c in coords :
            x = c[0] - self.south_west_coord[0]
            y = c[1] - self.south_west_coord[1]
            transformed_coords.append([x,y])
        arr = numpy.array(transformed_coords)
        arr = arr[:-1]
        return arr

    def __add_bitmap_polygon__(self, bitmap_polygon, value):
        #value : will be an eps for 2D and a material stack ID for 3D...
        if not (bitmap_polygon is None):
            georep = bitmap_polygon.georep_list
            for g in georep:
                if not g.is_empty:
                    if g.is_ring:
                        coords = g.boundary.coords			
                        coords_array = self.__transform_coords_to_numpy_array(coords)								
                        self.add_polygon(coords_array, value)		    
                    else:
                        outer_polygon_coords_array = self.__transform_coords_to_numpy_array(g.exterior.coords)
                        outer_polygon = self.add_polygon(outer_polygon_coords_array, value)
                        for ip in g.interiors:
                            #inner polygons
                            inner_polygon_coords_array = self.__transform_coords_to_numpy_array(ip.coords)
                            outer_polygon.add_inner_polygon(inner_polygon_coords_array)	


class MeepMaterial2DPolygonsFromFile(__MeepMaterialPolygonsFromFile__, meep.PolygonCallback2D):  

    def __get_config_from_file__(self, file_name):
        file_handle = open(file_name, "r")
        from cPickle import load
        (bitmap_polygons, eps_values, south_west) = load(file_handle)
        file_handle.close()
        return (bitmap_polygons, eps_values, south_west)


    def __init__(self, config_file, meep_volume):
        meep.PolygonCallback2D.__init__(self)
        (bitmap_polygons, eps_values, south_west) = self.__get_config_from_file__(config_file)
        self.south_west_coord = south_west
        for bitmap_polygon, eps in zip(bitmap_polygons, eps_values)[1:]: #ignore canvas polygon
            self.__add_bitmap_polygon__(bitmap_polygon, eps)



class MeepMaterial3DPolygonsFromFile(__MeepMaterialPolygonsFromFile__, meep.PolygonCallback3D):  

    def __get_config_from_file__(self, file_name):
        file_handle = open(file_name, "r")
        from cPickle import load	
        (bitmap_polygons, material_stack_ids, south_west, material_stacks_npy, n_o_material_stacks) = load(file_handle)
        file_handle.close()
        return (bitmap_polygons, material_stack_ids, south_west, material_stacks_npy, n_o_material_stacks)     

    def __init__(self,  config_file, meep_volume):
        meep.PolygonCallback3D.__init__(self)
        (bitmap_polygons, material_stack_ids, south_west, material_stacks_npy, n_o_material_stacks)  = self.__get_config_from_file__(config_file)
        self.south_west_coord = south_west
        self.add_material_stacks_from_numpy_matrix(material_stacks_npy,n_o_material_stacks)
        for bitmap_polygon, material_stack_id in zip(bitmap_polygons,material_stack_ids)[1:]: #ignore canvas polygon
            self.__add_bitmap_polygon__(bitmap_polygon, material_stack_id)



class AmplitudeFactorFromFile(meep.Callback):
    def __init__(self, config_file):
        meep.Callback.__init__(self)
        self.mode_profile = self.__get_config_from_file__(config_file)

    def __get_config_from_file__(self, file_name):	
        from cPickle import load
        file_handle = open(file_name, 'r')
        mode_profile = load(file_handle)
        return mode_profile

    def __get_amplitude_factor__(self, coordinate_relative_to_port_position):
        positions = self.mode_profile[0]
        fields = self.mode_profile[1]
        from scipy.interpolate import interp1d as interp
        i = interp(x = positions, y = fields, kind = 'linear', copy = True, bounds_error = False, fill_value = 0.0)	
        f = float(i(coordinate_relative_to_port_position[1]))	
        return f

    def complex_vec(self,vec):
        #BEWARE, these are coordinates RELATIVE to the source center !!!!
        try:
            x = vec.x()
            y = vec.y()
            factor = self.__get_amplitude_factor__([x,y])	
            if (isinstance(factor, complex)):
                return factor
            else:
                return complex(factor)
        except Exception, e:
            print "Exception in AmplitudeFactor::complex_vec (%f,%f): %s" %(x,y,e)
            raise e