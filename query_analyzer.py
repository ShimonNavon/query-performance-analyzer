import time
import pyodbc


def main():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=YourDB;"
        "Trusted_Connection=yes;"
    )

    cursor = conn.cursor()

    query = "SELECT 1"

    start_time = time.time()

    cursor.execute(query)
    rows = cursor.fetchall()

    end_time = time.time()

    print(f"Execution time: {end_time - start_time:.4f} seconds")
    print(f"Rows returned: {len(rows)}")


if __name__ == "__main__":
    main()