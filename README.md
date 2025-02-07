#ColorEncoder

ColorEncoder is a Python-based application that converts images into height maps based on color channel contributions. It also generates histograms of pixel values from the height map for analysis.

#Features
	•	Load an image into the application
	•	Display the original image on the left side of the canvas
	•	Convert the image into a height map based on color channel contributions
	•	Display the generated height map on the right side of the canvas
	•	Create and display a histogram of pixel values in the height map
	•	Save both the height map and histogram as PNG files

#Installation

Ensure you have Python installed (version 3.6 or higher). Install the required dependencies using:
pip install -r requirements.txt

#Usage

#Running the Application

Run the script using the following command:
python ColorEncoder.py

#Workflow
	1.	Load an Image
	•	Click the “Load Image” button to select an image from your device.
	•	The selected image will appear on the left side of the canvas.
	2.	Automatic Height Map Generation
	•	Once the image is loaded, it is immediately converted into a height map based on color channel contributions.
	•	The height map is displayed on the right side of the canvas.
	3.	Histogram Generation
	•	A histogram of the pixel values in the height map is created.
	•	It is displayed between or below the two images, depending on the window size.
	4.	Saving Results
	•	Click the “Save Height Map” button to save the height map as a PNG file.
	•	Click the “Save Histogram” button to save the histogram as a PNG file.
