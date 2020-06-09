# content of tests/test_paramatize_by_hook.py
test_data = [{"test_input": "3+5",
              "expected": 8,
              "id": "验证3+5=8"
              },
             {"test_input": "2+4",
              "expected": 6,
              "id": "验证2+4=6"
              },
             {"test_input": "6 * 9",
              "expected": 154,
              "id": "验证6*9=42"
              }
             ]


def pytest_generate_tests(metafunc):
    ids = []
    if "parameters" in metafunc.fixturenames:
        for data in test_data:  # 用test_data中的id作为测试用例名称
            ids.append(data['id'])
            print(ids)
        metafunc.parametrize("parameters", test_data, ids=ids, scope="function")  # 用test_data这个列表对parameters进行参数化。


def test_eval(parameters):
    assert eval(parameters['test_input']) == parameters['expected']