import os
import subprocess

xwall_path = os.environ["XWALL_PATH"]

def add_rule(rule) -> str:
    r = subprocess.Popen(f'{xwall_path}/cli/xwall_app -addrule {rule.src_addr} {rule.dst_addr} {rule.src_mask} {rule.dst_mask} {rule.src_port_min} {rule.src_port_max} {rule.dst_port_min} {rule.dst_port_max} {rule.protocol} {rule.action} TRUE', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = r.stdout.read().decode('utf8').strip()
    err = r.stderr.read().decode('utf8').strip()
    if err == "":
        return out
    return err

def del_rule(idx):
