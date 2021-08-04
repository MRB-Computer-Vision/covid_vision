
#load image
# initialize lime_explain
from covid_vision.interpretability.lime_explain import LimeExplain

lime_explain = LimeExplain()

#run explain

image_result = lime_explain.explain_xray(img)

