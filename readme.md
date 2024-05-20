# Face Detection App

Welcome to the Face Detection App! This project leverages MediaPipe's Face Mesh solution to detect and visualize facial landmarks in both images and videos. Built with Streamlit for an interactive web interface, this application allows users to upload images or videos and see real-time face detection results.

## Features

- **Real-time face detection** in images and videos.
- **Customizable parameters** for maximum face detection and confidence levels.
- **Webcam support** for live face detection.
- **Recording capability** for video processing.
- **Responsive and interactive UI** using Streamlit.

## Installation

To get started, clone the repository and install the necessary dependencies.

```bash
git clone https://github.com/khushalrathore/aslinterpreter.git
cd ASLi
pip install -r requirements.txt
```

## Usage

Run the application using the following command:

```bash
streamlit run app.py
```

### Interface Overview

1. **Sidebar Menu**:
   - **About App**: Provides information about the app.
   - **Run on Image**: Upload an image to detect faces.
   - **Run on Video**: Upload a video or use a webcam for face detection.

2. **Main Panel**:
   - Displays results based on the selected mode (Image or Video).
   - Shows detected faces and other relevant information.

## Code Overview

The application consists of several key components:

1. **Importing Libraries**:
   - OpenCV, MediaPipe, Streamlit, and other necessary libraries are imported.

2. **Helper Functions**:
   - `image_resize`: Resizes images while maintaining aspect ratio.

3. **Streamlit Interface**:
   - Sidebar for mode selection and parameter adjustments.
   - Main panel for displaying results.

4. **Face Detection Logic**:
   - Uses MediaPipe's Face Mesh for processing images and videos.
   - Displays detected faces with visual landmarks.

## Example

### Running on Image

1. Select "Run on Image" from the sidebar.
2. Upload an image or use the default demo image.
3. Adjust parameters like maximum faces and detection confidence.
4. View the detected faces with landmarks in the main panel.

### Running on Video

1. Select "Run on Video" from the sidebar.
2. Upload a video, or use the webcam.
3. Adjust parameters like maximum faces, detection confidence, and tracking confidence.
4. View the real-time face detection results and optionally record the output.

## Acknowledgments

- **MediaPipe**: For providing the robust Face Mesh solution.
- **Streamlit**: For making web app development easy and interactive.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

This project showcases my ability to leverage powerful libraries like MediaPipe and Streamlit to build interactive and responsive web applications. Feel free to explore the code and provide feedback. Happy face detecting!