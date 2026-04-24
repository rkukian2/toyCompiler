import minic


def test_package_importable() -> None:
    assert minic.__version__ == "0.0.0"
