# Vite + Tailwind CSS Project Setup Script

This Python script automates the setup of a Vite project with Tailwind CSS integration. It simplifies the process of initializing a new Vite project, installing dependencies, and configuring Tailwind CSS. 

## Features

- Dynamically prompts for the project folder name to avoid duplicate folders.
- Sets up a Vite project with the `vanilla` template.
- Installs and configures Tailwind CSS, PostCSS, and Autoprefixer.
- Removes unnecessary files (`vite.svg`, `javascript.svg`, `counter.js`, and `style.css`).
- Creates and configures essential files, including:
  - A custom `index.html` file with Tailwind CSS linked.
  - A `tailwind.css` file containing Tailwind's base, components, and utilities.
  - An empty `main.js` file for your JavaScript.
- Configures `postcss.config.js` and `tailwind.config.js` automatically.

## Requirements

- Python 3.x
- Node.js and npm installed

## How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/kiansolati56/vite-tailwind-setup.git
   cd vite-tailwind-setup

2. Ensure you have the required dependencies installed:

Install Node.js
Install Python 3

3. Run the script:
   ```bash
   python setup.py

4. Enter the desired project folder name when prompted.
5. Navigate to the created folder and run the development server:
   ```
   cd <project-folder>
   npm run dev

6. Open the project in your browser and start building!

## Project Structure
- The structure of the created project is as follows:
    ```
    <project-folder>/
    ├── index.html
    ├── postcss.config.js
    ├── tailwind.config.js
    ├── package.json
    ├── src/
    │   ├── main.js
    │   └── tailwind.css
    ├── node_modules/
    └── ...other files

## About

This script was created by Kian Solati to streamline the process of setting up Vite projects with Tailwind CSS.
Feel free to fork, modify, and use it in your projects!

## Contact
Telegram : @MrCrowlley
