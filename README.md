<<<<<<< HEAD
# 🐛 Wheel of Bugs

A fun and interactive web application that spins a wheel to randomly select software bugs! Perfect for developers who want to add some humor to their debugging sessions or use it as a teaching tool for common programming pitfalls.

## 🎯 Features

- **Interactive Wheel**: Beautifully animated spinning wheel with customizable segments
- **Configurable Bugs**: Easily add, remove, or edit bugs through the web interface
- **Customizable Settings**: Adjust spin duration and other parameters
- **Persistent Configuration**: All changes are automatically saved to a JSON configuration file
- **Responsive Design**: Works great on desktop and mobile devices
- **Easy Installation**: Simple pip install with all dependencies handled automatically

## 🎮 Demo

The wheel comes pre-loaded with common software bugs including:
- Segmentation fault
- Started at 1 instead of 0
- Wrong coordinate system
- Used left hand rule
- Off by cosine(dec)
- Didn't account for NaNs
- And more!

## 📦 Installation

### Option 1: Install from Source (Recommended)

1. **Clone or download this repository:**
   ```bash
   git clone https://github.com/yourusername/wheel_of_bugs.git
   cd wheel_of_bugs
   ```

2. **Install the package:**
   ```bash
   pip install -e .
   ```

3. **Run the application:**
   ```bash
   streamlit run wheel_of_bugs.py
   ```

### Option 2: Direct Installation

1. **Install dependencies:**
   ```bash
   pip install streamlit matplotlib numpy
   ```

2. **Download the files:**
   - `wheel_of_bugs.py` (main application)
   - `bugs_config.json` (configuration file)

3. **Run the application:**
   ```bash
   streamlit run wheel_of_bugs.py
   ```

### Option 3: Virtual Environment (Recommended for Development)

1. **Create and activate a virtual environment:**
   ```bash
   python -m venv wheel_env
   
   # On Windows:
   wheel_env\\Scripts\\activate
   
   # On macOS/Linux:
   source wheel_env/bin/activate
   ```

2. **Install the package:**
   ```bash
   cd wheel_of_bugs
   pip install -e .
   ```

3. **Run the application:**
   ```bash
   streamlit run wheel_of_bugs.py
   ```

## 🚀 Usage

### Running the Application

After installation, run the web application:

```bash
streamlit run wheel_of_bugs.py
```

The application will open in your default web browser, typically at `http://localhost:8501`.

### Using the Wheel

1. **Spin the Wheel**: Click the "🎰 SPIN THE WHEEL!" button to start the animation
2. **View Results**: After a few seconds, the wheel will stop and highlight the selected bug
3. **Reset**: Click "Reset Wheel" to clear the result and spin again

### Customizing Bugs

Use the **sidebar** to customize the wheel:

#### Add New Bugs:
1. Go to the "Edit Bugs" tab in the sidebar
2. Enter a new bug name in the text input
3. Click "Add Bug"

#### Remove Bugs:
1. Find the bug you want to remove in the list
2. Click the ❌ button next to it

#### Adjust Settings:
1. Go to the "Settings" tab in the sidebar  
2. Use the slider to adjust the spin duration (1-10 seconds)

### Manual Configuration

You can also manually edit the `bugs_config.json` file:

```json
{
  "bugs": [
    "Your custom bug 1",
    "Your custom bug 2",
    "Another debugging nightmare"
  ],
  "settings": {
    "spin_duration_seconds": 3.0,
    "wheel_colors": [
      "#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4",
      "#FFEAA7", "#DDA0DD", "#98D8C8", "#F7DC6F"
    ]
  }
}
```

## 🎨 Customization Options

### Bug Categories

Consider organizing bugs by category:
- **Logic Errors**: Off-by-one errors, wrong conditions
- **Memory Issues**: Null pointer exceptions, memory leaks
- **Data Issues**: Type mismatches, encoding problems  
- **Concurrency**: Race conditions, deadlocks
- **Integration**: API misuse, configuration errors

### Color Themes

Modify the `wheel_colors` array in `bugs_config.json` to customize the wheel appearance. Colors should be in hex format (e.g., `#FF6B6B`).

## 🔧 Technical Details

### Dependencies

- **Streamlit**: Web application framework
- **Matplotlib**: Wheel visualization and animation
- **NumPy**: Mathematical operations for animations

### File Structure

```
wheel_of_bugs/
├── wheel_of_bugs.py      # Main application file
├── bugs_config.json      # Configuration file (bugs & settings)
├── requirements.txt      # Python dependencies
├── setup.py             # Package installation script
└── README.md            # This documentation
```

### Configuration File Format

The `bugs_config.json` file contains:
- `bugs`: Array of bug names to display on the wheel
- `settings.spin_duration_seconds`: How long the wheel spins (float)
- `settings.wheel_colors`: Array of hex color codes for wheel segments

## 🐛 Troubleshooting

### Common Issues

**Application won't start:**
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check that you're in the correct directory
- Verify Python version compatibility (3.8+)

**Wheel appears blank:**
- Check that `bugs_config.json` exists and is valid JSON
- Ensure at least one bug is in the configuration file

**Configuration not saving:**
- Verify write permissions in the application directory
- Check that `bugs_config.json` is not read-only

### Getting Help

If you encounter issues:
1. Check that all files are in the same directory
2. Verify your Python version: `python --version` (needs 3.8+)
3. Try recreating the virtual environment
4. Check the Streamlit logs in the terminal for error messages

## 📝 License

This project is released under the MIT License. Feel free to modify, distribute, and use for any purpose!

## 🎉 Contributing

Contributions are welcome! Ideas for improvements:
- Sound effects for spinning
- Different wheel themes/styles  
- Bug categories with filtering
- Statistics tracking
- Export/import configuration files
- Multi-language support

## 🙏 Credits

This package was developed with the assistance of AI - specifically VSCode GitHub Copilot powered by Claude Sonnet 4. The AI helped design the architecture, implement the spinning wheel animation, create the user interface, and generate comprehensive documentation.

Perfect for developers who like to gamify their debugging process!

---

**Happy Bug Hunting!** 🐛🎯
=======
# wheel_of_bugs
Web application to determine which bug you are fixing by spinning the wheel
>>>>>>> bc4630ef76b1e573ebc58b1cbf7f861f3c3a18ec
