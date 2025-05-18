import streamlit as st
import logging
from streamlit_webrtc import webrtc_streamer, WebRtcMode,  AudioProcessorBase #, ClientSettings
# import av
import time
import pydub
import numpy as np
import queue
import threading
from example import app_sst

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    import os

    DEBUG = os.environ.get("DEBUG", "false").lower() not in ["false", "no", "0"]

    logging.basicConfig(
        format="[%(asctime)s] %(levelname)7s from %(name)s in %(pathname)s:%(lineno)d: "
        "%(message)s",
        force=True,
    )

    logger.setLevel(level=logging.DEBUG if DEBUG else logging.INFO)

    st_webrtc_logger = logging.getLogger("streamlit_webrtc")
    st_webrtc_logger.setLevel(logging.DEBUG)

    fsevents_logger = logging.getLogger("fsevents")
    fsevents_logger.setLevel(logging.WARNING)


    # Streamlit UI
    st.title("Real-Time Speech-to-Speech Translation")

    app_sst()

# webrtc_ctx = webrtc_streamer(
#     key="speech-translation",
#     mode=WebRtcMode.SENDONLY,
#     audio_receiver_size=1024,
#     client_settings=ClientSettings(
#         media_stream_constraints={"video": False, "audio": True},
#         rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
#     ),
#     audio_processor_factory=lambda: processor_instance,
# )
