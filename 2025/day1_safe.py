# login to the website and receive input from a URL and store it in a variable

import os

from pathlib import Path



import requests





def _load_aoc_session():

    """AOC_SESSION from env, else project-root .env (works in WSL and Windows)."""

    val = os.getenv("AOC_SESSION")

    if val:

        return val

    env_file = Path(__file__).resolve().parent.parent / ".env"

    if not env_file.is_file():

        return None

    for line in env_file.read_text(encoding="utf-8").splitlines():

        line = line.strip()

        if not line or line.startswith("#") or "=" not in line:

            continue

        key, _, value = line.partition("=")

        if key.strip() == "AOC_SESSION":

            return value.strip().strip('"').strip("'")

    return None





AOC_SESSION = _load_aoc_session()

if not AOC_SESSION:

    raise SystemExit(

        "请设置 AOC_SESSION：\n"

        "  1) 环境变量 export AOC_SESSION=...（WSL）或 $env:AOC_SESSION=...（PowerShell）\n"

        "  2) 或在项目根目录创建 .env，内容：AOC_SESSION=你的cookie"

    )



session = requests.Session()

session.cookies.set("session", AOC_SESSION)



url = "https://adventofcode.com/2025/day/1/input"

response = session.get(url)



if response.status_code != 200 or "Please log in" in response.text:

    raise SystemExit(f"获取 input 失败 (HTTP {response.status_code})")



data = response.text.strip().split("\n")

n = len(data)
cur = 50
res = 0
for i,x in enumerate(data):
    num = 0
    if x[0] == 'L':
        num = -int(x[1:])
    elif x[0] == 'R':
        num = int(x[1:])
    else:
        raise ValueError(f"Invalid direction: {x}")
    
    cur = (cur + num) % 100
    if cur == 0:
        res += 1
print(res)
    

