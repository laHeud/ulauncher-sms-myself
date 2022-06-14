import json
import logging
import requests
import os
from time import sleep
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

logger = logging.getLogger(__name__)


class SmsExtension(Extension):

    def __init__(self):
        super(SmsExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):

        raw_str = event.get_argument()
        url = "https://smsapi.free-mobile.fr/sendmsg"

        payload = json.dumps({
                "user": extension.preferences['user'],
                "pass": extension.preferences['pass'],
                "msg": raw_str })
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

        return RunScriptAction()



if __name__ == '__main__':
    SmsExtension().run()
