# Sierpinski-Triangle Plotter

This Python program generates a colorful plot by selecting random points within a triangle and assigning colors based on their proximity to the triangle's corners.

## Description

The program performs the following steps:
1. Opens a graphics window of user-defined width and height.
2. Defines three corners of a triangle at the top middle, lower left, and lower right of the window.
3. Randomly selects initial points and iteratively finds new points halfway towards a randomly chosen corner.
4. Colors each point based on its distance from the triangle's corners, creating a gradient effect.

## Requirements

- Python 3.x
- `graphics.py` module

## Usage

Run the program and input the desired width and height for the window when prompted. The program will then generate and display the plot. 

```python
python Sierpinski.py
