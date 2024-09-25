# virtual-keyboard

This project is a hand gesture-based virtual keyboard that allows users to input text using hand movements captured through a webcam. Utilizing OpenCV for image processing and a hand tracking module, the system detects the position of the user's hand and displays a virtual keyboard on the screen. The keyboard is designed with specific keys such as letters, "Space," and "Delete," represented as buttons that can be visually interacted with. When the user hovers their hand over a key and performs a clicking gesture (by pinching their fingers), the corresponding action is executed: letters are added to the text, spaces are created, or characters are deleted. The program also integrates the `pynput` library to simulate actual keyboard input, enhancing the user experience by enabling real-time text entry through intuitive gestures.

# You need to install the following libraries:
```
pip install opencv-python
```
```
pip install cvzone
```
```
pip install numpy
```
```
pip install pynput
```
After installing these libraries, you should be able to run the code without any issues. Make sure your Python environment is set up correctly and that you are using a compatible version of Python (usually Python 3.x).

and ya thats it 👍
