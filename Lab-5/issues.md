# Static Code Analysis Issues

| Issue | Type | Line(s) | Description | Fix Approach |
| :--- | :--- | :--- | :--- | :--- |
| B605 | Security (High) | 56 | Starting a process with a shell via `os.system` allows command injection. | Deleted the unused `printBadges` function entirely. |
| B301 | Security (Medium) | 51 | Use of `pickle` module is insecure and allows arbitrary code execution. | Replaced `pickle` with `json` for saving/loading data. |
| W0102 | Logic (Quality) | 11 | Dangerous default value `[]` as argument caused guests to share the same list. | Changed `guests=[]` to `guests=None` and initialized the list inside the function. |
| E225 | Style | 66 | Missing whitespace around operator. | Added spaces around the operator. |
| C0103 | Quality | Multiple | Function and argument names did not conform to snake_case. | Renamed `eventName` to `event_name`, `createEvent` to `create_event`, etc. |
| C0116 | Quality | Multiple | Missing function docstrings. | Added descriptive docstrings to all functions and the module. |