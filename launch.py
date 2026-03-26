#!/usr/bin/env python3
"""
Launcher script for Wheel of Bugs application
"""

import subprocess
import sys
from pathlib import Path

def main():
    """Launch the Wheel of Bugs application"""
    
    # Get the directory where this script is located
    script_dir = Path(__file__).parent
    app_file = script_dir / "wheel_of_bugs.py"
    
    if not app_file.exists():
        print(f"Error: {app_file} not found!")
        sys.exit(1)
    
    print("🐛 Starting Wheel of Bugs...")
    print(f"Application file: {app_file}")
    print("The application will open in your web browser.")
    print("Press Ctrl+C to stop the server.")
    print("-" * 50)
    
    try:
        # Launch streamlit
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", str(app_file)
        ], cwd=script_dir)
    except KeyboardInterrupt:
        print("\n🛑 Stopping Wheel of Bugs...")
    except FileNotFoundError:
        print("Error: Streamlit is not installed. Please run: pip install streamlit")
        sys.exit(1)

if __name__ == "__main__":
    main()