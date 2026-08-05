import unittest

from customer import echo_task, say_hello_task, echo_number_task


class TestCeleryTasks(unittest.TestCase):
    """Tests at the seam of direct task-function invocation (no broker/worker).

    External behavior only: return values promised by each task's docstring.
    """

    def test_echo_task_returns_the_message(self):
        self.assertEqual(echo_task("Hello, World!"), "Hello, World!")

    def test_say_hello_task_returns_greeting_with_name(self):
        self.assertIn("Alice", say_hello_task("Alice"))

    def test_echo_number_task_returns_final_number_processed(self):
        # Processes 5 numbers starting from the given one: 10, 11, 12, 13, 14
        self.assertEqual(echo_number_task(10), 14)


if __name__ == "__main__":
    unittest.main()
