import os
import sys
import subprocess


def find_envs_folder():
    """
    Traverse the current and parent directories to find an 'envs' folder.
    Returns the path to the 'envs' folder if found, otherwise None.
    """
    current_dir = os.path.abspath(os.getcwd())

    while current_dir != os.path.dirname(current_dir):  # Stop at the root
        potential_envs_path = os.path.join(current_dir, "envs")
        if os.path.exists(potential_envs_path) and os.path.isdir(potential_envs_path):
            return potential_envs_path
        current_dir = os.path.dirname(current_dir)

    return None


def create_virtual_env(env_path):
    """
    Create a virtual environment at the given path.
    """
    try:
        subprocess.check_call([sys.executable, "-m", "venv", env_path])
        print(f"Virtual environment created successfully at: {env_path}")
        print_instructions(env_path)
    except subprocess.CalledProcessError as e:
        print(f"Failed to create virtual environment: {e}")


def print_instructions(env_path):
    """
    Print instructions to activate the virtual environment and set it up in VS Code.
    """
    print("\nTo activate the virtual environment, use the following command:")
    if os.name == "nt":  # Windows
        print(f"{env_path}\\Scripts\\activate")
    else:  # macOS/Linux
        print(f"source {env_path}/bin/activate")

    print("\nIf you are using VS Code:")
    print("1. Open VS Code.")
    print("2. Press Ctrl+Shift+P (or Cmd+Shift+P on macOS) to open the command palette.")
    print("3. Search for 'Python: Select Interpreter' and select it.")
    print("4. Choose the interpreter located at:")
    if os.name == "nt":  # Windows
        print(f"{env_path}\\Scripts\\python.exe")
    else:
        print(f"{env_path}/bin/python3")
    print("\nYour virtual environment is now ready to use!")


def main():
    print("Virtual Environment Manager")
    print("============================")

    # Find the 'envs' folder
    envs_folder = find_envs_folder()
    if not envs_folder:
        print("No 'envs' folder found in the current or parent directories.")
        return

    print(f"'envs' folder found at: {envs_folder}")

    # Prompt for environment name
    env_name = input("Enter the name of the virtual environment: ").strip()
    env_path = os.path.join(envs_folder, env_name)

    # Check if the environment already exists
    if os.path.exists(env_path):
        print(f"The virtual environment '{env_name}' already exists at '{env_path}'.")
        print_instructions(env_path)
    else:
        # Ask if the user wants to create the environment
        create_env = input(
            f"The virtual environment '{env_name}' does not exist. Do you want to create it? (y/n): "
        ).strip().lower()

        if create_env == "y":
            create_virtual_env(env_path)
        else:
            print(
                f"You chose not to create the environment. To create it yourself, use the following command:"
            )
            print(f"python -m venv {env_path}")


if __name__ == "__main__":
    main()
