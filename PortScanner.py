from tkinter import *
import socket

# Button Logic =======================================================================================================
def button_pressed():
    target_ip = target_text_input.get("1.0", "end-1c").strip()
    start_port = int(port_start_input.get("1.0", "end-1c").strip())
    end_port = int(port_end_input.get("1.0", "end-1c").strip())

    output_scan_results.delete("1.0", "end")

    output_scan_results.insert("end", f"Target IP: {target_ip}\n")
    output_scan_results.insert("end", f"Start Port: {start_port}\n")
    output_scan_results.insert("end", f"End Port: {end_port}\n")
    output_scan_results.insert("end", "Starting Scan...\n")
    output_scan_results.insert("end", "=================================================================\n")
    
    for port in range(start_port, end_port + 1):
        if pscan(target_ip, port):
            output_scan_results.insert("end", f"Port {port} is open\n")
        else:
            output_scan_results.insert("end", f"Port {port} is closed\n")

# ========================================================================================================================
# port scan logic ========================================================================================================
def pscan(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((ip, port))
        s.close()
        return True
    except:
        s.close()
        return False

# ==========================================================================================================================
root = Tk()
root.title("Port Scanner")
root.configure(background="black")

root.minsize(1150, 850)
root.maxsize(1150, 850)
root.geometry("300x300+50+50")
title = Label(root, fg = "green", bg = "black", padx = 25, pady = 10, text = "Port Scanner")
title.pack()
title.config(font = ('Helvetica bold', 20))

name = Label(root, fg = "green", bg = "black", text = "Milan Skoro")
name.pack()
name.place(x = 10, y = 10)

# Input for target IP --------------------------------------------------------
target_text_input = Text(root, height = 1, width = 30)
target_text_input.pack()
target_text_input.place(x = 100, y = 150)

target_input_title = Label(root, fg = "green", bg = "black", text = "Enter target IP")
target_input_title.pack()
target_input_title.place(x = 150, y = 110)
target_input_title.config(font = ('Helvetica bold', 15))

# Input for Ports -------------------------------------------------------------
# Starting port
port_start_input = Text(root, height = 1, width = 5)
port_start_input.pack()
port_start_input.place(x = 130, y = 400)

port_start_info = Label(root, fg = "green", bg = "black", text = "Start")
port_start_info.pack()
port_start_info.place(x = 135, y = 375)

# Ending port
port_end_input = Text(root, height = 1, width = 5)
port_end_input.pack()
port_end_input.place(x = 250, y = 400)

port_end_info = Label(root, fg = "green", bg = "black", text = "End")
port_end_info.pack()
port_end_info.place(x = 258, y = 375)

# General port info
port_title_text = Label(root, fg = "green", bg = "Black", text = "Enter Start and End port")
port_title_text.pack()
port_title_text.place(x = 100, y = 335)
port_title_text.config(font = ('Helvetica bold', 15))

# Button to run scan ----------------------------------------------------------
run_scan_button = Button(root, fg = "green", bg = "black", text = "Start Scan", command = button_pressed)
run_scan_button.pack()
run_scan_button.place(x = 135, y = 600)
run_scan_button.config(font = ('Helvetica Bold', 20))

# Print Area -------------------------------------------------------------------
output_scan_results = Text(root, height = 35, width = 65)
output_scan_results.pack()
output_scan_results.place(x = 550, y = 110)

# Warning ----------------------------------------------------------------------
warning_label = Label(root, fg = "red", bg = "black", text = "WARNING: the larger the port range, \n the longer the wait!")
warning_label.pack()
warning_label.config(font = ('Helvetica Bold', 15))
warning_label.place(x = 50, y = 700)

root.mainloop()