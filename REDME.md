# UV vs Poetry - Speed Benchmark

This repository exists to compare the speed of UV and Poetry, mainly focusing on dependency resolution and installation time.

I’m keeping this benchmark intentionally simple and practical. The main question I want to answer is:

>  How much time are we wasting per CI run or per local install?

I’ll also test both tools inside a Docker container, since I have a hypothesis that the results may differ there.
Spoiler alert: I expect UV to win  but let’s measure instead of guessing 🙂



## TODO: Benchmark Improvements

Things already done and things planned to make the benchmark more accurate and fair.

> For now I'm kinda satisfied with the result

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
