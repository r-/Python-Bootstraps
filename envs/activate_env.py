import os
import platform

def find_envs_folder():
    """
    Traverse the script's location and its parent directories to find an 'envs' folder.
    Returns the path to the 'envs' folder if found, otherwise None.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))

    while script_dir != os.path.dirname(script_dir):  # Stop at the root
        potential_envs_path = os.path.join(script_dir, "envs")
        if os.path.exists(potential_envs_path) and os.path.isdir(potential_envs_path):
            return potential_envs_path
        script_dir = os.path.dirname(script_dir)

    return None

def list_virtual_environments(envs_folder):
    """
    List all subdirectories in the 'envs' folder that are potential virtual environments.
    """
    return [
        folder
        for folder in os.listdir(envs_folder)
        if os.path.isdir(os.path.join(envs_folder, folder))
    ]

def print_activation_instructions(env_path):
    """
    Print activation instructions for the selected virtual environment.
    """
    os_name = platform.system()

    print("\nTo activate the virtual environment, use one of the following commands:")

    if os_name == "Windows":
        print(f"1. Navigate to the environment's 'Scripts' directory and run:")
        print(f"   cd {env_path}\\Scripts")
        print(f"   activate")
        print("\n   OR\n")
        print(f"2. Use the direct path in Command Prompt:")
        print(f"   {env_path}\\Scripts\\activate.bat")
        print("\n**If you encounter an execution policy error, run one of the following commands in PowerShell:**")
        print("   Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process")
        print("   OR")
        print("   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser")
    else:  # macOS/Linux
        print(f"source {env_path}/bin/activate")

    print("\n**Note:** If you are running this script inside a VS Code terminal,")
    print("you may need to close the current terminal and reopen it before running the activation command.")
    print("This ensures VS Code correctly applies the environment settings.")
    print("\n**Additional Note:** If you are using VS Code, you should also select the correct Python interpreter.")
    print("Follow these steps to select the interpreter:")
    print("1. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS) to open the Command Palette.")
    print("2. Type 'Python: Select Interpreter' and select it from the list.")
    print("3. Choose the interpreter located at:")
    if os_name == "Windows":
        print(f"   {env_path}\\Scripts\\python.exe")
    else:
        print(f"   {env_path}/bin/python3")
    print("\nThis ensures VS Code uses the correct virtual environment for running your code.")

def main():
    print("Python Virtual Environment Activator")
    print("=====================================")

    # Find the 'envs' folder
    envs_folder = find_envs_folder()
    if not envs_folder:
        print("No 'envs' folder found in the script or parent directories.")
        return

    print(f"'envs' folder found at: {envs_folder}")

    # List available environments
    environments = list_virtual_environments(envs_folder)
    if not environments:
        print("No virtual environments found in the 'envs' folder.")
        return

    print("\nAvailable Virtual Environments:")
    for i, env in enumerate(environments, start=1):
        print(f"{i}. {env}")

    # Ask the user to choose an environment
    try:
        choice = int(input("\nEnter the number of the environment to activate: ").strip())
        if 1 <= choice <= len(environments):
            selected_env = environments[choice - 1]
            env_path = os.path.join(envs_folder, selected_env)
            print_activation_instructions(env_path)
        else:
            print("Invalid choice. Exiting.")
    except ValueError:
        print("Invalid input. Exiting.")

if __name__ == "__main__":
    main()
