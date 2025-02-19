# Secure Data Hiding in Images using Steganography (PNG Only) with GUI

This project implements a steganography technique to securely hide data within PNG images. PNG format is chosen due to its lossless compression, ensuring that the hidden data remains intact. This version includes a Graphical User Interface (GUI) for ease of use.

**Important:** This implementation currently only supports PNG image files. Using other image formats (like JPEG,JPG) will result in data loss due to lossy compression.

## Project Structure

├── Main_Code_Commit/
│   ├── MainApp.py       # Main script for launching the App
│   ├── encryption.py    # Functionality for encrypting data before hiding
│   ├── decryption.py    # Functionality for decrypting data after extraction
│   ├── apple.png        # Example PNG image for testing
│   ├── requirements.txt    # Installing the necessary libraries using pip
│   ├── background_image.jpg # Background image for the GUI
|__ Presentation_Eshaan_Sandhu
└── README.md

**Note:** All files within the `Main_Code_Commit/` directory must reside in the same folder for the script to execute correctly.

## Prerequisites

* **Python 3.x:** Ensure you have Python 3 installed on your system.
* **Required Libraries:** Install the necessary libraries using pip:

    ```bash
    pip install -r Main_Code_Commit/requirements.txt
    ```

    The `requirements.txt` file should contain the following:

    ```
    opencv-python
    Pillow
    cryptography
    numpy
    shutnil
    ```

    **Note:** Tkinter and os are standard Python libraries and do not need to be installed via pip.

## Usage

1.  **Clone the repository:**

    ```bash
    git clone [repository URL]
    cd [repository directory]
    ```

2.  **Navigate to the `Main_Code_Commit` directory:**

    ```bash
    cd Main_Code_Commit/
    ```

3.  **Running the GUI:**

    ```bash
    python main.py
    ```

    This will launch the GUI application.

4.  **Using the GUI:**

    * The GUI provides user-friendly controls for:
        * Selecting the input PNG image.
        * Entering the message and password to hide.
        * Choosing the output file path.
        * Extracting message from an image by entering password.
        * Potentially, displaying extracted message.
    * Please refer to the GUI elements for specific usage instructions.

## Important Considerations

* **PNG Format:** This implementation relies on the lossless compression of PNG. Using other image formats will likely result in data corruption.
* **Data Size:** The amount of data you can hide depends on the size of the image. Larger images can hold more data.
* **Security:** While steganography provides a degree of security, it is not foolproof. Sophisticated analysis techniques can potentially detect hidden data.
* **GUI Library:** Tkinter is used for the GUI.
* **Error Handling:** The provided code includes error handling for file not found, etc., and these errors are clearly displayed in the GUI.

## Future Improvements

* Implement support for other lossless image formats (e.g., BMP).
* Add error handling and input validation.
* Add more advanced GUI features (e.g., progress bars).
* Add support for hiding files, not only strings.
* Improve error handling and user feedback.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to submit a pull request.
