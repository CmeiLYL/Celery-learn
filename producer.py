from customer import echo_number_task, echo_task, say_hello_task

if __name__ == "__main__":
    # Example usage of the Celery tasks defined in customer.py

    # Call the echo_task with a message
    result_echo = echo_task.delay("Hello, World!")
    print(f"Echo Task Result: {result_echo.get(timeout=10)}")

    # Call the say_hello_task with a name
    result_hello = say_hello_task.delay("Alice")
    print(f"Say Hello Task Result: {result_hello.get(timeout=10)}")

    # Call the echo_number_task with numbers
    result_number = echo_number_task.delay(10)
    result_number_two = echo_number_task.delay(15)

    print("Waiting for tasks to complete...")
    print(f"Number Task 1 Result: {result_number.get(timeout=60)}")
    print(f"Number Task 2 Result: {result_number_two.get(timeout=60)}")
    print("All tasks completed.")
