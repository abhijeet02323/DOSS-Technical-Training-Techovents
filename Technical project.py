#submitted code in technica

import tkinter as tk
from tkinter import ttk
import boto3
import numpy as np
import cv2
from PIL import Image, ImageTk
import geocoder
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from tkinter import messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import filedialog
import mediapipe as mp
import tkinter as tk
from tkinter import scrolledtext
import cohere

import cv2
import mediapipe as mp

    def run_hand_detection_app():
        class HandFingerDetector:
            def __init__(self):
                self.mp_hands = mp.solutions.hands
                self.hands = self.mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
                self.mp_drawing = mp.solutions.drawing_utils
                self.finger_names = ['Thumb', 'Index Finger', 'Middle Finger', 'Ring Finger', 'Pinky']
                self.fingertip_indices = [4, 8, 12, 16, 20]
                self.cap = cv2.VideoCapture(0)
        
            def detect_hands_and_fingers(self):
                while self.cap.isOpened():
                    success, image = self.cap.read()
                    if not success:
                        break
        
                    image = self._process_image(image)
                    results = self.hands.process(image)
                    image = self._draw_landmarks(image, results)
                    cv2.imshow('Hand and Finger Detection', image)
        
                    if cv2.waitKey(5) & 0xFF == ord('q'):
                        break
        
                self.cap.release()
                cv2.destroyAllWindows()
        
            def _process_image(self, image):
                image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
                image.flags.writeable = False
                return image
        
            def _draw_landmarks(self, image, results):
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        self.mp_drawing.draw_landmarks(image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
                        self._label_fingers(image, hand_landmarks)
        
                return image
        
            def _label_fingers(self, image, hand_landmarks):
                for idx, landmark in enumerate(hand_landmarks.landmark):
                    if idx in self.fingertip_indices:
                        finger_name = self.finger_names[self.fingertip_indices.index(idx)]
                        h, w, c = image.shape
                        cx, cy = int(landmark.x * w), int(landmark.y * h)
                        cv2.putText(image, finger_name, (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2, cv2.LINE_AA)
        
        if __name__ == "__main__":
            detector = HandFingerDetector()
            detector.detect_hands_and_fingers()
            

    # Function to run instance controller
    def run_instance_controller():
        
        # Your existing code for EC2 instance controller
        class EC2InstanceController:
            def __init__(self, master):
                self.master = master
                self.master.title("EC2 Instance Controller")
                self.master.attributes('-fullscreen', True)  # Set to full screen

                # Style
                self.style = ttk.Style()
                self.style.theme_use("clam")
                self.style.configure("TButton", padding=10, font=("Helvetica", 14))
                self.style.configure("TLabel", padding=10, font=("Helvetica", 16))

                # Frame
                self.main_frame = ttk.Frame(master)
                self.main_frame.pack(pady=20)

                self.instance_status_label = ttk.Label(self.main_frame, text="", foreground="blue")
                self.instance_status_label.grid(row=0, column=0, columnspan=2)

                self.start_button = ttk.Button(self.main_frame, text="Start Instance", command=self.start_instance)
                self.start_button.grid(row=1, column=0, padx=10, pady=10)

                self.stop_button = ttk.Button(self.main_frame, text="Stop Instance", command=self.stop_instance)
                self.stop_button.grid(row=1, column=1, padx=10, pady=10)

                self.close_button = ttk.Button(master, text="Close", command=self.close_window)
                self.close_button.pack(side=tk.BOTTOM, pady=20)

                # Initial GUI update
                self.update_gui()

            def get_instance_state(self):
                response = self.ec2.describe_instances(InstanceIds=[self.INSTANCE_ID])
                state = response['Reservations'][0]['Instances'][0]['State']['Name']
                return state

            def start_instance(self):
                self.ec2.start_instances(InstanceIds=[self.INSTANCE_ID])
                self.update_gui()

            def stop_instance(self):
                self.ec2.stop_instances(InstanceIds=[self.INSTANCE_ID])
                self.update_gui()

            def update_gui(self):
                state = self.get_instance_state()
                if state == 'running':
                    self.instance_status_label.config(text="Instance Status: Running", foreground="green")
                elif state == 'stopped':
                    self.instance_status_label.config(text="Instance Status: Stopped", foreground="red")

            def close_window(self):
                self.master.destroy()

        def main():
            root = tk.Tk()
            app = EC2InstanceController(root)
            root.mainloop()

        if __name__ == "__main__":
            main()

        pass
    
    # Function to run location app
    def run_location():
        # Your existing code for location app
        class LocationApp:
            def __init__(self, master):
                self.master = master
                self.master.title("Location App")

                # Enhance button style and appearance
                style = ttk.Style()
                style.configure("TButton", padding=10, font=("Helvetica", 14))

                # Create a button to show coordinates
                self.button = ttk.Button(master, text="Show My Location", command=self.show_coordinates)
                self.button.pack(pady=20)

            def get_coordinates(self):
                return geocoder.ip('me').latlng

            def show_coordinates(self):
                coordinates = self.get_coordinates()
                lat, lon = coordinates
                location = geocoder.osm(coordinates, method='reverse')
                location_str = f"Latitude: {lat}\nLongitude: {lon}\nLocation: {location.address}"

                # Create a new window
                window = tk.Toplevel(self.master)
                window.title("Your Location")

                # Create a label to display coordinates and location
                label = tk.Label(window, text=location_str, padx=20, pady=20)
                label.pack()

        def main():
            root = tk.Tk()
            app = LocationApp(root)
            root.mainloop()

        if __name__ == "__main__":
            main()

        pass
    
    # Function to run Gmail sender
    def run_gmail():
        # Your existing code for Gmail sender
        class GmailSender:
            def __init__(self, root):
                self.root = root
                self.sender_email = "amitguptaie99@gmail.com"
                self.smtp_server = "smtp.gmail.com"
                self.port = 587  # For starttls
                self.email_password = "tngy dmma zjks qozp"  # Replace with your app password

                self.create_main_window()
                self.create_widgets()

            def send_email(self):
                receiver_email = self.receiver_entry.get()
                subject = self.subject_entry.get()
                message = self.message_entry.get("1.0", tk.END)

                if not receiver_email or not subject or not message:
                    messagebox.showerror("Error", "Please fill in all fields.")
                    return

                try:
                    # Establish a connection to the SMTP server
                    server = smtplib.SMTP(self.smtp_server, self.port)
                    server.starttls()
                    server.login(self.sender_email, self.email_password)

                    # Create the email message
                    msg = MIMEMultipart()
                    msg['From'] = self.sender_email
                    msg['To'] = receiver_email
                    msg['Subject'] = subject
                    msg.attach(MIMEText(message, 'plain'))

                    # Send the email
                    server.send_message(msg)
                    server.quit()
                    messagebox.showinfo("Success", "Email sent successfully.")
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred: {str(e)}")

            def draw_mail_logo(self, canvas):
                canvas.create_polygon(50, 50, 50, 100, 200, 100, 200, 50, fill="white", outline="black", width=2)
                canvas.create_arc(50, 50, 200, 100, start=0, extent=180, fill="white", outline="black", width=2)
                canvas.create_line(50, 75, 200, 75, fill="black", width=2)
                canvas.create_line(50, 75, 125, 125, fill="black", width=2)
                canvas.create_line(200, 75, 125, 125, fill="black", width=2)

            def create_main_window(self):
                self.root.title("Gmail Sender")
                self.root.geometry("400x400")
                self.root.configure(padx=10, pady=10)

            def create_widgets(self):
                canvas = tk.Canvas(self.root, width=250, height=150)
                canvas.pack()
                self.draw_mail_logo(canvas)

                receiver_label = tk.Label(self.root, text="Receiver Email:", font=("Helvetica", 12))
                receiver_label.pack()

                self.receiver_entry = tk.Entry(self.root, font=("Helvetica", 12))
                self.receiver_entry.pack(fill=tk.X)

                subject_label = tk.Label(self.root, text="Subject:", font=("Helvetica", 12))
                subject_label.pack()

                self.subject_entry = tk.Entry(self.root, font=("Helvetica", 12))
                self.subject_entry.pack(fill=tk.X)

                message_label = tk.Label(self.root, text="Message:", font=("Helvetica", 12))
                message_label.pack()

                self.message_entry = tk.Text(self.root, height=10, font=("Helvetica", 12))
                self.message_entry.pack(fill=tk.BOTH, expand=True)

                send_button = tk.Button(self.root, text="Send Email", command=self.send_email, font=("Helvetica", 12))
                send_button.pack()

        def main():
            root = tk.Tk()
            gmail_sender = GmailSender(root)
            root.mainloop()

        if __name__ == "__main__":
            main()

        pass
    
    # Function to run EC2 manager
    def run_EC2_manager():
        # Your existing code for EC2 manager
        class EC2Manager:
            def __init__(self, root):
                self.root = root
                self.aws_access_key_id = 'AKIA47CRUHKF5GPTTJK2'
                self.aws_secret_access_key = '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'
                self.region_name = 'ap-south-1'
                self.ec2 = boto3.resource('ec2', aws_access_key_id=self.aws_access_key_id, aws_secret_access_key=self.aws_secret_access_key, region_name=self.region_name)
                self.key_pair_name = 'nikhil'

                self.create_main_window()
                self.create_widgets()

            def launch_instance(self):
                instance = self.ec2.create_instances(
                    ImageId='ami-0e670eb768a5fc3d4',
                    MinCount=1,
                    MaxCount=1,
                    InstanceType='t2.micro',
                    KeyName=self.key_pair_name
                )
                self.output_text.insert(tk.END, "Instance launched: {}\n".format(instance[0].id))

            def stop_instance(self):
                instance_id = self.instance_entry.get()
                instance = self.ec2.Instance(instance_id)
                instance.stop()
                self.output_text.insert(tk.END, "Instance stopped: {}\n".format(instance_id))

            def terminate_instance(self):
                instance_id = self.instance_entry.get()
                instance = self.ec2.Instance(instance_id)
                instance.terminate()
                self.output_text.insert(tk.END, "Instance terminated: {}\n".format(instance_id))

            def list_running_instances(self):
                self.output_text.delete('1.0', tk.END)
                running_instances = self.ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
                self.output_text.insert(tk.END, "Running instances:\n")
                for instance in running_instances:
                    self.output_text.insert(tk.END, "Instance ID: {}\n".format(instance.id))

            def list_all_except_terminated(self):
                self.output_text.delete('1.0', tk.END)
                all_instances = self.ec2.instances.all()
                self.output_text.insert(tk.END, "All instances except terminated:\n")
                for instance in all_instances:
                    if instance.state['Name'] != 'terminated':
                        self.output_text.insert(tk.END, "Instance ID: {}\n".format(instance.id))

            def create_main_window(self):
                self.root.title("EC2 Manager")
                self.root.geometry("400x400")
                self.root.configure(padx=10, pady=10)

            def create_widgets(self):
                self.output_text = tk.Text(self.root, height=10, width=40, font=("Helvetica", 12))
                self.instance_entry = tk.Entry(self.root, font=("Helvetica", 12))
                self.launch_button = tk.Button(self.root, text="Launch Instance", command=self.launch_instance, font=("Helvetica", 12))
                self.stop_button = tk.Button(self.root, text="Stop Instance", command=self.stop_instance, font=("Helvetica", 12))
                self.terminate_button = tk.Button(self.root, text="Terminate Instance", command=self.terminate_instance, font=("Helvetica", 12))
                self.list_running_button = tk.Button(self.root, text="List Running Instances", command=self.list_running_instances, font=("Helvetica", 12))
                self.list_except_terminated_button = tk.Button(self.root, text="List All Except Terminated", command=self.list_all_except_terminated, font=("Helvetica", 12))
                self.quit_button = tk.Button(self.root, text="Quit", command=self.root.quit, font=("Helvetica", 12))

                self.output_text.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
                self.instance_entry.grid(row=1, column=0, padx=10, pady=5)
                self.launch_button.grid(row=1, column=1, padx=10, pady=5)
                self.stop_button.grid(row=2, column=0, padx=10, pady=5)
                self.terminate_button.grid(row=2, column=1, padx=10, pady=5)
                self.list_running_button.grid(row=3, column=0, padx=10, pady=5)
                self.list_except_terminated_button.grid(row=3, column=1, padx=10, pady=5)
                self.quit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        def main():
            root = tk.Tk()
            ec2_manager = EC2Manager(root)
            root.mainloop()

        if __name__ == "__main__":
            main()

        pass
    
    # Function to run S3 file manager
    def run_S3filemanager():
        # Your existing code for S3 file manager
        class S3FileManager:
            def __init__(self, aws_access_key_id, aws_secret_access_key, bucket_name):
                self.aws_access_key_id = aws_access_key_id
                self.aws_secret_access_key = aws_secret_access_key
                self.bucket_name = bucket_name
                self.s3_client = boto3.client('s3', aws_access_key_id=self.aws_access_key_id, aws_secret_access_key=self.aws_secret_access_key)

                self.root = tk.Tk()
                self.root.title("S3 File Manager")

                screen_width = self.root.winfo_screenwidth()
                screen_height = self.root.winfo_screenheight()
                self.root.geometry(f"{screen_width-100}x{screen_height-100}+50+50")

                self.upload_button = tk.Button(self.root, text="Upload File", command=self.upload_file)
                self.upload_button.pack(pady=10)

                self.list_button = tk.Button(self.root, text="List Files", command=self.list_files)
                self.list_button.pack(pady=10)

                self.delete_button = tk.Button(self.root, text="Delete File", command=self.delete_file)
                self.delete_button.pack(pady=10)

                self.file_list = tk.Listbox(self.root)
                self.file_list.pack(fill=tk.BOTH, expand=True, pady=10)

                self.message_label = tk.Label(self.root, text="")
                self.message_label.pack(pady=10)

                self.control_frame = tk.Frame(self.root)
                self.control_frame.pack(side=tk.TOP, anchor=tk.NE, padx=10, pady=10)

                self.maximize_button = tk.Button(self.control_frame, text="Maximize", command=self.maximize_window)
                self.maximize_button.pack(side=tk.LEFT)

                self.minimize_button = tk.Button(self.control_frame, text="Minimize", command=self.minimize_window)
                self.minimize_button.pack(side=tk.LEFT)

                self.close_button = tk.Button(self.control_frame, text="Close", command=self.close_window)
                self.close_button.pack(side=tk.LEFT)

                self.root.mainloop()

            def upload_file(self):
                filename = filedialog.askopenfilename()
                if filename:
                    object_name = filename.split('/')[-1]
                    try:
                        self.s3_client.upload_file(filename, self.bucket_name, object_name)
                        print(f'{filename} uploaded successfully to {self.bucket_name}/{object_name}')
                    except Exception as e:
                        print(f'Error uploading {filename} to {self.bucket_name}/{object_name}: {e}')

            def list_files(self):
                try:
                    response = self.s3_client.list_objects_v2(Bucket=self.bucket_name)
                    if 'Contents' in response:
                        files = [obj['Key'] for obj in response['Contents']]
                        self.file_list.delete(0, tk.END)
                        for file in files:
                            self.file_list.insert(tk.END, file)
                        print(f'Files in {self.bucket_name}: {files}')
                    else:
                        print(f'No files found in {self.bucket_name}')
                except Exception as e:
                    print(f'Error listing files in {self.bucket_name}: {e}')

            def delete_file(self):
                selected_item = self.file_list.curselection()
                if selected_item:
                    filename = self.file_list.get(selected_item)
                    try:
                        self.s3_client.delete_object(Bucket=self.bucket_name, Key=filename)
                        print(f'{filename} deleted successfully from {self.bucket_name}')
                        self.message_label.config(text=f'{filename} deleted successfully from {self.bucket_name}')
                    except Exception as e:
                        print(f'Error deleting {filename} from {self.bucket_name}: {e}')
                        self.message_label.config(text=f'Error deleting {filename} from {self.bucket_name}: {e}')

            def maximize_window(self):
                self.root.state('zoomed')

            def minimize_window(self):
                self.root.state('iconic')

            def close_window(self):
                self.root.destroy()

        if __name__ == "__main__":

        pass
    
    def run_gen_AI():
        class CohereChatApp:
            def __init__(self, api_key):
                # Initialize the Cohere client
                self.co = cohere.Client(api_key)
                
                # Create the main window
                self.window = tk.Tk()
                self.window.title("Cohere AI Chat")
                
                # Create a scrolled text widget for the conversation
                self.conversation = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, state='normal', width=50, height=20)
                self.conversation.pack(padx=10, pady=10)
                
                # Create a text widget for user input
                self.user_input = tk.Text(self.window, height=3, width=50)
                self.user_input.pack(padx=10, pady=(0, 10))
                
                # Create a button to send the message
                self.send_button = tk.Button(self.window, text="Send", command=self.send_message)
                self.send_button.pack(pady=(0, 10))
                
                # Start the Tkinter event loop
                self.window.mainloop()
            
            def send_message(self):
                user_message = self.user_input.get("1.0", tk.END).strip()
                if user_message:
                    self.conversation.insert(tk.END, f"You: {user_message}\n")
                    self.user_input.delete("1.0", tk.END)
                    
                    try:
                        # Get response from Cohere
                        response = self.co.generate(
                            model='command-xlarge-nightly',
                            prompt=user_message,
                            max_tokens=50
                        )
                        ai_message = response.generations[0].text.strip()
                        self.conversation.insert(tk.END, f"AI: {ai_message}\n")
                    except Exception as e:
                        self.conversation.insert(tk.END, f"Error: {e}\n")
        
        # Replace 'use your own' with your actual API key
        api_key = 'use your own'
        app = CohereChatApp(api_key)

    
    
    # Create buttons for each application
    instance_controller_button = tk.Button(root, text="EC2 Instance Controller", command=run_instance_controller)
    instance_controller_button.pack(pady=10)
    
    location_button = tk.Button(root, text="Location App", command=run_location)
    location_button.pack(pady=10)
    
    gmail_button = tk.Button(root, text="Gmail Sender", command=run_gmail)
    gmail_button.pack(pady=10)
    
    EC2_manager_button = tk.Button(root, text="EC2 Manager", command=run_EC2_manager)
    EC2_manager_button.pack(pady=10)
    
    S3filemanager_button = tk.Button(root, text="S3 File Manager", command=run_S3filemanager)
    S3filemanager_button.pack(pady=10)
    
    hand_detection_button = tk.Button(root, text="Hand Detection App", command=run_hand_detection_app)
    hand_detection_button.pack(pady=10)

    gen_ai_button = tk.Button(root, text="Gen AI", command=run_gen_AI)
    gen_ai_button.pack(pady=10)                           
    
    root.mainloop()

if __name__ == "__main__":
    main_frame_window()
