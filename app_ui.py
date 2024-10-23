import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Import from Pillow for image handling
import os
from watering_schedule import generate_watering_schedule, plants

# Tkinter UI Setup
root = tk.Tk()
root.title("Plant Watering Schedule")
root.geometry("600x500")

# Load the background image
background_image = Image.open("C:/Users/hanad/OneDrive/Documents/plant_watering_schedule/4057631.jpg")  # Replace with your image file
background_photo = ImageTk.PhotoImage(background_image)

# Create a label to display the background image
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Make it fill the window

# Set custom window icon (ensure favicon.ico is in the same folder as app_ui.py)
root.iconbitmap(r"C:/Users/hanad/OneDrive/Documents/plant_watering_schedule/favicon.ico")

# Function to animate text popping up
def animate_text(text, label, index=0):
    if index < len(text):
        label.config(text=text[:index + 1])  # Show text incrementally
        root.after(100, animate_text, text, label, index + 1)  # Delay for the next character

# Create the label for the title but leave it empty initially
label = tk.Label(root, text="", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333")
label.pack(pady=20)

# Start the animation for the title text
animate_text("Welcome to the Plant Watering Schedule App", label)

# Add a title for the schedule box
schedule_title = tk.Label(root, text="Watering Schedule", font=("Arial", 14, "bold"), bg="#f0f0f0", fg="#333")
schedule_title.pack(pady=10)

# Function to handle button click and generate the schedule
def generate_schedule():
    schedule = generate_watering_schedule(plants)
    text_box.config(state="normal")
    text_box.delete(1.0, tk.END)

    for date, plants_for_date in schedule.items():
        # Insert the date and apply the 'date_highlight' tag
        text_box.insert(tk.END, f"{date}:\n", "date_highlight")
        
        for plant in plants_for_date:
            text_box.insert(tk.END, f"    {plant}\n", "plant_name")
        
        text_box.insert(tk.END, "\n" + "-" * 50 + "\n\n")

    text_box.config(state="disabled")

# Clear schedule function
def clear_schedule():
    text_box.config(state="normal")  # Enable text box to clear content
    text_box.delete(1.0, tk.END)  # Clear all content
    text_box.config(state="disabled")  # Lock the text box again to make it read-only

# Save schedule to file function (with popup)
def save_to_file():
    text_box.config(state="normal")  # Temporarily enable text box to read the content
    schedule = text_box.get(1.0, tk.END)  # Get all text from the text box
    text_box.config(state="disabled")  # Set back to read-only

    file_path = "watering_schedule.txt"
    # Save the content to a file
    with open(file_path, "w") as f:
        f.write(schedule)

    # Show popup asking if the user wants to open the file
    response = messagebox.askyesno("File Saved", "The schedule has been saved. Do you want to open the file?")
    
    if response:  # If the user clicks "Yes", open the file
        os.startfile(file_path)

# Create a frame to hold the scrollable text box
schedule_frame = tk.Frame(root, bg="#f0f0f0", padx=10, pady=10, bd=2, relief="sunken")
schedule_frame.pack(pady=20)

# Add a scrollable text widget
scrollbar = tk.Scrollbar(schedule_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text_box = tk.Text(schedule_frame, height=15, width=50, font=("Helvetica", 12), yscrollcommand=scrollbar.set, bg="#e8f5e9", fg="#000", wrap="word", padx=10, pady=10, bd=0, state="disabled")
text_box.pack(side=tk.LEFT)

# Add custom tags for coloring plant names and dates
text_box.tag_configure("plant_name", foreground="blue", font=("Arial", 12, "bold"))
text_box.tag_configure("date_highlight", background="#D3D3D3", foreground="green", font=("Arial", 12, "bold"))

scrollbar.config(command=text_box.yview)

# Add buttons
button = tk.Button(root, text="Generate Watering Schedule", command=generate_schedule, bg="#4CAF50", fg="white", font=("Arial", 12), width=25)
button.pack(pady=10)

clear_button = tk.Button(root, text="Clear Schedule", command=clear_schedule, bg="#FF6F61", fg="white", font=("Arial", 12), width=20)
clear_button.pack(pady=5)

save_button = tk.Button(root, text="Save to File", command=save_to_file, bg="#2196F3", fg="white", font=("Arial", 12), width=20)
save_button.pack(pady=5)

# Add a footer for credits
footer_label = tk.Label(root, text="Developed by Hanad", font=("Arial", 10, "italic"), bg="#f0f0f0", fg="#888")
footer_label.pack(side=tk.BOTTOM, pady=10)

# Run the application
root.mainloop()
