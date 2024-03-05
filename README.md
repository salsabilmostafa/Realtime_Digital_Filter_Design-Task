# Custom Digital Filter Design Application

This desktop application allows users to design custom digital filters by placing zeros and poles on the z-plane. It provides an intuitive interface with interactive features for modifying filter elements and visualizing frequency responses. Additionally, users can apply the designed filter to real-time signals and correct phase distortions using All-Pass filters.

## Features

### Z-Plane Plotting
- Plot the z-plane with the unit circle.
- Place zeros and poles on the z-plane.
- Modify placed zeros/poles by dragging.
- Click on a zero or pole to delete it.
- Clear all zeros, clear all poles, or clear all.
- Option to add conjugates for complex elements.

### Frequency Response Plotting
- Display magnitude and phase response graphs corresponding to the placed elements.

### Real-Time Filtering
- Apply the filter to a lengthy signal in real-time.
- Graph to show the time progress of the original signal.
- Graph to show the time progress of the filtered signal.
- Control the speed/temporal-resolution of the filtering process with a slider.
- Input an arbitrary real-time signal using mouse movement.

### Phase Correction with All-Pass Filters
- Library of all-pass filters with visualization (zero-pole combination and phase response).
- Select and add all-pass filters to the original design.
- Custom-built all-pass: input an arbitrary "a" to calculate its phase response and integrate it with the library.
- Enable/disable added all-pass elements via a drop-down menu or checkboxes.

## Demo


https://github.com/salsabilmostafa/Realtime_Digital_Filter_Design-Task/assets/115428975/273714cc-1e45-44ae-9a11-31420d4c6309


## Usage

1. Clone the repository.

    ```bash
    git clone https://github.com/your-username/Realtime_Digital_Filter_Design-Task.git
    ```

2. Run the application.

    ```bash
    python Digital_Filter.py
    ```

3. Explore the features provided by the digital filter design application.

## Dependencies

Ensure you have the following dependencies installed before running the application:

- Python 3.7 or above
- PyQt5
- pyqtgraph
- sys
- function
- math
- warnings
- numpy
- scipy

## Contributions

Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.
