from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClasssifier

iris = load_iris()

X,Y = iris.data, iris.target
X_train, X_test, Y_train, Y_test = train_test_split(X,Y)

model = RandomForestClasssifier()
model.fit(X_train,Y_train)

##convert to onnx format
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType
initial_type = [('float_input', FloatTensorType([None, 4]))]
onx = convert_sklearn(clr, initial_types=initial_type)
with open("rf_iris.onnx", "wb") as f:
    f.write(onx.SerializeToString())