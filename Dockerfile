# Small, official Python base image (fewer packages = smaller attack surface).
# Pinned to the "bookworm" (Debian 12) variant rather than the default
# "slim", which currently resolves to Debian 13 ("trixie"). Trixie is new
# enough that most of its CVEs don't have upstream fixes yet, which makes
# vulnerability scanning far less useful. Bookworm is mature and stable,
# so far more of its known CVEs already have patches available.
FROM python:3.12-slim-bookworm

# Directory inside the container where our app will live
WORKDIR /app

# Copy only the dependency files first, then install.
# Docker caches this layer, so it's only re-run when dependencies change,
# not every time application code changes.
COPY requirements.txt requirements-dev.txt ./
RUN pip install --no-cache-dir -r requirements.txt -r requirements-dev.txt

# Now copy the rest of the project (source code, tests, pyproject.toml)
COPY . .

# Install our own package in the same way we do locally
RUN pip install --no-cache-dir -e .

# Default action when the container runs: execute the test suite
CMD ["pytest"]
