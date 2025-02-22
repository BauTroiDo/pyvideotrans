# -*- coding: utf-8 -*-
import re
from videotrans.configure import config

GOOGLE_NAME = "Google"
MICROSOFT_NAME = "Microsoft"
AI302_NAME = "302.ai"
BAIDU_NAME = "Baidu"
DEEPL_NAME = "DeepL"
DEEPLX_NAME = "DeepLx"
OTT_NAME = "OTT"
TENCENT_NAME = "Tencent"
CHATGPT_NAME = "ChatGPT"
LOCALLLM_NAME = "LocalLLM"
ZIJIE_NAME = "ZijieHuoshan"
AZUREGPT_NAME = "AzureGPT"
GEMINI_NAME = "Gemini"
TRANSAPI_NAME = "TransAPI"
FREEGOOGLE_NAME = "FreeGoogle"
FREECHATGPT_NAME = "FreeChatGPT"
SRT_NAME = "srt"
# 翻译通道
TRANSNAMES = [
    MICROSOFT_NAME,
    #FREECHATGPT_NAME,
    GOOGLE_NAME,
    ZIJIE_NAME,
    AI302_NAME,
    BAIDU_NAME,
    DEEPL_NAME,
    CHATGPT_NAME,
    LOCALLLM_NAME,
    AZUREGPT_NAME,
    GEMINI_NAME,
    TENCENT_NAME,
    OTT_NAME,
    DEEPLX_NAME,
    TRANSAPI_NAME,
    FREEGOOGLE_NAME
]
# subtitles language code https://zh.wikipedia.org/wiki/ISO_639-2
LANG_CODE = {
    "zh-cn": [
        "zh-cn",  # google通道
        "chi",  # 字幕嵌入语言
        "zh",  # 百度通道
        "ZH",  # deepl deeplx通道
        "zh",  # 腾讯通道
        "zh",  # OTT通道
        "zh-Hans",# 微软翻译
        "Simplified Chinese" if config.defaulelang !='zh' else '简体中文' #AI翻译
    ],
    "zh-tw": [
        "zh-tw",
        "chi",
        "cht",
        "ZH",
        "zh-TW",
        "zt",
        "zh-Hant",
        "Traditional Chinese" if config.defaulelang !='zh' else '繁体中文'
    ],
    "en": [
        "en",
        "eng",
        "en",
        "EN-US",
        "en",
        "en",
        "en",
        "English language" if config.defaulelang !='zh' else '英语'
    ],
    "fr": [
        "fr",
        "fre",
        "fra",
        "FR",
        "fr",
        "fr",
        "fr",
        "French language" if config.defaulelang !='zh' else '法语'
    ],
    "de": [
        "de",
        "ger",
        "de",
        "DE",
        "de",
        "de",
        "de",
        "German language" if config.defaulelang !='zh' else '德语'
    ],
    "ja": [
        "ja",
        "jpn",
        "jp",
        "JA",
        "ja",
        "ja",
        "ja",
        "Japanese language" if config.defaulelang !='zh' else '日语'
    ],
    "ko": [
        "ko",
        "kor",
        "kor",
        "KO",
        "ko",
        "ko",
        "ko",
        "Korean language" if config.defaulelang !='zh' else '韩语'
    ],
    "ru": [
        "ru",
        "rus",
        "ru",
        "RU",
        "ru",
        "ru",
        "ru",
        "Russian language" if config.defaulelang !='zh' else '俄罗斯语'
    ],
    "es": [
        "es",
        "spa",
        "spa",
        "ES",
        "es",
        "es",
        "es",
        "Spanish language" if config.defaulelang !='zh' else '西班牙语'
    ],
    "th": [
        "th",
        "tha",
        "th",
        "No",
        "th",
        "th",
        "th",
        "Thai language" if config.defaulelang !='zh' else '泰国语'
    ],
    "it": [
        "it",
        "ita",
        "it",
        "IT",
        "it",
        "it",
        "it",
        "Italian language" if config.defaulelang !='zh' else '意大利语'
    ],
    "pt": [
        "pt",# pt-PT
        "por",
        "pt",
        "PT-PT",
        "pt",
        "pt",
        "pt",
        "Portuguese language" if config.defaulelang !='zh' else '葡萄牙语'
    ],
    "vi": [
        "vi",
        "vie",
        "vie",
        "No",
        "vi",
        "No",
        "vi",
        "Vietnamese language" if config.defaulelang !='zh' else '越南语'
    ],
    "ar": [
        "ar",
        "are",
        "ara",
        "AR",
        "ar",
        "ar",
        "ar",
        "Arabic language" if config.defaulelang !='zh' else '阿拉伯语'
    ],
    "tr": [
        "tr",
        "tur",
        "tr",
        "TR",
        "tr",
        "tr",
        "tr",
        "Turkish language" if config.defaulelang !='zh' else '土耳其语'
    ],
    "hi": [
        "hi",
        "hin",
        "hi",
        "No",
        "hi",
        "hi",
        "hi",
        "Hindi language" if config.defaulelang !='zh' else '印度语'
    ],
    "hu": [
        "hu",
        "hun",
        "hu",
        "HU",
        "No",
        "No",
        "hu",
        "Hungarian language" if config.defaulelang !='zh' else '匈牙利语'
    ],
    "uk":[
        "uk",
        "ukr",
        "ukr",#百度
        "UK",#deepl
        "No",#腾讯
        "No",#ott
        "uk",#微软
        "Ukrainian language" if config.defaulelang !='zh' else '乌克兰语'
    ],
    "id":[
        "id",
        "ind",
        "id",
        "ID",
        "id",
        "No",
        "id",
        "Indonesian language" if config.defaulelang !='zh' else '印度尼西亚语'
    ],
    "ms":[
        "ms",
        "may",
        "may",
        "No",
        "ms",
        "No",
        "ms",
        "Malay language" if config.defaulelang !='zh' else '马来西亚语'
    ],
    "kk":[
        "kk",
        "kaz",
        "No",
        "No",
        "No",
        "No",
        "kk",
        "Kazakh language" if config.defaulelang !='zh' else '哈萨克语'
    ],
    "cs":[
        "cs",
        "ces",
        "cs",
        "CS",
        "No",
        "No",
        "cs",
        "Czech language" if config.defaulelang !='zh' else '捷克语'
    ],
    "pl":[
        "pl",
        "pol",
        "pl",
        "PL",
        "No",
        "No",
        "pl",
        "Polish language" if config.defaulelang !='zh' else '波兰语'
    ],
    "nl":[
        "nl",  # google通道
        "dut",  # 字幕嵌入语言
        "nl",  # 百度通道
        "NL",  # deepl deeplx通道
        "No",  # 腾讯通道
        "No",  # OTT通道
        "nl",# 微软翻译
        "Dutch" if config.defaulelang !='zh' else '荷兰语' #AI翻译
    ]
}


# 根据界面显示的语言名称，比如“简体中文、English” 获取语言代码，比如 zh-cn en 等, 如果是cli，则直接是语言代码
def get_code(*, show_text=None):
    if not show_text or show_text == '-' :
        return None
    if show_text in LANG_CODE:
        return show_text
    if show_text in config.rev_langlist:
        return config.rev_langlist[show_text]
    return None


# 根据显示的语言和翻译通道，获取该翻译通道要求的源语言代码和目标语言代码
# translate_type翻译通道
# show_source翻译后显示的原语言名称
# show_target 翻译后显示的目标语言名称
# 如果是cli，则show均是语言代码
def get_source_target_code(*, show_source=None, show_target=None, translate_type=None):
    source_list = None
    target_list = None
    if not translate_type:
        return None, None
    lower_translate_type = translate_type.lower()
    if show_source:
        source_list = LANG_CODE[show_source] if show_source in LANG_CODE else LANG_CODE[
            config.rev_langlist[show_source]]
    if show_target:
        target_list = LANG_CODE[show_target] if show_target in LANG_CODE else LANG_CODE[
            config.rev_langlist[show_target]]
    if lower_translate_type in [GOOGLE_NAME.lower(), TRANSAPI_NAME.lower(),FREEGOOGLE_NAME.lower() ]:
        return (source_list[0] if source_list else "-", target_list[0] if target_list else "-")
    elif lower_translate_type == BAIDU_NAME.lower():
        return (source_list[2] if source_list else "-", target_list[2] if target_list else "-")
    elif lower_translate_type in [DEEPLX_NAME.lower(), DEEPL_NAME.lower()]:
        return (source_list[3] if source_list else "-", target_list[3] if target_list else "-")
    elif lower_translate_type == TENCENT_NAME.lower():
        return (source_list[4] if source_list else "-", target_list[4] if target_list else "-")
    elif lower_translate_type in [CHATGPT_NAME.lower(), AZUREGPT_NAME.lower(), GEMINI_NAME.lower(),LOCALLLM_NAME.lower(),ZIJIE_NAME.lower(),AI302_NAME.lower()]:
       return (source_list[7] if source_list else "-", target_list[7] if target_list else "-")
    elif lower_translate_type == OTT_NAME.lower():
        return (source_list[5] if source_list else "-", target_list[5] if target_list else "-")
    elif lower_translate_type==MICROSOFT_NAME.lower():
        return (source_list[6] if source_list else "-", target_list[6] if target_list else "-")
    else:
        raise Exception(f"[error]get_source_target_code:{translate_type=},{show_source=},{show_target=}")


# 判断当前翻译通道和目标语言是否允许翻译
# 比如deepl不允许翻译到某些目标语言，某些通道是否填写api key 等
# translate_type翻译通道
# show_target 翻译后显示的目标语言名称
# only_key=True 仅检测 key 和api，不判断目标语言
def is_allow_translate(*, translate_type=None, show_target=None, only_key=False):
    lower_translate_type = translate_type.lower()

    if lower_translate_type == CHATGPT_NAME.lower() and not config.params['chatgpt_key']:
        return config.transobj['chatgptkeymust']
    if lower_translate_type == AI302_NAME.lower() and not config.params['ai302_key']:
        return '必须填写 302.ai 平台的 sk'

    if lower_translate_type == LOCALLLM_NAME.lower() and not config.params['localllm_api']:
        return '必须填写本地大模型API地址' if config.defaulelang=='zh' else 'Please input Local LLM API url'
    if lower_translate_type == ZIJIE_NAME.lower() and (not config.params['zijiehuoshan_model'].strip() or not config.params['zijiehuoshan_key'].strip()):
        return '必须填写字节火山api_key和推理接入点'

    if lower_translate_type == GEMINI_NAME.lower() and not config.params['gemini_key']:
        return config.transobj['chatgptkeymust']
    if lower_translate_type == AZUREGPT_NAME.lower() and (
            not config.params['azure_key'] or not config.params['azure_api']):
        return 'No Azure key'

    if lower_translate_type == BAIDU_NAME.lower() and (
            not config.params["baidu_appid"] or not config.params["baidu_miyue"]):
        return config.transobj['baikeymust']
    if lower_translate_type == TENCENT_NAME.lower() and (
            not config.params["tencent_SecretId"] or not config.params["tencent_SecretKey"]):
        return config.transobj['tencent_key']
    if lower_translate_type == DEEPL_NAME.lower() and not config.params["deepl_authkey"]:
        return config.transobj['deepl_authkey']
    if lower_translate_type == DEEPLX_NAME.lower() and not config.params["deeplx_address"]:
        return config.transobj['setdeeplx_address']

    if lower_translate_type == TRANSAPI_NAME.lower() and not config.params["trans_api_url"]:
        return "必须配置自定义翻译api的地址" if config.defaulelang=='zh' else "The address of the custom translation api must be configured"

    if lower_translate_type == OTT_NAME.lower() and not config.params["ott_address"]:
        return config.transobj['setott_address']

    if only_key:
        return True
    #再判断是否为No，即不支持
    index = 0
    if lower_translate_type == BAIDU_NAME.lower():
        index = 2
    elif lower_translate_type in [DEEPLX_NAME.lower(), DEEPL_NAME.lower()]:
        index = 3
    elif lower_translate_type == TENCENT_NAME.lower():
        index = 4
    elif lower_translate_type==MICROSOFT_NAME.lower():
        index=6

    if show_target:
        target_list = LANG_CODE[show_target] if show_target in LANG_CODE else LANG_CODE[
            config.rev_langlist[show_target]]
        if target_list[index].lower() == 'no':
            return config.transobj['deepl_nosupport']

    return True


# 获取用于进行语音识别的预设语言，比如语音是英文发音、中文发音
# 根据 原语言进行判断,基本等同于google，但只保留_之前的部分
def get_audio_code(*, show_source=None):
    source_list = LANG_CODE[show_source] if show_source in LANG_CODE else LANG_CODE[config.rev_langlist[show_source]]
    return re.split(r'_|-', source_list[0])[0]


# 获取嵌入软字幕的3位字母语言代码，根据目标语言确定
def get_subtitle_code(*, show_target=None):
    if show_target in LANG_CODE:
        return LANG_CODE[show_target][1]
    if show_target in config.rev_langlist:
        return LANG_CODE[config.rev_langlist[show_target]][1]

    return 'eng'


# 翻译,先根据翻译通道和目标语言，取出目标语言代码
def run(*, translate_type=None, text_list=None, target_language_name=None, set_p=True,inst=None,source_code=None):
    _, target_language = get_source_target_code(show_target=target_language_name, translate_type=translate_type)
    lower_translate_type = translate_type.lower()
    if lower_translate_type == GOOGLE_NAME.lower():
        from videotrans.translator.google import trans
    elif lower_translate_type==FREEGOOGLE_NAME.lower():
        from videotrans.translator.freegoogle import trans
    elif lower_translate_type == BAIDU_NAME.lower():
        from videotrans.translator.baidu import trans
    elif lower_translate_type == DEEPL_NAME.lower():
        from videotrans.translator.deepl import trans
    elif lower_translate_type == DEEPLX_NAME.lower():
        from videotrans.translator.deeplx import trans
    elif lower_translate_type == OTT_NAME.lower():
        from videotrans.translator.ott import trans
    elif lower_translate_type == TENCENT_NAME.lower():
        from videotrans.translator.tencent import trans
    elif lower_translate_type == CHATGPT_NAME.lower():
        from videotrans.translator.chatgpt import trans
    elif lower_translate_type == AI302_NAME.lower():
        from videotrans.translator.ai302 import trans
    elif lower_translate_type == LOCALLLM_NAME.lower():
        from videotrans.translator.localllm import trans
    elif lower_translate_type == ZIJIE_NAME.lower():
       from videotrans.translator.huoshan import trans
    elif lower_translate_type == GEMINI_NAME.lower():
        from videotrans.translator.gemini import trans
    elif lower_translate_type == AZUREGPT_NAME.lower():
        from videotrans.translator.azure import trans
    elif lower_translate_type==MICROSOFT_NAME.lower():
        from videotrans.translator.microsoft import trans
    elif lower_translate_type==TRANSAPI_NAME.lower():
        from videotrans.translator.transapi import trans
    else:
        raise Exception(f"{translate_type=},{target_language_name=}")
    return trans(text_list, target_language, set_p=set_p,inst=inst,source_code=source_code)
