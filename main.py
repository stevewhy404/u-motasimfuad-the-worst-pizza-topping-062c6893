import os

LINE = "New topping: wet socks marinated in expired yogurt, baked onto a crust so soggy it asked for a divorce."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
