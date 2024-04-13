# Final Project
# Date: April 12, 2024
# Group 4:
#  - Cong Lanh Hoang
#  - Einer Cupino
#  - Jasper Jan Tan
#  - Kwok Yuk Chui
#  - Wing Chi Lam

import time
from tkinter import *
from threading import Thread
from group_4_publisher import Publisher

class Application(Tk):
  def __init__(self, title, geometry):
    Tk.__init__(self)
    self.background_color = "#90EE90"

    self.title(title)
    self.geometry(geometry)
    self.configure(bg=self.background_color)

    # Create a frame to hold the widgets
    container = Frame(self, bg=self.background_color)
    container.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)
    
    self.create_ui(container)
    self.publisher = None
  
  def create_ui(self, parent = None):
    if not parent: parent = self

    # Define grid layout
    parent.columnconfigure(list(range(9)), weight=1, uniform="a")
    parent.rowconfigure(list(range(5)), weight=1, uniform="a")

    # Create a label for the name of the data-entry form with bold & italic font
    heading_label = Label(parent, text="MQTT Publisher", font=("Calibri", 32, "bold", "italic"), bg=self.background_color)
    heading_label.grid(row=0, column=0, columnspan=9, sticky="new")

    # Create first column with the following labels
    broker_address_label = Label(parent, text="Broker Address:", font=("Calibri", 14, "bold"), bg=self.background_color)
    broker_address_label.grid(row=1, column=0, columnspan=2, sticky="nw")

    broker_port_label = Label(parent, text="Broker Port:", font=("Calibri", 14, "bold"), bg=self.background_color)
    broker_port_label.grid(row=2, column=0, columnspan=2, sticky="nw")

    topic_label = Label(parent, text="Topic:", font=("Calibri", 14, "bold"), bg=self.background_color)
    topic_label.grid(row=3, column=0, columnspan=2, sticky="nw")

    log_label = Label(parent, text="Log:", font=("Calibri", 14, "bold"), bg=self.background_color)
    log_label.grid(row=1, column=5, columnspan=4, sticky="nw")

    # Create a button to start publisher
    start_button = Button(parent, text="Start", font=("Calibri", 14, "bold"), highlightbackground=self.background_color, command=self.start)
    start_button.grid(row=4, column=0, sticky="new", padx=5, pady=5)

    # Create a button to stop publisher
    stop_button = Button(parent, text="Stop", font=("Calibri", 14, "bold"), highlightbackground=self.background_color, command=self.stop)
    stop_button.grid(row=4, column=1, sticky="new", padx=5, pady=5)

    # Create a button to exit
    exit_button = Button(parent, text="Exit", font=("Calibri", 14, "bold"), highlightbackground=self.background_color, command=self.exit)
    exit_button.grid(row=4, column=2, sticky="new", padx=5, pady=5)

    # Create an entry that captures broker address
    self.broker_address = Entry(parent, font=("Calibri", 14), textvariable=StringVar(value="localhost"))
    self.broker_address.grid(row=1, column=2, columnspan=2, sticky="nw")

    # Create an entry that captures broker port
    self.broker_port = Entry(parent, font=("Calibri", 14), textvariable=StringVar(value="1883"))
    self.broker_port.grid(row=2, column=2, columnspan=2, sticky="nw")

    # Create an entry that captures topic
    self.topic = Entry(parent, font=("Calibri", 14), textvariable=StringVar(value="room_temperature"))
    self.topic.grid(row=3, column=2, columnspan=2, sticky="nw")

    # Create a text area to display log
    self.log = Text(parent, font=("Calibri", 14), height=20, width=60)
    self.log.grid(row=2, column=5, columnspan=4, rowspan=3, sticky="nw")

  def start(self):
    broker_address = self.broker_address.get()
    broker_port = int(self.broker_port.get())
    topic = self.topic.get()

    # Initialize publisher
    self.publisher = Publisher(broker_address, broker_port, topic)
    # Start publisher in a separate thread
    self.publisher_thread = Thread(target=self.publisher.start)
    self.publisher_thread.daemon = True
    self.publisher_thread.start()

    # Start a thread to continuously update the log
    self.update_log_thread = Thread(target=self.update_log)
    self.update_log_thread.daemon = True
    self.update_log_thread.start()

    # Update log with message
    self.log.insert(END, "Publisher started\n")
  
  def stop(self):
    self.stop_thread = Thread(target=self.stop_publisher)
    self.stop_thread.daemon = True
    self.stop_thread.start()

  def exit(self):
    self.destroy()
  
  def update_log(self):
    while True:
      if self.publisher:
        log_content = self.publisher.log
        if log_content:
          self.log.delete("1.0", END)  # Clear previous content
          self.log.insert(END, log_content)
      time.sleep(1)
  
  def stop_publisher(self):
    self.publisher.stop()
    self.publisher = None
    self.log.delete("1.0", END)
    self.log.insert(END, "Publisher stopped\n")

if __name__ == "__main__":
  title = "MQTT Publisher"
  geometry = "1280x600"
  app = Application(title, geometry)
  app.mainloop()