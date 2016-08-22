import awesome


def test_awesome():
    ok = awesome.awesome()
    assert ok == "awesome"
    assert 1 == 1


if __name__ == "__main__":
    test_awesome()

