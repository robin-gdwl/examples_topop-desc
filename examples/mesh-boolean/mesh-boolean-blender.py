from compas.geometry import Box
from compas.geometry import Translation
from compas.datastructures import Mesh
from compas.datastructures import mesh_quads_to_triangles

from compas_blender.artists import MeshArtist

import compas_libigl as igl

# ==============================================================================
# Input Geometry
# ==============================================================================

a = Box.from_width_height_depth(5.0, 3.0, 1.0)
b = Box.from_width_height_depth(1.0, 5.0, 3.0)

a = Mesh.from_shape(a)
b = Mesh.from_shape(b)

mesh_quads_to_triangles(a)
mesh_quads_to_triangles(b)

# ==============================================================================
# Booleans
# ==============================================================================

A = a.to_vertices_and_faces()
B = b.to_vertices_and_faces()

C = igl.mesh_union(A, B)
c_union = Mesh.from_vertices_and_faces(*C)

C = igl.mesh_intersection(A, B)
c_intersection = Mesh.from_vertices_and_faces(*C)

C = igl.mesh_difference(A, B)
c_diff = Mesh.from_vertices_and_faces(*C)

# ==============================================================================
# Visualization
# ==============================================================================

c_union.transform(Translation([7.5, 0, 0]))
c_intersection.transform(Translation([15, 0, 0]))
c_diff.transform(Translation([22.5, 0, 0]))

