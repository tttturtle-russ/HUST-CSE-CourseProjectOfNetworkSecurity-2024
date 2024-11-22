from rule import Rule
from tkinter import ttk

class RuleTable:
    def __init__(self, master) -> None:
        self.table = ttk.Treeview(master,  
                                  columns=(
                                    'name',
                                    'src_addr',
                                    'src_mask',
                                    'src_port_range',
                                    'dst_addr',
                                    'dst_mask',
                                    'dst_port_range',
                                    'action',
                                    'protocol'
                                    ),
                                    show='headings',
                                    displaycolumns='#all')
        self.table.heading('name', text='Name',anchor='w')
        self.table.heading('src_addr', text='Source Addr', anchor='w')
        self.table.heading('src_mask', text='Source Mask', anchor='w')
        self.table.heading('src_port_range', text='Source Port Range', anchor='w')
        self.table.heading('dst_addr', text='Destination Addr', anchor='w')
        self.table.heading('dst_mask', text='Destination Mask', anchor='w')
        self.table.heading('dst_port_range', text='Destination Port Range', anchor='w')
        self.table.heading('action', text='Action', anchor='w')
        self.table.heading('protocol', text='Protocol', anchor='w')

    def insert(self, rule):
        self.table.insert('', 'end', values=(
            rule.name,
            rule.src_addr,
            rule.src_mask,
            f'{rule.src_port_min}-{rule.src_port_max}',
            rule.dst_addr,
            rule.dst_mask,
            f'{rule.dst_port_min}-{rule.dst_port_max}',
            rule.action,
            rule.protocol
        ))

    def update(self, rules):
        self.table.delete(*self.table.get_children())
        for rule in rules:
            self.insert(rule)

    def grid(self, **kwargs):
        self.table.grid(**kwargs)

    def selection(self):
        return self.table.selection()
    
    def delete(self, item):
        self.table.delete(item)