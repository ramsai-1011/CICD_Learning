from mlops_project.train import train_and_evaluate


def test_model_accuracy_is_reasonable() -> None:
    accuracy, _ = train_and_evaluate()

    assert accuracy >= 0.75, f"Expected model accuracy above 0.75, got {accuracy}"
