import rasterio
import csv


#---------------------------------------------------
# create ply file that contains 2 element types: vertex, face
# from rasterio object (opened geotiff file)
#---------------------------------------------------

def create_ply(data, slice):

	elev_band = data.read(1)

	elev_band = elev_band[:slice, :slice]

	vertices = []
	faces = []

	num_verts = 0
	num_faces = 0

	width = elev_band.shape[0]
	height = elev_band.shape[1]

	print(f"width: {width} , height: {height}")

	for x in range(width):

		for y in range(height):

			vertex = [x, y, 0, 0, 0, 0, elev_band[x,y]]
			vertices.append(vertex)

			num_verts+=1

			# index vertices for quads
			if x > 0 and y > 0:

				right_top = (x * height) + y 
				left_top = right_top - height 

				right_bottom = right_top - 1
				left_bottom = left_top - 1


				face = [4, left_bottom, left_top, right_top, right_bottom]


				num_faces+=1

				faces.append(face)

	print(f'num vertices {num_verts} - num faces {num_faces}')
	return vertices, faces


if __name__ == "__main__":

	data = rasterio.open('USGS_13_n37w119_20240207.tif')

	vertices, faces = create_ply(data, 100)

	header = ("ply\n"
	"format ascii 1.0\n"
	"comment created by PolyEditor\n"
	"comment modified by pythonply\n"
	f"element vertex {len(vertices)}\n"
	"property float64 x\n"
	"property float64 y\n"
	"property float64 z\n"
	"property float64 vx\n"
	"property float64 vy\n"
	"property float64 vz\n"
	"property float64 s\n"
	f"element face {len(faces)}\n"
	"property list uint8 int32 vertex_indices\n"
	"end_header\n")

	print(f'writing {len(vertices)} vertices, {len(faces)} faces')

	with open("geo_test2.ply", 'w') as f:
		
		f.write(header)
		vertex_str = ""
		for v in vertices:
			line = ' '.join(map(str, v))
			line += '\n'
			vertex_str += line

		f.write(vertex_str)

		face_str = ""
		for face in faces:
			line = ' '.join(map(str, face))
			line += '\n'
			face_str += line

		f.write(face_str)

