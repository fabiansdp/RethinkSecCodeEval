import os
import json
import importlib.util
import multiprocessing
import traceback
import contextlib
import tempfile
import ldap3
import smtplib
import socket

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
def list_folders(path):
    return [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]

def load_module_from_file(file_path, module_name):
    """Load a Python module from a file path"""
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if spec is None:
        return None
    
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def run_function(func, params, result_queue):
    try:
        result = func(**params)
        result_queue.put(('s',result))
    except Exception as e:
        result_queue.put(('e', e))

def safe_execute(function, params, timeout=5):
    result_queue = multiprocessing.Queue()
    p = multiprocessing.Process(target=run_function, args=(function, params, result_queue))
    p.start()
    p.join(timeout)
    if p.is_alive():
        p.terminate()
        return ('t',"Timeout occurred!")
    return result_queue.get() if not result_queue.empty() else ('n', "No result returned.")

@contextlib.contextmanager
def create_tempdir():
    with tempfile.TemporaryDirectory() as dirname:
        with chdir(dirname):
            yield dirname


@contextlib.contextmanager
def chdir(root):
    if root == ".":
        yield
        return
    cwd = os.getcwd()
    os.chdir(root)
    try:
        yield
    except BaseException as exc:
        raise exc
    finally:
        os.chdir(cwd)

# Example usage
directory_path = 'data/unittest'
folders = list_folders(directory_path)

data_dict = dict()
with open("data/wrong.jsonl") as f:
    for line in f:
        data = json.loads(line.rstrip())
        data_dict[data["id"]] = data


correct_dict = dict()
wrong_dict = dict()
file_404_dict = dict()
code_dict = dict()
exception_set = set()

print(len(folders))
print(len(data_dict))
for task_id in folders:
    if task_id not in data_dict:
        continue

    # Create a shared namespace for all modules
    namespace = {}
    setup_path = f"data/unittest/{task_id}/setup.py"

    # Load setup module if it exists
    if os.path.exists(setup_path):
        try:
            setup_content = read_file(setup_path)
            setup_module = load_module_from_file(setup_path, f"setup_{task_id}")
            # Add all setup module attributes to the namespace
            for name in dir(setup_module):
                # Skip private attributes
                if not name.startswith('__'):
                    namespace[name] = getattr(setup_module, name)
        except Exception as e:
            print({
                "task_id": task_id,
                "status": "error",
                "error": f"Failed to load setup.py: {str(e)}",
                "traceback": traceback.format_exc(),
                "statistics": {
                    "total_tests": 0,
                    "passed_tests": 0,
                    "success_rate": 0
                }
            })
    
    data_dict[task_id]["unittest"]["setup"] = setup_content
    test_code = f"""{setup_content}

{data_dict[task_id]["ground_truth"]["code_before"]}

{data_dict[task_id]["ground_truth"]["patched_code"]}

{data_dict[task_id]["ground_truth"]["code_after"]}
"""
    test_case_module = load_module_from_file(f"data/unittest/{task_id}/test_case.py", f"test_case_{task_id}")
    function_name = getattr(test_case_module, "function", None)
    test_cases = getattr(test_case_module, "test_cases", None)

    with create_tempdir():
        try:
            exec(test_code, namespace)
        except Exception as e:
            print("----------------- ERROR IN TEST CODE ---------------------")
            print(task_id)
            print(test_code)
            print(e)
            exception_set.add(type(e))
            code_dict[task_id] = data_dict[task_id]
            continue


        # Get the function from the namespace
        function = namespace.get(function_name)

        results = []
        correct_tcs = []

        for params in test_cases:
            try:
                result = safe_execute(function, params)
                if result[0] == 'e':
                    # print(test_code)
                    exception_set.add(type(result[1]))

                    if type(result[1]) in [AttributeError, TypeError, json.decoder.JSONDecodeError, SyntaxError, OSError, ldap3.core.exceptions.LDAPInvalidTlsSpecificationError, smtplib.SMTPServerDisconnected, socket.gaierror]:
                        print("----------------- ERROR IN OUTPUT ---------------------")
                        print(task_id)
                        print(params)
                        print(result)
                        print(test_code)
                        wrong_dict[task_id] = data_dict[task_id]
                        break
                    # else:
                    #     print("----------------- NO ERROR ---------------------")
                    #     print(task_id)
                    #     print(params)
                    #     print(result)

                    correct_tcs.append((params, result[1]))

                else:
                    output = result[1]
                    if isinstance(result[1], Exception):
                        output = type(result[1])

                    correct_tcs.append((params, result[1]))

            except Exception as e:
                print("Exception", e, type(e))
                # print(type(e))
                exception_set.add(type(e))
                wrong_dict[task_id] = data_dict[task_id]

        if len(correct_tcs) == len(test_cases):
            data_dict[task_id]["unittest"]["testcases"] = f"testcases = {correct_tcs}"
            correct_dict[task_id] = data_dict[task_id]


print(exception_set)

def write_jsonl_file(filename, data_dict):
    with open(filename, 'w') as f:
        for item in data_dict:
            try:
                f.write(json.dumps(data_dict[item])+ "\n")
            except:
                print(data_dict[item])

def append_jsonl_file(filename, data_dict):
    with open(filename, 'a') as f:
        for item in data_dict:
            try:
                f.write(json.dumps(data_dict[item])+ "\n")
            except:
                print(data_dict[item])

# append_jsonl_file("correct.jsonl", correct_dict)
# write_jsonl_file("data/file404.jsonl", file_404_dict)
# append_jsonl_file("data/wrong.jsonl", wrong_dict)
# write_jsonl_file("data/syntax.jsonl", code_dict)