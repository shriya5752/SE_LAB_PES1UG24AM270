# Reflection Report

**1. What was the most severe issue found by Bandit, and why is it dangerous?**
Bandit found a High severity issue (B605) where `os.system()` was used to print badges. This is dangerous because it allows shell command injection, letting an attacker execute malicious terminal commands if they control the `eventName` variable. I fixed this by deleting the unused function. Additionally, Bandit flagged the use of `pickle` (B301) as a Medium severity issue. Pickle is insecure because it allows arbitrary code execution if an attacker tampers with the saved `.pkl` file. I fixed this by migrating the save/load functionality to the safer `json` module.

**2. How did fixing the Flake8 formatting issues make the code easier to read?**
Flake8 caught spacing issues, inline comment spacing, and missing blank lines. Adding whitespace around operators and ensuring consistent blank lines between functions makes the code visually cleaner and much easier to scan for logical errors.

**3. Explain the logical bug you fixed in Pylint (the default argument issue) and how it affected the program's output.**
The `create_event` function used `guests=[]` as a default argument. In Python, this list is shared across all function calls. This caused guests from Tech Meetup to bleed into Alumni Dinner, making Alumni Dinner full too early, and showing the wrong guests in the output. Changing it to `guests=None` and initializing the list inside the function fixed the shared state.

**4. What was your final Pylint score?**
My final Pylint score was 10.00/10.