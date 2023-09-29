import os
import shutil
import subprocess
import nbformat
import requests  # Added requests for sending Slack messages


def send_slack_message(message):
    slack_webhook_url = "https://hooks.slack.com/services/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"
    message = {"text": message}
    response = requests.post(slack_webhook_url, json=message)
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(
            f"Failed to send message. Status code: {response.status_code}, Response: {response.text}"
        )


def add_code_to_notebook(notebook_path, code):
    with open(notebook_path, "r") as f:
        notebook = nbformat.read(f, as_version=4)

    code_cell = nbformat.v4.new_code_cell(code)

    notebook.cells.insert(0, code_cell)

    with open(notebook_path, "w") as f:
        nbformat.write(notebook, f)


def main():
    # Define the folder containing the notebooks to test
    notebook_folder = os.getcwd()

    # Define a list to store the names of notebooks that failed
    failed_notebooks = []

    # Iterate through all notebooks in the folder
    for notebook_name in os.listdir(notebook_folder):
        if notebook_name.endswith(".ipynb"):
            notebook_path = os.path.join(notebook_folder, notebook_name)

            # Create a copy of the notebook
            notebook_copy_path = os.path.join(
                notebook_folder, f"{notebook_name}_copy.ipynb"
            )
            shutil.copy(notebook_path, notebook_copy_path)

            # Add the code to the copied notebook
            code_to_add = 'import os\nCLEANLAB_API_KEY = os.getenv("CLEANLAB_API_KEY")'
            add_code_to_notebook(notebook_copy_path, code_to_add)

            # Run the copied notebook using subprocess
            try:
                subprocess.check_call(
                    [
                        "jupyter",
                        "nbconvert",
                        "--to",
                        "notebook",
                        "--execute",
                        notebook_copy_path,
                    ]
                )
            except subprocess.CalledProcessError:
                failed_notebooks.append(notebook_name)

            # Delete the copied notebook
            os.remove(notebook_copy_path)

    # Check for failed notebooks
    if failed_notebooks:
        message = f"The following notebooks failed: {', '.join(failed_notebooks)}"
        send_slack_message(message)
        for notebook_name in failed_notebooks:
            print(notebook_name)
    else:
        print(
            f"All notebooks passed successfully at {datetime.now().strftime('%d/%m/%Y_%H:%M:%S')}"
        )


if __name__ == "__main__":
    main()
