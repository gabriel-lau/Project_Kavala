import pytest
from SRC.Main import *
import mock
import io

maze_normal = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'O', 'O', 'O', 'X', 'O', 'A', 'X'], ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'X'], ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'], ['X', 'O', 'X', 'O', 'X', 'X', 'O', 'X'], ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'], ['X', 'O', 'X', 'O', 'O', 'O', 'X', 'X'], ['X', 'B', 'X', 'X', 'X', 'X', 'X', 'X']]
maze_no_start_end = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'O', 'O', 'O', 'X', 'O', 'X', 'X'], ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'X'], ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'], ['X', 'O', 'X', 'O', 'X', 'X', 'O', 'X'], ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'], ['X', 'O', 'X', 'O', 'O', 'O', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
# ==================================================================
# Test for reading files

# Adding a normal maze returns a list with the maze coordinates
def test_read_maze_normal():
    with mock.patch('builtins.input', return_value='maze.csv'):
        assert read_file([]) == maze_normal

# Adding a maze with no start and end point returns a list with the maze coordinates
def test_read_maze_no_start_end():
    with mock.patch('builtins.input', return_value='maze-no-start-end.csv'):
        assert read_file([]) == maze_no_start_end

# Adding an empty maze file returns empty maze_list
def test_read_maze_empty():
    with mock.patch('builtins.input', return_value='maze-empty.csv'):
        assert read_file([]) == []

# Adding a csv file that does not exist returns empty maze_list
def test_read_csv_no_exist():
    with mock.patch('builtins.input', return_value='fake.csv'):
        assert read_file([]) == []

# Check if function store_start_end knows if maze has no start (A) or end (B) point
def test_store_start_end_name_error():
    with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout: 
        store_start_end([])
    assert fake_stdout.getvalue() == 'Maze does not have a start or end point.\n'

# Check if function store_start_end records the value of the start (A) and end (B) point
def test_store_start_end_row_exist():
    value = store_start_end(maze_normal)
    assert value == [[2, 7], [8, 2]]