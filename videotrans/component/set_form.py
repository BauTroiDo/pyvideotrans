# set baidu appid and secrot
from PySide6 import QtCore
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog

from videotrans.configure import config
from videotrans.ui.ai302 import Ui_ai302form
from videotrans.ui.ai302tts import Ui_ai302ttsform
from videotrans.ui.article import Ui_articleform
from videotrans.ui.azure import Ui_azureform
from videotrans.ui.baidu import Ui_baiduform
from videotrans.ui.chatgpt import Ui_chatgptform
from videotrans.ui.chattts import Ui_chatttsform
from videotrans.ui.cosyvoice import Ui_cosyvoiceform
from videotrans.ui.deepl import Ui_deeplform
from videotrans.ui.deeplx import Ui_deeplxform
from videotrans.ui.fishtts import Ui_fishttsform
from videotrans.ui.gptsovits import Ui_gptsovitsform
from videotrans.ui.localllm import Ui_localllmform
from videotrans.ui.ott import Ui_ottform
from videotrans.ui.clone import Ui_cloneform
from videotrans.ui.gemini import Ui_geminiform
from videotrans.ui.info import Ui_infoform
from videotrans.ui.setini import Ui_setini
from videotrans.ui.setlinerole import Ui_setlinerole
from videotrans.ui.srthebing import Ui_srthebing
from videotrans.ui.tencent import Ui_tencentform
from videotrans.ui.elevenlabs import Ui_elevenlabsform
from videotrans.ui.transapi import Ui_transapiform
from videotrans.ui.ttsapi import Ui_ttsapiform
from videotrans.ui.youtube import Ui_youtubeform
from videotrans.ui.separate import Ui_separateform
from videotrans.ui.azuretts import Ui_azurettsform
from videotrans.ui.zh_recogn import Ui_zhrecognform
from videotrans.ui.zijiehuoshan import Ui_zijiehuoshanform
from videotrans.ui.doubao import Ui_doubaoform


class SetLineRole(QDialog, Ui_setlinerole):  # <===
    def __init__(self, parent=None):
        super(SetLineRole, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(f"{config.rootdir}/videotrans/styles/icon.ico"))

class BaiduForm(QDialog, Ui_baiduform):  # <===
    def __init__(self, parent=None):
        super(BaiduForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(f"{config.rootdir}/videotrans/styles/icon.ico"))


class YoutubeForm(QDialog, Ui_youtubeform):  # <===
    def __init__(self, parent=None):
        super(YoutubeForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(f"{config.rootdir}/videotrans/styles/icon.ico"))
        config.canceldown=False
    def closeEvent(self, event):
        config.canceldown=True

class SeparateForm(QDialog, Ui_separateform):  # <===
    def __init__(self, parent=None):
        super(SeparateForm, self).__init__(parent)
        self.task=None
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(f"{config.rootdir}/videotrans/styles/icon.ico"))
    def closeEvent(self, event):
        config.separate_status='stop'
        if self.task:
            self.task.finish_event.emit("end")
            self.task=None
        self.hide()
        event.ignore()


class TencentForm(QDialog, Ui_tencentform):  # <===
    def __init__(self, parent=None):
        super(TencentForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(f"{config.rootdir}/videotrans/styles/icon.ico"))

class TtsapiForm(QDialog, Ui_ttsapiform):  # <===
    def __init__(self, parent=None):
        super(TtsapiForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(f"{config.rootdir}/videotrans/styles/icon.ico"))

class TransapiForm(QDialog, Ui_transapiform):  # <===
    def __init__(self, parent=None):
        super(TransapiForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(f"{config.rootdir}/videotrans/styles/icon.ico"))


class GPTSoVITSForm(QDialog, Ui_gptsovitsform):  # <===
    def __init__(self, parent=None):
        super(GPTSoVITSForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(f"{config.rootdir}/videotrans/styles/icon.ico"))

class CosyVoiceForm(QDialog, Ui_cosyvoiceform):  # <===
    def __init__(self, parent=None):
        super(CosyVoiceForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(f"{config.rootdir}/videotrans/styles/icon.ico"))


class FishTTSForm(QDialog, Ui_fishttsform):  # <===
    def __init__(self, parent=None):
        super(FishTTSForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(f"{config.rootdir}/videotrans/styles/icon.ico"))


class AI302Form(QDialog, Ui_ai302form):  # <===
    def __init__(self, parent=None):
        super(AI302Form, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(f"{config.rootdir}/videotrans/styles/icon.ico"))


class AI302TTSForm(QDialog, Ui_ai302ttsform):  # <===
    def __init__(self, parent=None):
        super(AI302TTSForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(f"{config.rootdir}/videotrans/styles/icon.ico"))



class SetINIForm(QDialog, Ui_setini):  # <===
    def __init__(self, parent=None):
        super(SetINIForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(f"{config.rootdir}/videotrans/styles/icon.ico"))




class DeepLForm(QDialog, Ui_deeplform):  # <===
    def __init__(self, parent=None):
        super(DeepLForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(f"{config.rootdir}/videotrans/styles/icon.ico"))
        
class AzurettsForm(QDialog, Ui_azurettsform):  # <===
    def __init__(self, parent=None):
        super(AzurettsForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(f"{config.rootdir}/videotrans/styles/icon.ico"))

class ElevenlabsForm(QDialog, Ui_elevenlabsform):  # <===
    def __init__(self, parent=None):
        super(ElevenlabsForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(f"{config.rootdir}/videotrans/styles/icon.ico"))


class InfoForm(QDialog, Ui_infoform):  # <===
    def __init__(self, parent=None):
        super(InfoForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(f"{config.rootdir}/videotrans/styles/icon.ico"))

class ArticleForm(QDialog, Ui_articleform):  # <===
    def __init__(self, parent=None):
        super(ArticleForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(f"{config.rootdir}/videotrans/styles/icon.ico"))


class DeepLXForm(QDialog, Ui_deeplxform):  # <===
    def __init__(self, parent=None):
        super(DeepLXForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(f"{config.rootdir}/videotrans/styles/icon.ico"))

class OttForm(QDialog, Ui_ottform):  # <===
    def __init__(self, parent=None):
        super(OttForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(f"{config.rootdir}/videotrans/styles/icon.ico"))
class CloneForm(QDialog, Ui_cloneform):  # <===
    def __init__(self, parent=None):
        super(CloneForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(f"{config.rootdir}/videotrans/styles/icon.ico"))
class ChatttsForm(QDialog, Ui_chatttsform):  # <===
    def __init__(self, parent=None):
        super(ChatttsForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(f"{config.rootdir}/videotrans/styles/icon.ico"))

class ZhrecognForm(QDialog, Ui_zhrecognform):  # <===
    def __init__(self, parent=None):
        super(ZhrecognForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(f"{config.rootdir}/videotrans/styles/icon.ico"))


class DoubaoForm(QDialog, Ui_doubaoform):  # <===
    def __init__(self, parent=None):
        super(DoubaoForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(f"{config.rootdir}/videotrans/styles/icon.ico"))


# set chatgpt api and key
class ChatgptForm(QDialog, Ui_chatgptform):  # <===
    def __init__(self, parent=None):
        super(ChatgptForm, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(f"{config.rootdir}/videotrans/styles/icon.ico"))

class LocalLLMForm(QDialog, Ui_localllmform):  # <===
    def __init__(self, parent=None):
        super(LocalLLMForm, self).__init__(parent)
        self.setupUi(self)
        self.localllm_model.addItems(config.localllm_model_list)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(f"{config.rootdir}/videotrans/styles/icon.ico"))

class ZijiehuoshanForm(QDialog, Ui_zijiehuoshanform):  # <===
    def __init__(self, parent=None):
        super(ZijiehuoshanForm, self).__init__(parent)
        self.setupUi(self)
        self.zijiehuoshan_model.addItems(config.zijiehuoshan_model_list)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(f"{config.rootdir}/videotrans/styles/icon.ico"))

class HebingsrtForm(QDialog, Ui_srthebing):  # <===
    def __init__(self, parent=None):
        super(HebingsrtForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(f"{config.rootdir}/videotrans/styles/icon.ico"))


class GeminiForm(QDialog, Ui_geminiform):  # <===
    def __init__(self, parent=None):
        super(GeminiForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(f"{config.rootdir}/videotrans/styles/icon.ico"))

class AzureForm(QDialog, Ui_azureform):  # <===
    def __init__(self, parent=None):
        super(AzureForm, self).__init__(parent)
        self.setupUi(self)
        self.azure_model.addItems(config.azure_model_list)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(f"{config.rootdir}/videotrans/styles/icon.ico"))

