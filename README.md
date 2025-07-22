# QR Code Generator

This Python project allows you to generate QR codes in both SVG and PNG formats from a custom string or URL. It uses the `pyqrcode` and `pypng` libraries to create high-quality QR codes suitable for websites, apps, or printed materials.

## Features

- Input validation for empty strings
- Generates both `.svg` and `.png` versions of the QR code
- Easy to use and extend
- Unit tested using Python's `unittest` framework

## File Structure

- `qr_code_generator.py`: Main script for QR code generation. Contains a single function `generate_qr_code(data, svg_filename, png_filename)` that creates the QR files.
- `test_qr_code_generator.py`: Contains test cases for both expected and edge-case scenarios using the `unittest` framework.
- `.gitignore`: Prevents tracking of temporary, system, and generated files.
- `README.md`: Documentation file (this one).
- `LICENSE`: MIT License file for open-source distribution.

## Requirements

- Python 3.x
- `pyqrcode`
- `pypng`

## Installation

```bash```
pip install pyqrcode pypng

## Usage
from qr_code_generator import generate_qr_code
generate_qr_code("https://example.com")

## Testing
python test_qr_code_generator.py