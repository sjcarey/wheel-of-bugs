"""
Wheel of Bugs - A fun web application for spinning the wheel of software bugs!

Author: Created with GitHub Copilot
"""

import streamlit as st
import json
import matplotlib.pyplot as plt
import numpy as np
import time
import random
import os
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Wheel of Bugs",
    page_icon="🐛",
    layout="centered",
    initial_sidebar_state="collapsed"
)

class WheelOfBugs:
    def __init__(self):
        self.config_file = Path(__file__).parent / "bugs_config.json"
        self.load_config()
        
    def load_config(self):
        """Load bugs and settings from configuration file"""
        try:
            with open(self.config_file, 'r') as f:
                config = json.load(f)
                self.bugs = config["bugs"]
                self.settings = config["settings"]
        except FileNotFoundError:
            st.error(f"Configuration file not found: {self.config_file}")
            st.stop()
        except json.JSONDecodeError:
            st.error("Invalid JSON in configuration file")
            st.stop()
    
    def save_config(self):
        """Save current bugs and settings to configuration file"""
        config = {
            "bugs": self.bugs,
            "settings": self.settings
        }
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=2)
    
    def create_wheel_figure(self, rotation_angle=0, highlight_segment=None):
        """Create the wheel visualization using matplotlib"""
        fig, ax = plt.subplots(figsize=(10, 10))
        
        # Calculate angles for each segment
        n_bugs = len(self.bugs)
        angles = [360/n_bugs] * n_bugs
        colors = self.settings["wheel_colors"]
        
        # Ensure we have enough colors
        while len(colors) < len(self.bugs):
            colors.extend(colors)
        colors = colors[:len(self.bugs)]
        
        # Highlight the selected segment if specified
        if highlight_segment is not None:
            edge_colors = ['red' if i == highlight_segment else 'white' for i in range(n_bugs)]
            linewidths = [4 if i == highlight_segment else 1 for i in range(n_bugs)]
        else:
            edge_colors = 'white'
            linewidths = 1
        
        # Create pie chart with rotation
        wedges, texts = ax.pie(
            angles, 
            labels=self.bugs,
            colors=colors,
            startangle=90 + rotation_angle,
            textprops={'fontsize': 10, 'weight': 'bold'},
            wedgeprops={'edgecolor': edge_colors, 'linewidth': linewidths}
        )
        
        # Add center circle for aesthetics
        centre_circle = plt.Circle((0,0), 0.3, fc='white', ec='black', linewidth=2)
        fig.gca().add_artist(centre_circle)
        
        # Add title in center
        ax.text(0, 0, "🐛\nWheel of\nBugs", ha='center', va='center', 
                fontsize=12, weight='bold')
        
        # Add pointer at top
        ax.annotate('', xy=(0, 1), xytext=(0, 1.1),
                   arrowprops=dict(arrowstyle='->', lw=3, color='red'))
        
        ax.set_xlim(-1.2, 1.2)
        ax.set_ylim(-1.2, 1.2)
        
        return fig
    
    def spin_wheel(self):
        """Animate the wheel spinning"""
        placeholder = st.empty()
        
        # Calculate total rotations (multiple full rotations plus final position)
        base_rotations = random.uniform(3, 6)  # 3-6 full rotations
        final_angle = random.uniform(0, 360)   # Final stopping position
        total_rotation = base_rotations * 360 + final_angle
        
        # Animation parameters
        duration = self.settings["spin_duration_seconds"]
        frames = 60
        dt = duration / frames
        
        # Spinning animation with deceleration
        for i in range(frames):
            progress = i / frames
            # Ease-out animation (deceleration)
            eased_progress = 1 - (1 - progress) ** 3
            current_angle = eased_progress * total_rotation
            
            with placeholder.container():
                fig = self.create_wheel_figure(current_angle)
                st.pyplot(fig, clear_figure=True)
                plt.close()
            
            time.sleep(dt)
        
        # Determine which segment the wheel stopped on
        # Normalize final angle and account for wheel orientation
        normalized_angle = (360 - (final_angle % 360)) % 360
        segment_size = 360 / len(self.bugs)
        winning_segment = int(normalized_angle / segment_size) % len(self.bugs)
        
        # Show final result with highlighted segment
        with placeholder.container():
            fig = self.create_wheel_figure(total_rotation, winning_segment)
            st.pyplot(fig, clear_figure=True)
            plt.close()
        
        return self.bugs[winning_segment]
    
    def edit_bugs_interface(self):
        """Interface for editing the bugs list"""
        st.subheader("🛠️ Edit Bugs")
        
        # Display current bugs with delete buttons
        bugs_to_remove = []
        for i, bug in enumerate(self.bugs):
            col1, col2 = st.columns([4, 1])
            with col1:
                st.text(f"{i+1}. {bug}")
            with col2:
                if st.button("❌", key=f"delete_{i}"):
                    bugs_to_remove.append(i)
        
        # Remove selected bugs
        for idx in reversed(bugs_to_remove):
            self.bugs.pop(idx)
            self.save_config()
            st.rerun()
        
        # Add new bug
        with st.form("add_bug_form"):
            new_bug = st.text_input("Add a new bug:")
            if st.form_submit_button("Add Bug"):
                if new_bug.strip():
                    self.bugs.append(new_bug.strip())
                    self.save_config()
                    st.success(f"Added: {new_bug}")
                    st.rerun()
    
    def settings_interface(self):
        """Interface for editing settings"""
        st.subheader("⚙️ Settings")
        
        new_duration = st.slider(
            "Spin Duration (seconds)",
            min_value=1.0,
            max_value=10.0,
            value=self.settings["spin_duration_seconds"],
            step=0.5
        )
        
        if new_duration != self.settings["spin_duration_seconds"]:
            self.settings["spin_duration_seconds"] = new_duration
            self.save_config()
            st.success("Settings saved!")

def main():
    """Main application function"""
    
    # Title and description
    st.title("🐛 Wheel of Bugs")
    st.markdown("*Spin the wheel to discover your next debugging adventure!*")
    
    # Initialize wheel
    wheel = WheelOfBugs()
    
    # Sidebar for configuration
    with st.sidebar:
        st.title("Configuration")
        
        tab1, tab2 = st.tabs(["Edit Bugs", "Settings"])
        
        with tab1:
            wheel.edit_bugs_interface()
        
        with tab2:
            wheel.settings_interface()
    
    # Main content
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Show the wheel (static initially)
        if 'wheel_result' not in st.session_state:
            fig = wheel.create_wheel_figure()
            st.pyplot(fig, clear_figure=True)
            plt.close()
        
        # Spin button
        if st.button("🎰 SPIN THE WHEEL!", type="primary", use_container_width=True):
            if len(wheel.bugs) == 0:
                st.error("Please add some bugs to the wheel first!")
            else:
                with st.spinner("Spinning the wheel..."):
                    result = wheel.spin_wheel()
                    st.session_state.wheel_result = result
        
        # Show result
        if 'wheel_result' in st.session_state:
            st.markdown("---")
            st.success(f"🎯 **You got:** {st.session_state.wheel_result}")
            
            # Reset button
            if st.button("Reset Wheel", type="secondary"):
                if 'wheel_result' in st.session_state:
                    del st.session_state.wheel_result
                st.rerun()
    
    # Instructions
    with st.expander("📖 How to use"):
        st.markdown("""
        1. **Spin the Wheel**: Click the big spin button to start the wheel spinning
        2. **Edit Bugs**: Use the sidebar to add or remove bugs from the wheel
        3. **Adjust Settings**: Change the spin duration in the settings tab
        4. **Configuration**: All changes are automatically saved to `bugs_config.json`
        
        **Note**: You can manually edit the `bugs_config.json` file to add more bugs or customize colors!
        """)

if __name__ == "__main__":
    main()