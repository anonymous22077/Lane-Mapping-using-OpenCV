# Lane-Mapping-using-OpenCV
<u>Real-Time Lane Detection Using OpenCV:</u>
<br>
<br>
<b>Overview</b>
<br>
This project demonstrates real-time lane detection in road videos using OpenCV and Python. The program applies Canny Edge Detection and Hough Line Transformation to highlight lane lines on the road. Customizable trackbars allow you to adjust parameters in real-time, enhancing the accuracy of lane detection.
<br>
<br>
<b>Features:</b>
<br>
<pre>
  Real-Time Lane Detection: Detects lanes in each frame of the video, allowing for smooth, continuous lane mapping.
  Adjustable Parameters: Trackbars enable on-the-fly adjustment of line color, line thickness, edge detection thresholds, and other Hough Transform settings.
  Region of Interest: Focuses on a defined area of the image to improve detection accuracy.
</pre>
<br>
<b><Demo:</b>

Note: If GitHub doesn’t support the video format, consider linking to an external video hosting site like YouTube or converting the video to a GIF format.

Dependencies
To run this project, install the required libraries:

plaintext
Copy code
opencv-python
numpy
Install dependencies via:

bash
Copy code
pip install -r requirements.txt
Project Structure
plaintext
Copy code
- src/
   - lane_mapping.py          # Main code file
- videos/
   - road_view_demo.mp4       # Sample video for demonstration
- README.md
- requirements.txt            # List of dependencies
How to Run
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/lane-mapping.git
Navigate to the Directory:

bash
Copy code
cd lane-mapping/src
Run the Program:

bash
Copy code
python lane_mapping.py
Use the Road view2.mp4 video file or replace it with any other road video for lane detection.

Trackbar Controls
RED, GREEN, BLUE: Adjust the color of the detected lane lines.
Low Threshold & High Threshold: Control Canny Edge Detection sensitivity.
Threshold: Minimum number of intersections in Hough Space to consider a line.
Min Line Length: Minimum line length for line segments.
Max Line Gap: Maximum gap between lines to connect them.
Line Thickness: Adjust the thickness of the detected lane lines.
Code Explanation
region_of_interest: Masks the image to only show the region of interest.
draw_the_lines: Draws the detected lines on the image based on Hough Transform results.
process: Applies grayscale conversion, Gaussian blur, edge detection, and Hough Transform to detect lane lines in each frame.
Example Images

Contributing
Feel free to open issues or pull requests to contribute to this project.

License
This project is licensed under the MIT License.
