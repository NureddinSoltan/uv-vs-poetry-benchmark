# UV vs Poetry - Speed Benchmark

This repository exists to compare the speed of UV and Poetry, mainly focusing on dependency resolution and installation time.

I’m keeping this benchmark simple and practical. The main question I want to answer is:

>  How much time are we wasting per CI run or per local install?

I’ll also test both tools inside a Docker container, since I have a hypothesis that the results may differ there.
Spoiler alert: I expect UV to win, but let’s measure instead of guessing 🙂

## How to run it:
1. Open the **uv_vs_poetry** folder.
2. run either `uv_vs_poetry.py` or `uv_vs_poetry_no_lock_files.py`


## Libraries used for testing (49 libraries)
```bash
django django-bolt django-rest-api fastapi pymongo loguru jinja2 passlib pyjwt cryptography boto3 fernet-cli pillow python-multipart rq base32-crockford requests faker ruamel-yaml s3cmd pytest snakeviz bcrypt xlsxwriter ruff pre-commit httpx weasyprint dateparser net-tools sysstat gnureadline pd pympler pydantic firebase-admin premailer sentry-sdk langchain langchain-openai langchain-google-genai langchain-anthropic opencv-python qrcode numpy pandas openpyxl pymupdf mongomock
```

## TODO: Benchmark Improvements
> For now, I’m mostly satisfied with the results and feel they answer the comparison question. In the future, we can improve the benchmark to make it more solid and accurate.

### Completed

- [x] Basic benchmark script with timing
- [x] Test with lock files (installation only)
- [x] Test without lock files (resolution + installation)
- [x] Export results to JSON
- [x] Clean virtual environment between runs
- [x] Add timestamp to results

### Planned

- [ ] Include timestamp in output summary.
- [ ] Record number of dependencies installed
- [ ] Track disk space used by each tool
- [ ] Test with cold cache (clear cache before running)
- [ ] Test with warm cache (run twice, use the second result)
- [ ] Run multiple iterations (3–5 runs) and calculate averages
<!-- - [ ] Fully document the test environment: -->

  <!-- - [ ] Python version -->
  <!-- - [ ] OS and version -->
  <!-- - [ ] Internet speed / network conditions -->
  <!-- - [ ] Total number of dependencies in `pyproject.toml` -->
<!-- - [ ] Test offline installation (if possible) -->
<!-- - [ ] Add charts/graphs for visual comparison -->
- [ ] Add Docker / Docker Compose benchmarks (including image size)

