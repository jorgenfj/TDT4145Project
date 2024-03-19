
# Project Setup Guide

This guide will walk you through setting up the database and installing the necessary Python package for this project.

## Database Setup

Follow these steps to set up the SQLite database for this project:

1. **Download SQLite3**
   - Visit the [SQLite Download Page](https://www.sqlite.org/download.html) and download SQLite for your operating system.

2. **Create the Database**
   - Open a terminal or command prompt.
   - Navigate to the directory where you have downloaded the project.
   - To create the database from the SQL script, run:
     ```shell
     sqlite3 dbname.db < teater.sql
     ```

## Installing Python and pip

Ensure you have Python installed on your system. pip (Python's package installer) is included with Python. To check if you have Python and pip installed, you can run the following commands in your terminal or command prompt:

```shell
python --version
pip --version
```

If you do not have Python installed, download and install it from the [official Python website](https://www.python.org/downloads/). During the installation process, make sure to select the option to add Python to your system's PATH.

## Installing PrettyTable

PrettyTable is a Python library that allows you to easily display tabular data. Follow these steps to install PrettyTable:

1. **Open a Terminal or Command Prompt**
   - Make sure you have Python and pip installed by following the steps above.

2. **Install PrettyTable**
   - Run the following command:
     ```shell
     pip install prettytable
     ```

You are now ready to use the project with SQLite and PrettyTable.

