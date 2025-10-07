FROM ghcr.io/astral-sh/uv:python3.11-alpine

# Create a non-root user to run the application
RUN addgroup -S nonroot \
    && adduser -S -G nonroot -h /home/nonroot nonroot

# Set environment variables for UV
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV UV_TOOL_BIN_DIR=/usr/local/bin

# Create application directory and set as working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies using UV
RUN uv sync --all-extras --all-groups

# Change ownership of the application directory and switch to non-root user
RUN chown -R nonroot:nonroot /app
USER nonroot

# Run sh
CMD ["sh"]
