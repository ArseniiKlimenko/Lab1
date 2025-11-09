import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

lynx = np.array([
[209.70, 368.42], [157.63, 332.16], [118.82, 284.21], [80.95, 224.56], [43.08, 244.44], [20.36, 266.67], [-4.26, 293.57], [2.37, 263.16], [-20.36, 292.40], [-39.29, 299.42], [-21.30, 259.65],
[-50.65, 267.84], [-39.29, 242.11], [-55.38, 240.94], [-100.83, 300.58], [-149.11, 345.03], [-172.78, 361.40], [-189.82, 300.58], [-192.66, 225.73], [-181.30, 145.03], [-168.05, 104.09], [-184.14, 66.67],
[-186.98, 31.58], [-183.20, 3.51], [-208.76, -4.68], [-197.40, -29.24], [-182.25, -44.44], [-203.08, -43.27], [-172.78, -92.40], [-131.12, -126.32], [-101.78, -147.37], [-74.32, -163.74], [-110.30, -224.56],
[-143.43, -287.72], [-161.42, -240.94], [-282.60, -221.05], [-388.64, -205.85], [-370.65, -301.75], [-339.41, -397.66], [18.46, -397.66], [345.09, -400.00], [359.29, -378.95], [367.81, -342.69], [346.98, -362.57], [363.08, -302.92], [357.40, -243.27], [348.88, -266.67], [336.57, -201.17], [290.18, -135.67], [240.00, -118.13], [258.93, -164.91], [257.99, -228.07], [252.31, -271.35], [256.09, -333.33],
[247.57, -359.06], [230.53, -307.60], [194.56, -238.60], [160.47, -181.29], [120.71, -149.71], [165.21, -132.16], [201.18, -100.58], [183.20, -99.42], [221.07, -73.68], [253.25, -24.56], [222.01, -23.39],
[251.36, -1.17], [262.72, 24.56], [234.32, 25.73], [214.44, 42.11], [202.13, 60.82], [220.12, 101.75], [234.32, 160.23], [240.00, 230.41], [232.43, 316.96], [209.70, 368.42]
]).T

def plot_2d(X_copy, A, title):
    transformed = (A @ X_copy)
    plt.figure(figsize=(8, 8))
    plt.title(title)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.plot(X_copy[0], X_copy[1], 'black', label='Original')
    plt.plot(transformed[0], transformed[1], 'blue', label='Transformed')
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend()
    plt.show()

    return transformed

def stretch(X, a, b):
    X_copy = X.copy()
    A = np.array([[a, 0],
                  [0, b]])
    print(f"\nStretch a={a}, b={b}")
    transformed_matrix = plot_2d(X_copy, A, f"Stretched by a={a}, b={b}")
    print(f"Result matrix:\n{transformed_matrix[:, :5]},")

def shear(X, a, b):
    X_copy = X.copy()
    A = np.array([[1, a],
                  [b, 1]])
    print(f"\nShear a={a}, b={b}")
    transformed_matrix = plot_2d(X_copy, A, f"Shear by a={a}, b={b}")
    print(f"Result matrix:\n{transformed_matrix[:, :5]},")

def reflection(X, a, b):
    X_copy = X.copy()
    A = (1 / (a**2 + b**2)) * np.array([[a**2 - b**2, 2 * a * b],
                                      [2 * a * b, b**2 - a**2]])
    print(f"\nReflection by a={a}, b={b} ")
    transformed_matrix = plot_2d(X_copy, A, f"Reflection by a={a}, b={b}")
    print(f"Result matrix:\n{transformed_matrix[:, :5]},")

def rotation(X, degrees):
    X_copy = X.copy()
    radians = np.radians(degrees)
    cos = np.cos(radians)
    sin = np.sin(radians)
    A = np.array([[cos, -sin],
                  [sin, cos]])
    print(f"\nRotation degrees={degrees}")
    transformed_matrix = plot_2d(X_copy, A, f"Rotation by degrees={degrees}")
    print(f"Result matrix:\n{transformed_matrix[:, :5]},\n")

#Test task1
stretch(lynx, 2, 3)
shear(lynx, 2, 3)
reflection(lynx, 1, 1)
rotation(lynx, 80)

print("Test task2")
print("Rotate(45), Shear(0.7, 0), Stretch(1.6, 0.7)")
Stretch_matrix = np.array([[1.6, 0],
                          [0, 0.7]])
Shear_matrix = np.array([[1, 0.7],
                          [0, 1]])

rad_45 = np.radians(45)
cos= np.cos(rad_45)
sin = np.sin(rad_45)
Rotation_matrix = np.array([[cos, -sin],
                            [sin, cos]])

print("\nStretch - Shear - Rotate")

print("\nStretch\n")
matrix1 = plot_2d(lynx, Stretch_matrix, "1. Stretch")
print(f"New lynx {matrix1[:, :5]}")

print("\nShear\n")
matrix2 = plot_2d(matrix1, Shear_matrix, "1.2: Stretch - Shear")
print(f"New lynx {matrix2[:, :5]}")

print("\nRotation\n")
matrix3 = plot_2d(matrix2, Rotation_matrix, "1.3 (Final): Stretch - Shear - Rotate")
print(f"New lynx {matrix3[:, :5]}")


print("\nRotate - Shear - Stretch")

print("\nRotation\n")
matrix1_combo2 = plot_2d(lynx, Rotation_matrix, "2.1: Rotate")
print(f"New lynx {matrix1_combo2[:, :5]}")

print("\nShear\n")
matrix2_combo2 = plot_2d(matrix1_combo2, Shear_matrix, "2.2: Rotate - Shear")
print(f"New lynx {matrix2_combo2[:, :5]}")

print("\nStretch\n")
matrix3_combo2 = plot_2d(matrix2_combo2, Stretch_matrix, "2.3 (Final): Rotate - Shear - Stretch")
print(f"New lynx {matrix3_combo2[:, :5]}")


print("\nShear - Stretch - Rotate")

print("\nShear\n")
matrix1_combo3 = plot_2d(lynx, Shear_matrix, "3.1: Shear")
print(f"New lynx {matrix1_combo3[:, :5]}")

print("\nStretch\n")
matrix2_combo3 = plot_2d(matrix1_combo3, Stretch_matrix, "3.2: Shear - Stretch")
print(f"New lynx {matrix2_combo3[:, :5]}")

print("\nRotation\n")
matrix3_combo3 = plot_2d(matrix2_combo3, Rotation_matrix, "3.3 (Final): Shear - Stretch - Rotate")
print(f"New lynx {matrix3_combo3[:, :5]}\n")


#Reading the .off file
def read_off(filename: str):
    with open(filename, 'r') as f:
        if 'OFF' != f.readline().strip():
            raise ValueError('Not a valid OFF header')
        n_verts, n_faces, _ = map(int, f.readline().strip().split())
        verts = [list(map(float, f.readline().strip().split())) for i in range(n_verts)]
        faces = [list(map(int, f.readline().strip().split()[1:])) for i in range(n_faces)]
    return np.array(verts), faces

def plot_off(vertices, transformed, faces, title):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    mesh = Poly3DCollection([vertices[face] for face in faces], alpha=0.2, edgecolor='black')
    ax.add_collection3d(mesh)
    mesh_transformed = Poly3DCollection([transformed[face] for face in faces], alpha=0.4, edgecolor='blue')
    ax.add_collection3d(mesh_transformed)
    ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], s=2, c='r')
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title(title)
    max_range = np.array([vertices[:, 0].max() - vertices[:, 0].min(),
                          vertices[:, 1].max() - vertices[:, 1].min(),
                          vertices[:, 2].max() - vertices[:, 2].min()]).max() / 2.0

    mid_x = (vertices[:, 0].max() + vertices[:, 0].min()) * 0.5
    mid_y = (vertices[:, 1].max() + vertices[:, 1].min()) * 0.5
    mid_z = (vertices[:, 2].max() + vertices[:, 2].min()) * 0.5
    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)

    plt.show()

def rotate_xy_3d(X, degrees):
    X_copy = X.copy()
    radians = np.radians(degrees)
    cos = np.cos(radians)
    sin = np.sin(radians)
    A = np.array([[cos, -sin, 0],
                  [sin, cos, 0],
                  [0, 0, 0]])

    transformed = (A @ X_copy.T).T
    return transformed, A

def rotate_yz_3d(X, degrees):
    X_copy = X.copy()
    radians = np.radians(degrees)
    cos = np.cos(radians)
    sin = np.sin(radians)
    A = np.array([[1, 0, 0],
                  [0, cos, -sin],
                  [0, sin, cos]])
    transformed = (A @ X_copy.T).T
    return transformed, A

def rotate_xz_3d(X, degrees):
    X_copy = X.copy()
    radians = np.radians(degrees)
    cos = np.cos(radians)
    sin = np.sin(radians)
    A = np.array([[cos, 0, -sin],
                    [0, 1, 0],
                  [sin, 0, cos]])
    transformed = (A @ X_copy.T).T
    return transformed, A

file_path = "toilet_0007.off"
car_vertices, car_faces = read_off(file_path)
plot_off(car_vertices, car_vertices, car_faces, f"Original ({file_path})")

print("Task 3")
print("XY rotation(90 degrees)")
rotated_car_xy, A = rotate_xy_3d(car_vertices, 90)
print(f"Rotation xy matrix:\n {A}")
plot_off(car_vertices, rotated_car_xy, car_faces, "Rotation xy")

print("YZ rotation(90 degrees)")
rotated_car_yz, A = rotate_yz_3d(car_vertices, 90)
print(f"Rotation yz matrix:\n {A}")
plot_off(car_vertices, rotated_car_yz, car_faces, "Rotation yz")

print("XZ rotation(90 degrees)")
rotated_car_xz, A = rotate_xz_3d(car_vertices, 90)
print(f"Rotation xz matrix:\n {A}")
plot_off(car_vertices, rotated_car_xz, car_faces, "Rotation xz")

print("Task 4")

print("\n4.1: Matrix XY(30)")
change1, A1 = rotate_xy_3d(car_vertices, 30)
print(f"Rotation xy matrix:\n {A1}")
plot_off(car_vertices, change1, car_faces, "Original - Rotation XY(30)")

print("\n4.2: Matrix YZ(45)")
change2, A2 = rotate_yz_3d(change1, 45)
print(f"Rotation yz matrix:\n {A2}")
plot_off(change1, change2, car_faces, "Original - Rotation XY(30) - Rotation YZ(45)")

print("\n4.3: Matrix XZ (60)")
change3, A3 = rotate_xz_3d(change2, 60)
print(f"Rotation xz matrix:\n {A3}")
plot_off(change2, change3, car_faces, "Original - Rotation XY(30) - Rotation YZ(45) - Rotation XZ(60)")

A_composite = A3 @ A2 @ A1
plot_off(car_vertices, change3, car_faces, "Final result")
print(f"Final composite matrix:\n {A_composite}")






