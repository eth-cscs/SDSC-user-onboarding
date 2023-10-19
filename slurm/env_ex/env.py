import os
import socket
import json

hostname = socket.gethostname()
print(f"Hello from {hostname}")


print(f"The SLURM environment is")

slurm_env = {k: v for k, v in os.environ.items() if k.startswith('SLURM_')}
print(json.dumps(slurm_env, indent=4))