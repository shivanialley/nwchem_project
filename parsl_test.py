import parsl
from parsl import python_app, bash_app
from parsl.configs.local_threads import config

# Load the Parsl configuration
parsl.load(config)

@python_app
def hello_python():
    return 'Hello from Python!'

@bash_app
def hello_bash():
    return 'echo "Hello from Bash!"'

if __name__ == "__main__":
    python_future = hello_python()
    bash_future = hello_bash()

    print(python_future.result())
    print(bash_future.result())

