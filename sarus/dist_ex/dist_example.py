import os
import time
import torch
import torch.distributed as dist

print(f"Setting up process group with master at {os.environ['MASTER_ADDR']}:{os.environ['MASTER_PORT']}")

dist.init_process_group(backend='nccl', init_method='env://')

local_rank = int(os.environ["LOCAL_RANK"])
device_id = local_rank
world_rank = dist.get_rank()
world_size = dist.get_world_size()

# Generate initial value on each rank
if world_rank == 0:
    initial_value = torch.tensor([3.0]).cuda(device_id)
    print(f"Generated initial value: {initial_value.item()}")
else:
    initial_value = torch.tensor([0.0]).cuda(device_id)

# Share the initial value on all nodes
dist.broadcast(initial_value, src=0)
print(f"Working with initial value: {initial_value.item()}")


result = initial_value

for i in range(3):
    time.sleep(3)

    # Generate a random value locally
    random_value = torch.rand(1).cuda(device_id)
    print(f"Generated random value: {random_value.item()}")

    # Add all local random values and make them available on each rank
    dist.all_reduce(random_value, op=dist.ReduceOp.SUM)
    print(f"Mean of random values: {random_value.item()/world_size}")

    # Add the sum of random values to the initial value
    result = result + random_value/world_size
    print(f"Updated initial value: {result.item()}")

# Sync and output the result on master rank
dist.barrier()
if world_rank == 0:
    print(f"Final value is {result.item()}")

# Cleanup distributed environment
print(f"Finishing and exiting.")
dist.destroy_process_group()
