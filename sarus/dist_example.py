import os
import torch
import torch.distributed as dist

print(os.environ['MASTER_ADDR'])

dist.init_process_group(backend='nccl', init_method='env://')

local_rank = int(os.environ["LOCAL_RANK"])
device_id = local_rank
world_rank = dist.get_rank()

# Generate initial value on each rank
if world_rank == 0:
    initial_value = torch.tensor([5.0]).cuda(local_rank)
    print(f"Rank {world_rank}: Generated initial value: {initial_value.item()}")
else:
    initial_value = torch.tensor([0.0]).cuda(local_rank)

# Share the initial value on all nodes
dist.broadcast(initial_value, src=0)
print(f"Rank {world_rank}: Working with initial value: {initial_value.item()}")

# Generate a random value locally
random_value = torch.rand(1).cuda(local_rank)
print(f"Rank {world_rank}: Generated random value: {random_value.item()}")

# Add all local random values and make them available on each rank
dist.all_reduce(random_value, op=dist.ReduceOp.SUM)
print(f"Rank {world_rank}: Sum of random values: {random_value.item()}")

# Add the sum of random values to the initial value
result = initial_value + random_value
print(f"Rank {world_rank}: Updated initial value: {result.item()}")

# Cleanup distributed environment
dist.destroy_process_group()
print(f"Rank {world_rank}: Finished - exiting.")
