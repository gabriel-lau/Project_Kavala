import pytest
from SRC.Main import *
import mock
import io

maze_normal = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'O', 'O', 'O', 'X', 'O', 'A', 'X'], ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'X'], ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'], ['X', 'O', 'X', 'O', 'X', 'X', 'O', 'X'], ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'], ['X', 'O', 'X', 'O', 'O', 'O', 'X', 'X'], ['X', 'B', 'X', 'X', 'X', 'X', 'X', 'X']]
maze_no_start_end = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'O', 'O', 'O', 'X', 'O', 'X', 'X'], ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'X'], ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'], ['X', 'O', 'X', 'O', 'X', 'X', 'O', 'X'], ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'], ['X', 'O', 'X', 'O', 'O', 'O', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
# ==================================================================
# Test for reading files

def test_read_maze_normal():
    with mock.patch('builtins.input', return_value='maze.csv'):
        assert read_file([]) == maze_normal
    
def test_read_maze_empty():
    with mock.patch('builtins.input', return_value='maze-empty.csv'):
        assert read_file([]) == []

def test_read_maze_no_start_end():
    with mock.patch('builtins.input', return_value='maze-no-start-end.csv'):
        assert read_file([]) == maze_no_start_end

def test_store_start_end_name_error():
    with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout: 
        store_start_end([])
    assert fake_stdout.getvalue() == 'Maze does not have a start or end point.\n'

def test_store_start_end_row_exist():
    value = store_start_end(maze_normal)
    assert value == [[2, 7], [8, 2]]
