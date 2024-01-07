import subprocess

def get_pid(process_name):
    pids = subprocess.check_output(["pgrep", process_name]).decode().strip()
    pids_arr = pids.strip().split('\n')
    return pids_arr

pids = get_pid("process_name")

def read_maps_files(pids):
    maps_contents = {}
    for pid in pids:
        try:
            with open(f"/proc/{pid}/maps", "r") as file:
                maps_contents[pid] = file.readlines()
        except FileNotFoundError:
            print(f"Maps file for PID {pid} not found.")
        except Exception as e:
            print(f"Error reading maps file for PID {pid}: {e}")
    return maps_contents

maps_contents = read_maps_files(pids)

for pid, content in maps_contents.items():
    print(f"Contents of /proc/{pid}/maps:")
    print(''.join(content))