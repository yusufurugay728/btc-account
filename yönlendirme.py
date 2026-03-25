import base64 as b
import webbrowser as w

x = "aHR0cHM6Ly93d3cubGlua2VkaW4uY29tL2luL3l1c3VmLXVyZ2F5LTJiNzI0OTNiYS8/aXNTZWxmUHJvZmlsZT10cnVl"

u = b.b64decode(x[::-1][::-1]).decode()

w.open(u)
