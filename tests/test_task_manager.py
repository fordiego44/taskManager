import io
import json
import os
import sys
import tempfile
import unittest

from task_manager import TaskManager, Task


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.filename = os.path.join(self.temp_dir.name, "tasks.json")
        self.original_filename = TaskManager.FILENAME
        TaskManager.FILENAME = self.filename
        self.manager = TaskManager()

    def tearDown(self):
        TaskManager.FILENAME = self.original_filename
        self.temp_dir.cleanup()

    def test_add_task_saves_task(self):
        self.manager.add_task("Comprar leche")

        self.assertEqual(len(self.manager._tasks), 1)
        task = self.manager._tasks[0]
        self.assertIsInstance(task, Task)
        self.assertEqual(task.description, "Comprar leche")
        self.assertFalse(task.completed)
        self.assertEqual(task.id, 1)

        with open(self.filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        self.assertEqual(data, [{"id": 1, "description": "Comprar leche", "completed": False}])

    def test_complete_task_marks_task_completed_and_saves(self):
        self.manager.add_task("Pagar facturas")

        captured_output = io.StringIO()
        sys_stdout = sys.stdout
        sys.stdout = captured_output

        try:
            self.manager.complete_task(1)
        finally:
            sys.stdout = sys_stdout

        task = self.manager._tasks[0]
        self.assertTrue(task.completed)
        self.assertIn("Tarea completada", captured_output.getvalue())

        with open(self.filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        self.assertEqual(data[0]["completed"], True)

    def test_delete_task_removes_task_and_saves(self):
        self.manager.add_task("Leer un libro")

        captured_output = io.StringIO()
        sys_stdout = sys.stdout
        sys.stdout = captured_output

        try:
            self.manager.delete_task(1)
        finally:
            sys.stdout = sys_stdout

        self.assertEqual(self.manager._tasks, [])
        self.assertIn("Tarea eliminada: #1", captured_output.getvalue())

        with open(self.filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        self.assertEqual(data, [])

    def test_load_tasks_restores_existing_tasks(self):
        self.manager.add_task("Aprender Python")
        new_manager = TaskManager()

        self.assertEqual(len(new_manager._tasks), 1)
        self.assertEqual(new_manager._tasks[0].description, "Aprender Python")
        self.assertEqual(new_manager._tasks[0].id, 1)

    def test_list_tasks_prints_tasks(self):
        self.manager.add_task("Hacer ejercicio")

        captured_output = io.StringIO()
        sys_stdout = sys.stdout
        sys.stdout = captured_output

        try:
            self.manager.list_tasks()
        finally:
            sys.stdout = sys_stdout

        text = captured_output.getvalue()
        self.assertIn("#1: Hacer ejercicio", text)
        self.assertIn("[ ", text)

    def test_complete_nonexistent_task_shows_error(self):
        captured_output = io.StringIO()
        sys_stdout = sys.stdout
        sys.stdout = captured_output

        try:
            self.manager.complete_task(99)
        finally:
            sys.stdout = sys_stdout

        self.assertIn("Tarea no encontrada: #99", captured_output.getvalue())

    def test_delete_nonexistent_task_shows_error(self):
        captured_output = io.StringIO()
        sys_stdout = sys.stdout
        sys.stdout = captured_output

        try:
            self.manager.delete_task(99)
        finally:
            sys.stdout = sys_stdout

        self.assertIn("Tarea no encontrada: #99", captured_output.getvalue())


if __name__ == "__main__":
    unittest.main()
