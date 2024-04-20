import os
import subprocess
import sys
import pyttsx3
import readline
import sqlite3
from datetime import datetime

engine = pyttsx3.init(driverName="espeak")
con = sqlite3.connect("tasks.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS tasks(name code, status code, date)")
print("< Enter 'help' to help you >")

codes = [
    "create py",
    "create html",
    "brave",
    "brave youtube",
    "$",
    "say",
    "run",
    "do py",
    "salman",
    "ctask",
    "stasks",
    "dtask",
    "utask",
    "comt",
    "help",
    "exit",
    "quit",
    "reset",
]


def create_folder(name):
    folder_path = f"/home/adamwael/{name}"
    if os.path.exists(folder_path):
        print(
            f"🤖 computer: 🤨 Folder '{name}' already exists. Please enter a different name."
        )
        return False
    else:
        os.mkdir(folder_path)
        print(f"🤖 computer: 😀 Folder '{name}' created successfully.")
        return True


def execute_command(command):
    os.system(f"{command}")


def start():
    while True:
        readline.parse_and_bind("tab: complete")

        def complete(text, state):
            volcab = codes
            results = [x for x in volcab if x.startswith(text)] + [None]
            return results[state]

        readline.set_completer(complete)
        code = input("✍  Enter Your code: ")

        if code.lower() == "create py":
            while True:
                name = input("✍📁  Enter folder name: ")
                if " " in name:
                    name = input("✍📁  Enter folder name: ")
                if create_folder(name):
                    os.system(f"touch /home/adamwael/{name}/main.py")
                    os.system(
                        f"echo \"print('Hello, World!')\" > /home/adamwael/{name}/main.py"
                    )
                    print("🤖 computer: Done")
                    engine.say("Done")
                    engine.runAndWait()
                    print(f"/home/adamwael/{name}/")
                    os.system(f"nautilus /home/adamwael/{name}")
                    break

        elif code.lower() == "create html":
            while True:
                name = input("✍📁 Enter folder name: ")
                if " " in name:
                    name = input("✍📁  Enter folder name: ")
                if create_folder(name):
                    css_code = """
                    body {
                        margin: 0;
                        padding: 0;
                    }
                    """
                    os.system(
                        f"touch /home/adamwael/{name}/index.html /home/adamwael/{name}/style.css /home/adamwael/{name}/main.js"
                    )
                    os.system(
                        f"""echo "
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <link rel='stylesheet' href='style.css'>
        <title>Document</title>
    </head>
    <body>
        <h1>Hello World</h1>
        <script src='main.js'></script>
    </body>
</html>
                        " > /home/adamwael/{name}/index.html"""
                    )
                    os.system(f'echo "{css_code}" > /home/adamwael/{name}/style.css')
                    os.system(
                        f"echo \"console.log('Hello, World!');\" > /home/adamwael/{name}/main.js"
                    )
                    print("🤖 computer: Done")
                    engine.say("Done")
                    engine.runAndWait()
                    os.system(f"nautilus /home/adamwael/{name}")
                    break

        elif "brave" in code:
            search = code.replace("brave ", "").replace(" ", "+")
            if "youtube" in search:
                you2b = input("✍🔎  Enter your youtube search: ").replace(" ", "+")
                execute_command(
                    f"brave-browser https://www.youtube.com/results?search_query={you2b}"
                )
            else:
                execute_command(
                    f"brave-browser https://www.google.com/search?q={search}"
                )
            print("🤖 computer: Done")
            engine.say("Done")
            engine.runAndWait()

        elif "$" in code:
            command = code.replace("$", "")
            execute_command(command)

        elif code.lower() in ("exit", "quit"):
            print("🤖 computer: 🚪 Exited...")
            return

        elif "say" in code.lower():
            talk = code.replace("say", "")
            print(f"🤖 computer: {talk}")
            engine.say(talk)
            engine.runAndWait()

        elif "run" in code.lower():
            file = code.replace("run ", "").replace(" ", "\\ ")
            if "html" in file or "htm" in file:
                print(f"🤖 computer: opening {file}")
                os.system(f"brave-browser {file}")
                print("--------")

            elif "py" in file or "htm" in file:
                print(f"🤖 computer: running {file}")
                os.system(f"python3 {file}")
                print("--------")

            else:
                print("🤖 computer: i don't found this extintion")

        elif "do py" in code.lower():
            run = code.replace("do py ", "")
            os.system("python3")

        elif code.lower() == "salman":
            os.system(f"ssh salman@10.0.0.8")

        elif code.lower() == "ctask":
            task = input("What's your task, (c): ")
            tasks = [(task)]
            if task.lower() == "c":
                pass
            else:
                date_ = datetime.now()
                cur.execute(
                    "INSERT INTO tasks VALUES(?,?,?)",
                    (
                        task,
                        "❌",
                        datetime.now(),
                    ),
                )
                con.commit()
                print("🤖 computer: Your task added")
                engine.say("Your task added")
                engine.runAndWait()

        elif code.lower() == "stasks":
            cur.execute("SELECT rowid,* FROM tasks")

            print("-" * 20)

            print("ID- Task- Status- date-added")
            for i in cur.fetchall():
                print(
                    str(i[0]) + "- " + str(i[1]) + " - " + str(i[2]) + " - " + str(i[3])
                )
            print("-" * 20)

        elif code.lower() == "comt":
            cur.execute("SELECT rowid,* FROM tasks")
            print("-" * 20)
            print("ID- Task- Status- date-added")
            for i in cur.fetchall():
                print(str(i[0]) + "- " + str(i[1]) + " - " + str(i[2]))
            print("-" * 20)

            task = input("Enter your tasks id completed: ")
            cur.execute(
                "UPDATE tasks SET status = ? WHERE rowid = ?",
                (
                    "✅",
                    task,
                ),
            )
            con.commit()
            print("🤖 computer: your task completed")
            engine.say("your task completed")
            engine.runAndWait()

        elif code.lower() == "dtask":
            cur.execute("SELECT rowid,* FROM tasks")
            print("-" * 20)
            print("ID- Task- Status- date-added")
            for i in cur.fetchall():
                print(str(i[0]) + "- " + str(i[1]) + " - " + str(i[2]))
            print("-" * 20)

            task = input("Write your task id if no (c): ")
            if task == "c":
                pass

            else:
                cur.execute("DELETE FROM tasks WHERE rowid=?", (task,))
                con.commit()
                print("🤖 computer: task was deleted")
                engine.say("task was deleted")
                engine.runAndWait()

        elif code.lower() == "utask":
            cur.execute("SELECT rowid,* FROM tasks")
            print("-" * 20)
            print("ID- Task- Status- date-added")
            for i in cur.fetchall():
                print(str(i[0]) + "- " + str(i[1]) + " - " + str(i[2]))
            print("-" * 20)

            task = input("Write your task id if no (c): ")
            update = input("What do you want to update: ")
            if task == "c":
                pass
            else:
                cur.execute(
                    "UPDATE tasks SET name = ? WHERE rowid=?",
                    (
                        update,
                        task,
                    ),
                )
                con.commit()
                print("🤖 computer: task was updated")
                engine.say("task was updated")
                engine.runAndWait()

        elif code.lower() == "reset":
            os.system("clear")

            def restart_program():
                """Restarts the current Python program."""
                python = sys.executable
                script = os.path.abspath(__file__)
                subprocess.call([python, script])
                os._exit(0)  # Exit gracefully to avoid potential errors

            # Example usage:
            if __name__ == "__main__":
                # Your main program code here

                # When you want to restart:
                restart_program()

        elif code == "":
            start()
            break
            return

        elif "help" in code.lower():
            print(
                """
                                    *All program commands*
                                     ---------------------
                                     
              ------------------------*create new projects*---------------------+
            -> create py - To make new python project                           |
            -> create html - To make new website with all files (html, css, js) |
              ------------------------------------------------------------------+
              ------------------------*Searching*------------------------------+
            -> brave [your search] - To search on your browser                 |
            -> brave youtube - To search on youtube                            |
              -----------------------------------------------------------------+
              ------------------------*Computer*--------------------------------------------------+
            -> $[terminal command] - To write terminal commands easy                              |
            -> say [...] - To make computer say                                                   |
            -> run [full python file or html path] - To run html on browser or run python project |
            -> do py - To open python terminal editor                                             |
            -> salman - To connect with computer                                                  |
              ------------------------------------------------------------------------------------+
              ----------------------------*Your tasks*-------------------------+
            -> ctask - To create new task                                      |
            -> stasks - To show all your tasks                                 |
            -> dtask - To delete any select task with id                       |
            -> utask - To update any select task with id                       |                       
            -> comt - To complete any select task with id                      |
              -----------------------------------------------------------------+
              --------------------------*program*------------------------------+
            -> help - To help you with programe commands                       |
            -> exit or quit - To exit from the program                         |
            -> reset - To Restart the program                                  |
              -----------------------------------------------------------------+
              ---------------------------*Hints*-------------------------------+
            -> $clear - To clear your terminal                                 |
              -----------------------------------------------------------------+
              
            """
            )

        else:
            print("🤖 computer: Not found this code")
            engine.say("Not found this code")
            engine.runAndWait()

            def did_you_mean(user_input, options):
                """Suggests closest match based on simple string similarity.

                Args:
                    user_input: The user's input string.
                    options: A list of possible options.

                Returns:
                    A string suggesting the closest match, or None if no close match found.
                """
                # Calculate edit distance (number of edits to transform one string to another)
                min_distance = float("inf")  # Initialize with infinity
                closest_match = None

                for option in options:
                    distance = sum(a != b for a, b in zip(user_input, option))
                    if distance < min_distance:
                        min_distance = distance
                        closest_match = option

                if min_distance <= 1:  # Adjust threshold as needed (e.g., for typos)
                    print(f"Did you mean '{closest_match}'?")
                    print('If Not "help"!')

                else:
                    return None

                # Example usage (same as previous example)

            did_you_mean(code, codes)


start()

con.close()
