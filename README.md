
# TEZZERACT Simulation

This project simulates the projection of a 4D hypercube (tesseract) onto a 2D plane using Pygame. The code applies 4D rotation transformations and projects the result onto 3D and 2D spaces, visualizing the process in real-time. The simulation creates an interactive graphical display of a rotating 4D cube, with edge connections between vertices.

## Features

- **4D Cube Simulation**: Rotates a tesseract (4D cube) in 4D space and projects it onto a 2D plane.
- **Interactive Visualization**: Uses Pygame to render the 2D projection of the 4D cube and rotate it in real time.
- **Custom Matrix Operations**: Includes a custom matrix multiplication function to handle 4D and 3D transformations.
- **Real-Time Rotation**: The cube rotates continuously with smooth transitions and can be customized by adjusting rotation speeds.

## Prerequisites

Before running the project, ensure you have the following dependencies installed:

- Python 3.x
- Pygame library (can be installed using `pip`)

To install Pygame, run the following command:

```bash
pip install pygame
```

## How to Run the Project

1. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/yourusername/4d-cube-projection.git
   cd 4d-cube-projection
   ```

2. Install the required dependencies using `pip` (as mentioned in the prerequisites).

3. Run the main script to launch the simulation:

   ```bash
   python main.py
   ```

   This will open a Pygame window with the rotating 4D cube projection.

## Controls

- **Escape Key**: Close the simulation.
- **Adjust Speed**: Modify the speed of rotation in the `speed` variable in the code.

## How It Works

- **Matrix Multiplication**: The simulation relies on matrix operations to perform the 4D rotations and projections. The custom `matrix_multiplication` function handles the matrix multiplication for transforming the cube's vertices.
  
- **4D Rotations**: Several rotation matrices are defined for rotating the 4D cube around various axes. These matrices are applied to the cube's vertices, resulting in the desired transformation.
  
- **Projection**: After performing the rotation, the coordinates of the cube's vertices are projected onto a 2D plane by applying a perspective projection matrix.

- **Rendering**: The vertices are rendered as circles, and edges between them are drawn using lines, giving a visual representation of the cube in 2D space.

## Contributing

Feel free to fork this repository and submit pull requests for improvements, bug fixes, or new features. All contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
