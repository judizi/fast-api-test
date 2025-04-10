import os
import sys

if len(sys.argv) < 2:
    base_dir = os.path.abspath(os.path.dirname(__file__))
    try:
        os.system(f"echo 'ENV=development' > {base_dir}/app/.env")
        os.system(f"fastapi dev {base_dir}/app/main.py")
    except SystemExit:
        sys.exit(0)
else:
    if sys.argv[1] == "prod":
        os.system("echo 'ENV=production' > app/.env")
        os.system(f"PYTHONPATH=./app gunicorn app.main:app -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000")
        