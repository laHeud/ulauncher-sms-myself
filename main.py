import json
import logging
import subprocess
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction


logger = logging.getLogger(__name__)


class SmsExtension(Extension):

    def __init__(self):
        super(SmsExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, RunCommand())

class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        command = event.get_argument()
        data = { "command": command }
        logger.warn(data)


        return RenderResultListAction([ExtensionResultItem(icon='images/sms.png',
                                         name='Send %s' % (command),
                                         on_enter=ExtensionCustomAction(data))])

class RunCommand(EventListener):

    def on_event(self, event, extension):

        data = event.get_data()

        user = extension.preferences["user"]
        passwd = extension.preferences["pass"]
        command = data["command"]
        logger.warn(user)

        # subprocess.run(["/bin/terminator", "-c", "print('ocean')"])

        return HideWindowAction()


if __name__ == '__main__':
    SmsExtension().run()
