import os
import shutil
import subprocess
import nbformat
import os
import datetime
import requests  # Added requests for sending Slack messages


def send_slack_message(message):
    slack_webhook_url = os.getenv("SLACK_WEB_HOOK_URL")
    message = {"text": message}
    response = requests.post(slack_webhook_url, json=message)
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(
            f"Failed to send message. Status code: {response.status_code}, Response: {response.text}"
        )


def replace_code_in_notebook(notebook_path, old_code, new_code):
    with open(notebook_path, "r") as f:
        notebook = nbformat.read(f, as_version=4)

    for cell in notebook.cells:
        if cell.cell_type == "code" and old_code in cell.source:
            cell.source = cell.source.replace(old_code, new_code)
            break

    with open(notebook_path, "w") as f:
        nbformat.write(notebook, f)

old_code = 'API_KEY = "<insert your API key>"\nstudio = Studio(API_KEY)'
new_code = 'import os\nAPI_KEY = os.getenv("CLEANLAB_API_KEY")'



import os
import subprocess
import papermill as pm
import time

def main():
    # Define the folder containing the notebooks to test
    notebook_folder = os.path.join(os.getcwd(), "cleanlab-studio-api")

    # Define a list to store the names of notebooks that failed
    failed_notebooks = []

    # Iterate through all notebooks in the folder
    for notebook_name in os.listdir(notebook_folder):
        if notebook_name.endswith(".ipynb"):
            notebook_path = os.path.join(notebook_folder, notebook_name)

            # Run the notebook using Papermill
            try:
                output_notebook_path = os.path.join(
                    notebook_folder, f"{notebook_name}_output.ipynb"
                )
                replace_code_in_notebook(notebook_path, old_code, new_code)

                # Add the code to the notebook before executing
                code_to_add = 'import os\nCLEANLAB_API_KEY = os.environ["CLEANLAB_API_KEY"]'
                pm.execute_notebook(
                    notebook_path,
                    output_notebook_path,
                    parameters=dict(CLEANLAB_API_KEY=os.environ['CLEANLAB_API_KEY']),
                    prepare_only=True,
                )

                # Overwrite the original notebook with the modified one
                os.rename(output_notebook_path, notebook_path)

                # Execute the notebook
                pm.execute_notebook(notebook_path, notebook_path)
            except Exception as e:
                failed_notebooks.append(notebook_name)

            # Add a 10-second pause
            time.sleep(10)

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
