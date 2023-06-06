import json
import onnx
import numpy as np

# Load the exported data from the JSON file
with open('onnx.json') as f:
    data = json.load(f)

# Convert the data to a numpy array
array = np.array(data['vectors'])

# Create an ONNX tensor
tensor = onnx.helper.make_tensor(name='vectors', data_type=onnx.TensorProto.FLOAT, dims=array.shape, vals=array.flatten())

# Create an ONNX graph with the tensor as input and output
graph = onnx.helper.make_graph(
    nodes=[],
    name='QdrantExportedData',
    inputs=[onnx.helper.make_tensor_value_info('vectors', onnx.TensorProto.FLOAT, array.shape)],
    outputs=[onnx.helper.make_tensor_value_info('vectors', onnx.TensorProto.FLOAT, array.shape)],
    initializer=[tensor]
)

# Create an ONNX model with the graph
model = onnx.helper.make_model(graph)

# Save the model to a file
onnx.save(model, 'ix.onnx')