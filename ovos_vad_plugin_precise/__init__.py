from os.path import join, dirname
from ovos_utils.log import LOG
from ovos_plugin_manager.templates.vad import VADEngine
from precise_lite_runner.runner import Listener


class PreciseVAD(VADEngine):
    def __init__(self, config=None, sample_rate=None):
        super().__init__(config, sample_rate)
        model = self.config.get("model") or join(dirname(__file__), "vad.tflite")
        self.vad_threshold = self.config.get("threshold", 0.35)
        self.debug = self.config.get("debug", False)
        self.vad = Listener(model)

    def is_silence(self, chunk):
        # return True or False
        prob = self.vad.get_prediction(chunk)
        if self.debug:
            LOG.debug(f"speech probability: {prob}")
        return prob < self.vad_threshold
