class Model:
    def __init__(self, inputs, outputs):
        self.input_layer = inputs
        self.output_layer = outputs

        self.optimizer = None

    def predict(self, x):
        flow_layer = self.input_layer
        flow_data = x
        while flow_layer is not None:
            flow_data = flow_layer.forwardProp(x=flow_data)
            flow_layer = flow_layer.childLayer
        return flow_data

    def update_on_batch(self, dLoss):
        flow_layer = self.output_layer
        d_flow_data = dLoss
        while flow_layer is not None:
            d_flow_data = flow_layer.backProp(dy=d_flow_data)
            if flow_layer.have_weight():
                flow_layer.W = self.optimizer.optimize( #Weight update
                    parameter=flow_layer.W,
                    gradient=flow_layer.dW
                )
                flow_layer.b = self.optimizer.optimize( #bias update
                    parameter=flow_layer.b,
                    gradient=flow_layer.db
                )
            flow_layer = flow_layer.parentLayer
