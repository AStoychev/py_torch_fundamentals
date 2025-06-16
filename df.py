import torch
print("PyTorch версия:", torch.__version__)
print("CUDA налична:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("CUDA устройство:", torch.cuda.get_device_name(0))
else:
    print("CUDA устройство не е намерено")