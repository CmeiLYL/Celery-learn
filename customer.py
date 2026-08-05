from time import sleep

from celery_app import app


@app.task(name="echo_task")
def echo_task(message):
    """
    A simple Celery task that echoes back the provided message.

    Args:
        message (str): The message to be echoed.

    Returns:
        str: The echoed message.
    """
    print(f"Echoing message: {message}")

    return message


@app.task(name="say_hello_task")
def say_hello_task(name):
    """
    A simple Celery task that returns a greeting message.

    Args:
        name (str): The name of the person to greet.

    Returns:
        str: A greeting message.
    """
    print(f"Greeting {name}")

    return f"Hello, {name}!"


@app.task(name="echo_number_task")
def echo_number_task(number):
    """
    A simple Celery task that prints an ascending sequence of 5 numbers
    starting from the given number, sleeping 1 second between each, to
    simulate a long-running task.

    Args:
        number (int): The number to start from.

    Returns:
        int: The final number processed.
    """
    limit = number + 5
    for current in range(number, limit):
        print(f"Echoing number: {current}")
        sleep(1)  # Simulate some processing time
    return limit - 1
