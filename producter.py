from customer import echo_task, say_hello_task, echo_number_task
from time import sleep
if __name__ == "__main__":
    # Example usage of the Celery tasks defined in customer.py

    # Call the echo_task with a message
    result_echo = echo_task.delay("Hello, World!")
    print(f"Echo Task Result: {result_echo.get()}")

    # Call the say_hello_task with a name
    result_hello = say_hello_task.delay("Alice")
    print(f"Say Hello Task Result: {result_hello.get()}")

    # Call the echo_number_task with a number
    result_number = echo_number_task.delay(10)
    result_number_2 = echo_number_task.delay(15)

    while not (result_number.ready() and result_number_2.ready()):
        print("Waiting for tasks to complete...")
        sleep(1)
    print("All tasks completed.")
