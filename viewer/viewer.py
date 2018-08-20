import tkinter as tk
from tkinter import ttk
import controller


class Viewer:
    def __init__(self):
        self.window = tk.Tk()
        self.set_window()
        self.set_labels()
        self.bt_choose_genome = tk.Button(self.window, text='Select input genome',
                                          width=20, height=2)
        self.bt_choose_seed = tk.Button(self.window, text='Select input seeds',
                                        width=20, height=2)
        self.bt_choose_down = tk.Button(self.window, text='Select download list',
                                        width=20, height=2)
        self.bt_show_genome = tk.Button(self.window, text='Show genome',
                                        width=15, height=2)
        self.bt_show_seed = tk.Button(self.window, text='Show seeds',
                                      width=15, height=2)
        self.bt_download = tk.Button(self.window, text='Download genomes',
                                     width=15, height=2)
        self.bt_compute = tk.Button(self.window, text='Compute',
                                    width=15, height=2)
        self.bt_show_res = tk.Button(self.window, text='Show result',
                                     width=15, height=2)
        self.bt_save = tk.Button(self.window, text='Save result',
                                 width=15, height=2)
        self.bt_blast = tk.Button(self.window, text='Select BLAST path',
                                  width=20, height=2)
        self.put_buttons()
        self.text = tk.Text(self.window, width=70, height=20)
        self.ini_text()

    def set_window(self):
        # Set window
        self.window.columnconfigure(0, weight=1)
        self.window.geometry()
        self.window.title("MLST")

    def ini_text(self):
        self.text.grid(row=4, column=0, padx=5, pady=10, columnspan=2,
                       sticky='ws')

    def set_text(self, in_text):
        self.text.insert('end', in_text)

    def set_labels(self):
        # Set labels
        # Input label
        lb_input = tk.Label(self.window, text='Select input files',
                            font=('Arial', 12), width=30, height=2)
        lb_input.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        # Output label
        # lb_output = tk.Label(self.window, text='Output',
        # font=('Arial', 12), width=30, height=2 )
        # lb_output.grid(row=3, column=0, padx=10, pady=10, sticky='w')

    def put_buttons(self):
        # set buttons
        self.bt_choose_genome.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.bt_blast.grid(row=1, column=1, padx=10, pady=10, sticky='w')
        self.bt_choose_seed.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.bt_choose_down.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        self.bt_show_genome.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        self.bt_show_seed.grid(row=5, column=1, padx=10, pady=10, sticky='w')
        self.bt_download.grid(row=1, column=2, padx=10, pady=10, sticky='en')
        self.bt_compute.grid(row=2, column=2, padx=10, pady=10, sticky='e')
        self.bt_show_res.grid(row=3, column=2, padx=10, pady=10, sticky='e')
        self.bt_save.grid(row=4, column=2, padx=10, pady=10, sticky='se')
