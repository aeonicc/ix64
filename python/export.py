
import torch
import torchvision

# Load a PyTorch model
model = torchvision.models.resnet18(pretrained=True)

# Set the model to evaluation mode
model.eval()

# Export the model to ONNX format
dummy_input = torch.randn(1, 3, 224, 224)
input_names = ["input"]
output_names = ["output"]
torch.onnx.export(model, dummy_input, "resnet18.onnx", verbose=True, input_names=input_names, output_names=output_names)