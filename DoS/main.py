import configparser
import DoS_Attack as attack
import time
import sys


def main():
    config = configparser.ConfigParser()

    if not config.read('Config.conf'):
        print("Error: Config.conf file not found or is empty.")
        return 1  # Return an error code

    try:
        settings = config['settings']
    except KeyError:
        print("Error: [settings] section not found in Config.conf.")
        return 1


    start_time = time.time()

    try:
        exe = attack.DoS_Attack(settings)
        exe.create_thread_pool()
    except (ValueError, KeyError) as e:
        print(f"Configuration Error: {e}")
        print("Please check Config.conf for missing or invalid values.")
        return 1
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 1

    end_time = time.time()
    print(f"\nTotal simulation time: {end_time - start_time:.2f} seconds.")
    return 0


if __name__ == "__main__":
    sys.exit(main())