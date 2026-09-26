"""Run a query file against a fresh in-memory teaching database."""
import sqlite3
import sys
from pathlib import Path

def run(path):
    with sqlite3.connect(':memory:') as conn:
        conn.execute('PRAGMA foreign_keys = ON')
        conn.executescript(Path(__file__).with_name('seed.sql').read_text(encoding='utf-8'))
        pending = ''
        for char in Path(path).read_text(encoding='utf-8'):
            pending += char
            if char == ';' and sqlite3.complete_statement(pending):
                cursor = conn.execute(pending)
                if cursor.description:
                    print([column[0] for column in cursor.description])
                    for row in cursor:
                        print(row)
                pending = ''
        if pending.strip():
            cursor = conn.execute(pending)
            if cursor.description:
                print([column[0] for column in cursor.description])
                for row in cursor:
                    print(row)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('Usage: python curriculum/labs/run_sql.py query.sql')
    run(sys.argv[1])
