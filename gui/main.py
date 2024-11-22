import tkinter as tk
from tkinter import ttk
from log import LogText
from rule_btn import AddRuleButton, DeleteRuleButton, SaveRuleButton, ClearRuleButton
from rule_table import RuleTable

class MainApplication:
    def __init__(self, window_name) -> None:

        self.window = tk.Tk()
        self.window.title(window_name)
        self.window.focus_force()
        self.window.geometry('1920x1080')
        self.window.resizable(True, True)

        self.notebook = ttk.Notebook(self.window)
        self.main_frame = tk.Frame()
        self.log_frame = tk.Frame()

        self.rule_table = RuleTable(self.main_frame)
        self.rule_table.grid(row=1, column=0, columnspan=4)

        self.log_text = LogText(self.log_frame)
        self.log_text.grid(row=1, column=0, columnspan=4)

        self.add_rule_btn = AddRuleButton(self.main_frame,self.log_text,self.rule_table, text='Add Rule')
        self.add_rule_btn.grid(row=0, column=0)

        self.delete_rule_btn = DeleteRuleButton(self.main_frame,self.log_text,self.rule_table, text='Delete Rule')
        self.delete_rule_btn.grid(row=0, column=1)

        self.save_rule_btm = SaveRuleButton(self.main_frame,self.log_text,self.rule_table, text='Save Rule')
        self.save_rule_btm.grid(row=0, column=2)

        self.clear_rule_btn = ClearRuleButton(self.main_frame,self.log_text,self.rule_table, text='Clear Rule')
        self.clear_rule_btn.grid(row=0, column=3)

        self.notebook.add(self.main_frame, text='Main')
        self.notebook.add(self.log_frame, text='Log')

        self.notebook.pack()
        

    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    app = MainApplication('Fire Wall Console')
    app.run()

    