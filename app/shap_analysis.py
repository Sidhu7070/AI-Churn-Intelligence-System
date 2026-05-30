import shap
import pandas as pd
import numpy as np


def get_shap_explanation(model, input_df):

    explainer = shap.TreeExplainer(model)

    explanation = explainer(input_df)

    values = explanation.values

    print("SHAP Shape:", values.shape)

    # Handle binary classification output
    if len(values.shape) == 3:

        # shape = (samples, features, classes)
        values = values[0, :, 1]

    elif len(values.shape) == 2:

        # shape = (samples, features)
        values = values[0]

    values = np.abs(values)

    feature_df = pd.DataFrame({
        "Feature": input_df.columns,
        "Impact": values
    })

    feature_df = feature_df.sort_values(
        by="Impact",
        ascending=False
    )

    return feature_df.head(10)