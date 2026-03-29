import time


def main():
    start_time = time.time()

    # Temporary placeholder so we can verify the script runs
    time.sleep(1)

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"Execution time: {execution_time:.4f} seconds")


if __name__ == "__main__":
    main()