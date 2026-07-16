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

    return "ok"


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

    return "ok"

@app.task(name="echo_number_task")
def echo_number_task(number):
    """
    A simple Celery task that echoes back the provided number.

    Args:
        number (int): The number to be echoed.

    Returns:
        str: A confirmation message.
    """
    max = number + 5
    while(number < max):
        print(f"Echoing number: {number}")
        number += 1
        sleep(1)  # Simulate some processing time
    return "ok"