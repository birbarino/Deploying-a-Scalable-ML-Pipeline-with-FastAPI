import pytest
from sklearn.ensemble import RandomForestClassifier
from ml.model import inference, train_model, compute_model_metrics
import numpy as np

def test_inference():
    """
    Test that inference() returns valid label predictions
    """
    X = np.random.rand(800, 8)
    y = np.random.randint(0, 2, size=800)
    model = RandomForestClassifier(random_state=100).fit(X, y)

    preds = inference(model, np.random.rand(160, 8))
    valid_preds = np.array([p in model.classes_ for p in preds])

    assert valid_preds.all()

def test_train_model():
    """
    Test that a random forest classifier is returned and it had data fit to it
    """
    # Generate random data sample
    X = np.random.rand(800, 8)
    y = np.random.randint(0, 2, size=800)
    test_model = train_model(X, y)

    assert isinstance(test_model, RandomForestClassifier)  
    
    # trained/fit models will have the feature_importances_ method
    assert hasattr(test_model, "feature_importances_")

def test_compute_model_metrics():
    """
    Test to ensure compute_model_metrics returns floats
    """
    real = [1, 1, 1, 0, 0, 1]
    pred = [1, 1, 1, 1, 1, 1]

    p, r, fb = compute_model_metrics(real, pred)

    assert isinstance(p, float)
    assert isinstance(r, float)
    assert isinstance(fb, float)
