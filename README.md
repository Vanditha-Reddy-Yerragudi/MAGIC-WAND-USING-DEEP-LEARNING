# MAGIC-WAND-USING-DEEP-LEARNING

## **Overview**  
The **Virtual Pen System** is an interactive software that enables users to **write or draw in the air** using a simple marker or pointer. Built using **OpenCV and Computer Vision**, it allows real-time **gesture-based interaction** without requiring a touchscreen. The system detects hand movements, converts them into digital strokes, and provides an intuitive way to write, draw, or erase on a virtual canvas.  

### **Key Applications:**  
**Artists** – Create freehand digital sketches effortlessly.  
**Educators & Presenters** – Annotate and explain concepts interactively.  
**Handwriting Recognition** – Convert air-written text into English or local languages.  

## **System Specifications**  

### **Software Requirements**  
**OpenCV** – For computer vision and marker detection.  
**Computer Vision** – For real-time tracking and drawing.  

### **Hardware Requirements**  
**Colored Pen/Marker** – Used for gesture-based drawing.  
**Camera** – Captures marker movements and tracks coordinates.  

### **Tools Used**  
**Spyder IDE** – Development environment for Python-based implementation.  

## **Methodology**  

### **Algorithm Steps:**  
**Find the HSV Range of the Target Marker**  
   - Convert RGB to HSV format for better color detection.  
   - Save the color range values in a `.py` file.  

**Apply Color Masking**  
   - Filter out the target marker from the background using HSV thresholding.  

**Track the Marker’s Position**  
   - Use **contour detection** to get the marker’s x,y coordinates.  

**Draw in Real-Time**  
   - Connect the previous x,y coordinates to the new ones, forming strokes.  

**Implement Eraser Functionality**  
   - When eraser mode is activated, the system removes unwanted lines.  

**Add a Wiper Function**  
   - Move the pen closer to the camera or press ‘C’ to clear the screen.  

## **Functionalities**  

**Finding the Target Pen’s Color Range**  
- Converts **RGB images to HSV** for accurate color detection.  
- Uses adjustable HSV sliders to refine the tracking range.  

**Tracking & Writing with the Pen**  
- **Contour detection** ensures the marker is tracked accurately.  
- The x,y position is updated frame-by-frame for seamless drawing.  

**Eraser Functionality**  
- **Gesture-based switching** between pen and eraser.  
- Moving the marker to a specific screen area toggles eraser mode.  

**Automated Wiping System**  
- Moving the pen close to the camera **clears the entire screen**.  
- **Contour-based detection** ensures smooth transitions.  
- Alerts users before wiping, allowing time to save their work.  

## **Benefits**  
**Touch-Free Interaction** – No physical contact needed.  
**Real-Time Drawing** – Immediate visualization of gestures.  
**User-Friendly** – Simple, intuitive, and accessible for all users.  
**Boosts Creativity & Productivity** – Ideal for artists, educators, and professionals.  
**Low-Cost Implementation** – Works with a standard camera and marker.  

This **Virtual Pen System** revolutionizes digital interaction, making drawing and writing as natural as using a real pen—without touching a screen! 🚀  

![image](https://github.com/user-attachments/assets/85678784-a586-4240-bb33-2036078e4a82)
