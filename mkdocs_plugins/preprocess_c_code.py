from mkdocs.plugins import BasePlugin
import os
import subprocess
import re
import glob

class PreprocessCCodePlugin(BasePlugin):
    def on_pre_build(self, config):
        # Preprocess all markdown files before building
        self.preprocess_markdown_files()
        return config

    def preprocess_markdown_files(self):
        # Find all markdown files in the specified directory
        markdown_files = glob.glob('docs/programming/c/*.md')  # Adjust the path as needed

        for md_file in markdown_files:
            self.process_markdown_file(md_file)

    def run_c_code(self, code):
        """Compiles and runs the C code, returning the output."""
        with open('temp.c', 'w') as f:
            f.write(code)

        # Compile the C code
        compile_process = subprocess.run(['gcc', 'temp.c', '-o', 'temp'], capture_output=True, text=True)

        if compile_process.returncode != 0:
            return f"Compilation Error:\n{compile_process.stderr}"

        # Run the compiled code
        run_process = subprocess.run(['./temp'], capture_output=True, text=True)
        return run_process.stdout if run_process.returncode == 0 else f"Runtime Error:\n{run_process.stderr}"

    def process_markdown_file(self, filepath):
        """Processes the markdown file to replace C code blocks with tabbed content."""
        with open(filepath, 'r') as file:
            content = file.read()

        # Regex to find C code blocks
        code_blocks = re.findall(r'```c exec(.*?)```', content, re.DOTALL)

        for code in code_blocks:
            output = self.run_c_code(code.strip())
            tabbed_content = f"=== \"Source\"\n" \
                             f"    ```c\n" \
                             f"{code.strip()}\n" \
                             f"    ```\n" \
                             f"=== \"Output\"\n" \
                             f"    ```\n" \
                             f"{output}\n" \
                             f"    ```\n"
            content = content.replace(f'```c{code}```', tabbed_content)
        print(f"Processed content for {filepath}:\n{content}\n")
