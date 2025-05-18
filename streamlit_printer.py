class StreamlitPrinter:
    def __init__(self, write_stream, err_stream=None):
        """
        :param write_stream: Callable that handles standard output (e.g., st.write or similar)
        :param err_stream: Optional callable for logging errors (e.g., st.error or similar)
        """
        self.write_stream = write_stream
        self.err_stream = err_stream or write_stream  # fallback if no error stream is provided

    def print_header(self):
        # You can customize this to show a session header, etc.
        self.write_stream("📡 WebRTC Stream Started")

    def print_token(self, token: str):
        self.write_stream(token)

    def log(self, level: str, msg: str):
        level = level.lower()
        if level == "info":
            self.err_stream(f"ℹ️ {msg}")
        elif level == "warning":
            self.err_stream(f"⚠️ {msg}")
        elif level == "error":
            self.err_stream(f"❌ {msg}")
        else:
            self.err_stream(f"{level.upper()}: {msg}")

    def print_lag(self):
        self.err_stream("🔴 [LAG DETECTED]")

    def print_pending(self):
        self.write_stream("⏳ Awaiting WebRTC connection...")