# Created by Kian Solati

import os
import subprocess

try:
    project_name = input("Enter the name of the project folder: ").strip()
    if not project_name:
        raise ValueError("Project name cannot be empty.")
    
    print(f"Creating Vite project in folder: {project_name}...")
    subprocess.run(
        f"npm create vite@latest {project_name} --template vanilla",
        check=True, shell=True
    )
    
    os.chdir(project_name)

    print("Removing unnecessary files...")
    unnecessary_files = [
        "public/vite.svg",
        "src/javascript.svg",
        "src/counter.js",
        "src/style.css"
    ]
    for file in unnecessary_files:
        if os.path.exists(file):
            os.remove(file)

    print("Clearing content of main.js...")
    main_js_path = "src/main.js"
    if os.path.exists(main_js_path):
        with open(main_js_path, "w", encoding="utf-8") as main_js_file:
            main_js_file.write("")

    print("Installing dependencies...")
    subprocess.run("npm install", check=True, shell=True)

    print("Installing Tailwind CSS...")
    subprocess.run("npm install -D tailwindcss postcss autoprefixer", check=True, shell=True)

    print("Initializing Tailwind CSS...")
    subprocess.run("npx tailwindcss init", check=True, shell=True)

    print("Creating PostCSS configuration...")
    with open("postcss.config.js", "w", encoding="utf-8") as postcss_file:
        postcss_file.write(
            """export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
};"""
        )

    print("Configuring Tailwind CSS...")
    with open("tailwind.config.js", "r+", encoding="utf-8") as config_file:
        content = config_file.read()
        config_file.seek(0)
        config_file.write(
            content.replace(
                "content: []",
                "content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}']",
            )
        )

    print("Creating files and directories...")
    os.makedirs("src", exist_ok=True)
    with open("src/tailwind.css", "w", encoding="utf-8") as css_file:
        css_file.write(
            """@tailwind base;\n@tailwind components;\n@tailwind utilities;"""
        )

    print("Updating index.html...")
    with open("index.html", "w", encoding="utf-8") as index_file:
        index_file.write(
            """<!doctype html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>By KianSolati, Enjoy</title>
  <link href="src/tailwind.css" rel="stylesheet">
</head>

<body class="bg-gray-100 flex justify-center items-center min-h-screen">
  <div class="bg-white p-6 shadow-lg rounded-md flex flex-col justify-center items-center">
    <h1 class="text-orange-400 text-3xl font-bold mb-2">Hello Guys!</h1>
    <h3 class="text-gray-600 font-medium mb-3">Created by Kian Solati, Enjoy</h3>
    <a href="https://github.com/kiansolati56" target="_blank"
      class="text-white bg-[#24292F] transition-all duration-300 focus:outline-none font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center hover:bg-[#050708]/70 me-2 mb-2">
      <svg class="w-4 h-4 me-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        viewBox="0 0 20 20">
        <path fill-rule="evenodd"
          d="M10 .333A9.911 9.911 0 0 0 6.866 19.65c.5.092.678-.215.678-.477 0-.237-.01-1.017-.014-1.845-2.757.6-3.338-1.169-3.338-1.169a2.627 2.627 0 0 0-1.1-1.451c-.9-.615.07-.6.07-.6a2.084 2.084 0 0 1 1.518 1.021 2.11 2.11 0 0 0 2.884.823c.044-.503.268-.973.63-1.325-2.2-.25-4.516-1.1-4.516-4.9A3.832 3.832 0 0 1 4.7 7.068a3.56 3.56 0 0 1 .095-2.623s.832-.266 2.726 1.016a9.409 9.409 0 0 1 4.962 0c1.89-1.282 2.717-1.016 2.717-1.016.366.83.402 1.768.1 2.623a3.827 3.827 0 0 1 1.02 2.659c0 3.807-2.319 4.644-4.525 4.889a2.366 2.366 0 0 1 .673 1.834c0 1.326-.012 2.394-.012 2.72 0 .263.18.572.681.475A9.911 9.911 0 0 0 10 .333Z"
          clip-rule="evenodd" />
      </svg>
      My Github
    </a>
  </div>
</body>

</html>"""
        )

    print("\nSuccessfully set up the project. Run the project with ...npm run dev...")
except ValueError as ve:
    print(f"Input error: {ve}")
except subprocess.CalledProcessError as e:
    print(f"Error while running a command: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
